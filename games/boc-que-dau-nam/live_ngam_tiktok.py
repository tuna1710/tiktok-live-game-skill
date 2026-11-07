# -*- coding: utf-8 -*-
"""
Colab Runner Mode B: Hands-Free Live Ngầm TikTok (Không Cần OBS / Máy Tính)
Tự động dựng màn hình ảo Xvfb, mở Chrome toàn màn hình và dùng FFmpeg đẩy trực tiếp lên TikTok Live qua RTMP.
"""
import os
import sys
import time
import subprocess
import urllib.request
import argparse
import signal

def parse_args():
    parser = argparse.ArgumentParser(description="Live ngầm TikTok Game trên Google Colab")
    parser.add_argument("--stream-url", type=str, default=os.environ.get("TIKTOK_STREAM_URL", "rtmp://live-push.tiktok.com/live/"), help="Máy chủ phát trực tiếp TikTok (RTMP URL)")
    parser.add_argument("--stream-key", type=str, default=os.environ.get("TIKTOK_STREAM_KEY", ""), help="Khóa luồng TikTok (Stream Key)")
    parser.add_argument("--tiktok-username", type=str, default=os.environ.get("TIKTOK_USERNAME", ""), help="Tên tài khoản TikTok (ví dụ: @tuna171095)")
    parser.add_argument("--width", type=int, default=1080, help="Độ rộng màn hình (mặc định: 1080)")
    parser.add_argument("--height", type=int, default=1920, help="Chiều cao màn hình (mặc định: 1920)")
    parser.add_argument("--fps", type=int, default=30, help="Tốc độ khung hình (mặc định: 30)")
    return parser.parse_args()

