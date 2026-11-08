const { spawn } = require('child_process');
const http = require('http');
const ioClient = require('socket.io-client');

const PORT = 3007;
const SERVER_URL = `http://localhost:${PORT}`;

async function runTests() {
  console.log('====================================================');
  console.log('🧪 BẮT ĐẦU KIỂM THỬ TOÀN DIỆN GAME RUNG CHUÔNG VÀNG');
  console.log('====================================================\n');

  // 1. Khởi động server
  console.log(`[1/5] Khởi động Game Server trên cổng ${PORT}...`);
  const serverEnv = { ...process.env, PORT: String(PORT), QUESTION_DURATION: '30' };
  const serverProcess = spawn('node', ['server.js'], {
    cwd: '/workspace/tiktok-live-game-skill/games/rung-chuong-vang',
    env: serverEnv,
    stdio: ['ignore', 'pipe', 'pipe']
  });

  serverProcess.stderr.on('data', data => {
    console.error(`[Server Error] ${data.toString().trim()}`);
  });

  // Đợi server sẵn sàng
  await new Promise(resolve => setTimeout(resolve, 2000));

  let testsPassed = 0;
  let testsFailed = 0;

  function assert(condition, message) {
    if (condition) {
      console.log(`  ✅ PASS: ${message}`);
      testsPassed++;
    } else {
      console.error(`  ❌ FAIL: ${message}`);
      testsFailed++;
    }
  }

  // 2. Kiểm tra HTTP Endpoints
  console.log('\n[2/5] Kiểm tra các HTTP Endpoints...');

  const httpGet = (path) => new Promise((resolve, reject) => {
    http.get(`${SERVER_URL}${path}`, res => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve({ status: res.statusCode, headers: res.headers, body: data }));
    }).on('error', reject);
  });

  try {
    const resHome = await httpGet('/');
    assert(resHome.status === 200, 'GET / trả về HTTP 200 OK');
    assert(resHome.body.includes('Đấu Trí Trạng Nguyên') || resHome.body.includes('Rung Chuông Vàng'), 'Màn hình Game HTML có chứa tiêu đề hợp lệ');
    assert(resHome.body.includes('live-toast'), 'Màn hình Game HTML chứa phần tử Live Action Toast');

    const resAdmin = await httpGet('/admin.html');
    assert(resAdmin.status === 200, 'GET /admin.html trả về HTTP 200 OK');
    assert(resAdmin.body.includes('sendMemberJoin') && resAdmin.body.includes('sendShare'), 'Trang Admin chứa các nút giả lập tương tác mới (Member, Share)');

    const resQuestions = await httpGet('/api/questions');
    assert(resQuestions.status === 200, 'GET /api/questions trả về HTTP 200 OK');
    const questionsData = JSON.parse(resQuestions.body);
    const count = questionsData.total || (questionsData.data && questionsData.data.length);
    assert(count >= 200, `Ngân hàng câu hỏi API trả về ${count} câu (>= 200 câu)`);

    const resTts = await httpGet('/api/tts?text=Xin%20chao%20cac%20si%20tu');
    assert(resTts.status === 200 || resTts.status === 302, `API TTS trả về mã HTTP ${resTts.status}`);
  } catch (err) {
    assert(false, `Lỗi khi kiểm tra HTTP: ${err.message}`);
  }

  // 3. Kết nối Socket.IO Client & Lấy State ban đầu
  console.log('\n[3/5] Kiểm tra Kết nối Socket.IO & Trạng thái khởi tạo...');
  const socket = ioClient(SERVER_URL, { reconnection: false });

  await new Promise(resolve => {
    socket.on('connect', () => {
      assert(true, 'Kết nối Socket.IO thành công');
      socket.emit('get_state');
    });

    socket.once('game_state', state => {
      assert(state.status === 'WAITING', `Trạng thái khởi tạo là WAITING (thực tế: ${state.status})`);
      assert(state.totalPlayers === 0, `Sàn đấu ban đầu chưa có thí sinh (${state.totalPlayers} thí sinh)`);
      resolve();
    });
  });

  // 4. Kiểm tra Tương tác & Sự kiện: Thêm Bot, Member Join, Share, Thả Tim
  console.log('\n[4/5] Kiểm tra Sự kiện Khán giả: Thêm Bot, Member Join, Share, Like...');
  
  let memberReceived = false;
  let shareReceived = false;
  let likeReceived = false;

  socket.on('member_join', data => {
    memberReceived = true;
    assert(data.nickname === 'Trần Anh Tuấn', `Sự kiện member_join hoạt động tốt: "${data.nickname}"`);
  });

  socket.on('share', data => {
    shareReceived = true;
    assert(data.nickname === 'Lê Bảo Châu', `Sự kiện share hoạt động tốt: "${data.nickname}"`);
  });

  socket.on('like', data => {
    likeReceived = true;
    assert(data.likeCount === 250, `Sự kiện like nhận được ${data.likeCount} tim`);
  });

  socket.emit('mock:member', { nickname: 'Trần Anh Tuấn' });
  socket.emit('mock:share', { nickname: 'Lê Bảo Châu' });
  socket.emit('mock:like', { likeCount: 250, nickname: 'Lê Bảo Châu' });
  socket.emit('mock:add_bots');

  await new Promise(resolve => setTimeout(resolve, 800));
  assert(memberReceived, 'Nhận sự kiện member_join thành công');
  assert(shareReceived, 'Nhận sự kiện share thành công');
  assert(likeReceived, 'Nhận sự kiện like thành công');

  // 5. Kiểm tra Chu trình Vòng thi: Bắt đầu câu hỏi -> Bot trả lời -> Auto Fast Forward (4s) -> Reveal
  console.log('\n[5/5] Kiểm tra Logic Vòng thi, Chốt đáp án sớm (checkAllAnswered), MC Speech & Công bố đáp án...');

  let questionStarted = false;
  let allAnsweredTriggered = false;
  let mcSpeechReceived = false;
  let revealReceived = false;

  socket.on('mc_speech', data => {
    if (!mcSpeechReceived) {
      mcSpeechReceived = true;
      console.log(`  🎙️ [MC TTS Voice Event]: "${data.text}" (priority: ${data.priority})`);
      assert(true, 'Nhận được sự kiện giọng nói MC (mc_speech)');
    }
  });

  socket.once('question_start', data => {
    questionStarted = true;
    assert(true, `Bắt đầu câu hỏi: "${data.question.question.substring(0, 50)}..."`);
    assert(data.question.options.length === 4, 'Đủ 4 lựa chọn A, B, C, D');

    // Sau khi bắt đầu câu hỏi 1.2 giây, gửi lệnh bot trả lời toàn bộ
    setTimeout(() => {
      console.log('  👉 Gửi lệnh cho toàn bộ thí sinh bot chốt đáp án...');
      socket.emit('mock:bots_answer');
    }, 1200);
  });

  socket.on('all_answered', data => {
    allAnsweredTriggered = true;
    assert(true, `Tính năng chốt đáp án sớm kích hoạt: "${data.message}" (timer còn: ${data.timer}s)`);
  });

  socket.once('question_reveal', data => {
    revealReceived = true;
    assert(true, `Công bố kết quả câu hỏi thành công!`);
    assert(data.correctLetter !== undefined, `Đáp án đúng là: ${data.correctLetter}`);
    assert(typeof data.aliveCount === 'number', `Số thí sinh còn sống: ${data.aliveCount}/${data.totalPlayers}`);
  });

  // Bắt đầu game
  socket.emit('mock:start_game');

  // Đợi vòng thi chạy xong và công bố kết quả (khoảng 8 giây vì sau khi all_answered timer rút còn 4s)
  for (let i = 0; i < 10; i++) {
    await new Promise(r => setTimeout(r, 1000));
    if (revealReceived) break;
  }

  assert(questionStarted, 'Câu hỏi bắt đầu thành công');
  assert(allAnsweredTriggered, 'Sự kiện all_answered đã kích hoạt khi toàn bộ thí sinh trả lời');
  assert(revealReceived, 'Công bố kết quả (question_reveal) hoàn thành chuẩn xác');

  // Dọn dẹp tiến trình
  console.log('\n====================================================');
  console.log(`📊 TỔNG KẾT KIỂM THỬ: ${testsPassed} ĐẠT, ${testsFailed} THẤT BẠI`);
  console.log('====================================================');

  socket.disconnect();
  serverProcess.kill('SIGINT');

  process.exit(testsFailed === 0 ? 0 : 1);
}

runTests().catch(err => {
  console.error('Fatal error during test:', err);
  process.exit(1);
});