def find_chrome():
    for cmd in ["google-chrome", "google-chrome-stable", "chromium-browser", "chromium", "/usr/bin/google-chrome"]:
        if subprocess.call(["which", cmd], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
            return cmd
    return None

def check_and_install_dependencies():
    print("📦 [1/5] Kiểm tra và cài đặt công cụ hệ thống...")
    need_apt = []
    if subprocess.call(["which", "Xvfb"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
        need_apt.append("xvfb")
    if subprocess.call(["which", "ffmpeg"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
        need_apt.append("ffmpeg")
    if subprocess.call(["which", "pulseaudio"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
        need_apt.append("pulseaudio")

    if need_apt:
        print(f"📥 Đang cài đặt: {', '.join(need_apt)}...")
        try:
            subprocess.run(["apt-get", "update", "-qq"], check=True)
            subprocess.run(["apt-get", "install", "-y", "-qq"] + need_apt, check=True)
        except Exception as e:
            print(f"⚠️ Cảnh báo apt-get: {e}")

    if not find_chrome():
        print("📥 Đang cài đặt Google Chrome...")
        try:
            chrome_deb = "/tmp/google-chrome-stable_current_amd64.deb"
            urllib.request.urlretrieve("https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb", chrome_deb)
            subprocess.run(["apt-get", "update", "-qq"], check=False)
            subprocess.run(["apt-get", "install", "-y", "-qq", chrome_deb], check=True)
            if os.path.exists(chrome_deb):
                os.remove(chrome_deb)
        except Exception as e:
            print(f"⚠️ Cài đặt Chrome deb lỗi ({e}), chuyển sang chromium-browser...")
            subprocess.run(["apt-get", "install", "-y", "-qq", "chromium-browser"], check=False)

def main():
    args = parse_args()
    print("=" * 70)
    print("🔴 TỰ ĐỘNG PHÁT LIVE NGẦM TIKTOK TRỰC TIẾP QUA RTMP (KHÔNG CẦN OBS)")
    print("=" * 70)

    stream_key = args.stream_key.strip()
    if not stream_key:
        print("\n❌ LỖI: Bạn chưa cung cấp Stream Key của TikTok Live!")
        print("👉 Cách lấy: Mở TikTok Live Studio hoặc ứng dụng TikTok -> Bắt đầu Live trên PC -> Sao chép URL Máy chủ và Khóa luồng (Stream Key).")
        print("👉 Cách chạy lệnh:")
        print("   python3 live_ngam_tiktok.py --stream-key YOUR_KEY_HERE --tiktok-username @YourUsername\n")
        sys.exit(1)

    stream_url = args.stream_url.rstrip('/')
    target_rtmp = f"{stream_url}/{stream_key}"
    w, h, fps = args.width, args.height, args.fps
    game_dir = os.path.dirname(os.path.abspath(__file__))

    check_and_install_dependencies()

    # Dọn dẹp tiến trình cũ
    print("🧹 [2/5] Dọn dẹp tiến trình cũ...")
    subprocess.run(["pkill", "-9", "-f", "Xvfb.*:99"], stderr=subprocess.DEVNULL)
    subprocess.run(["pkill", "-9", "-f", "server.js"], stderr=subprocess.DEVNULL)
    subprocess.run(["pkill", "-9", "-f", "chrome.*--window-size=1080"], stderr=subprocess.DEVNULL)
    subprocess.run(["pkill", "-9", "-f", "ffmpeg.*rtmp"], stderr=subprocess.DEVNULL)
    subprocess.run(["rm", "-f", "/tmp/.X99-lock", "/tmp/.X11-unix/X99"], stderr=subprocess.DEVNULL)
    time.sleep(1)

    # 1. Khởi tạo màn hình ảo Xvfb :99
    print(f"🖥️ [3/5] Khởi tạo màn hình ảo {w}x{h} (Display :99)...")
    xvfb_proc = subprocess.Popen(
        ["Xvfb", ":99", "-screen", "0", f"{w}x{h}x24", "-ac"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    time.sleep(2)

    # 2. Khởi chạy Server Node.js
    print("🚀 [4/5] Khởi chạy Server Game Node.js...")
    subprocess.run(["npm", "install", "--silent"], cwd=game_dir, check=True)
    server_env = os.environ.copy()
    server_env["PORT"] = "3000"
    if args.tiktok_username:
        server_env["TIKTOK_USERNAME"] = args.tiktok_username

    server_log = open("/tmp/live_server.log", "w")
    server_proc = subprocess.Popen(
        ["node", "server.js"],
        cwd=game_dir,
        env=server_env,
        stdout=server_log,
        stderr=subprocess.STDOUT
    )
    time.sleep(3)

    # 3. Khởi chạy Google Chrome trên màn hình ảo
    chrome_bin = find_chrome()
    chrome_flags = [
        chrome_bin,
        f"--window-size={w},{h}",
        "--window-position=0,0",
        "--kiosk",
        "--no-sandbox",
        "--disable-gpu",
        "--disable-dev-shm-usage",
        "--autoplay-policy=no-user-gesture-required",
        "http://localhost:3000/index.html"
    ]
    env_display = os.environ.copy()
    env_display["DISPLAY"] = ":99"
    chrome_proc = subprocess.Popen(chrome_flags, env=env_display, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(4)

    # 4. Bắt đầu đẩy luồng RTMP bằng FFmpeg
    print("📡 [5/5] Đang đẩy luồng video trực tiếp lên TikTok Live qua RTMP...")
    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-f", "x11grab",
        "-video_size", f"{w}x{h}",
        "-framerate", str(fps),
        "-i", ":99.0",
        "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-b:v", "3000k",
        "-maxrate", "3500k",
        "-bufsize", "6000k",
        "-pix_fmt", "yuv420p",
        "-g", str(fps * 2),
        "-c:a", "aac",
        "-b:a", "128k",
        "-ar", "44100",
        "-f", "flv",
        target_rtmp
    ]

    print("=" * 70)
    print("🔥 STREAM ĐANG HOẠT ĐỘNG! BẠN ĐÃ CÓ THỂ TẮT MÁY TÍNH / RẢNH TAY.")
    print("=" * 70)

    try:
        ffmpeg_proc = subprocess.Popen(ffmpeg_cmd)
        ffmpeg_proc.wait()
    except KeyboardInterrupt:
        print("\n🛑 Đang ngắt kết nối Live...")
    finally:
        for p in [chrome_proc, server_proc, xvfb_proc]:
            try:
                p.terminate()
            except Exception:
                pass

if __name__ == "__main__":
    main()
