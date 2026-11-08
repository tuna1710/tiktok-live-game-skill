# -*- coding: utf-8 -*-
"""
Colab Runner Mode A: Web OBS Streaming via Cloudflare Tunnel
Chạy game TikTok Live "Rung Chuông Vàng" trên Google Colab và tạo đường link HTTPS công khai để dán vào OBS Browser Source.
"""
import os
import sys
import time
import subprocess
import urllib.request
import re

print("=" * 70)
print("🚀 KHỞI ĐỘNG GAME: ĐẤU TRÍ TRẠNG NGUYÊN TIKTOK LIVE (MODE A: OBS WEB SOURCE)")
print("=" * 70)

GAME_DIR = os.path.dirname(os.path.abspath(__file__))
PORT = os.environ.get("PORT", "3000")
TIKTOK_USERNAME = os.environ.get("TIKTOK_USERNAME", "")

# 1. Tải và cài đặt Cloudflare Tunnel nếu chưa có
cloudflared_bin = "/usr/local/bin/cloudflared"
if not os.path.exists(cloudflared_bin):
    print("📥 Đang tải Cloudflare Tunnel...")
    url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64"
    urllib.request.urlretrieve(url, "/tmp/cloudflared")
    os.chmod("/tmp/cloudflared", 0o755)
    subprocess.run(["mv", "/tmp/cloudflared", cloudflared_bin])

# 2. Cài đặt npm dependencies
print("📦 Đang kiểm tra thư viện Node.js...")
subprocess.run(["npm", "install", "--silent"], cwd=GAME_DIR, check=True)

# 3. Dọn dẹp tiến trình cũ
subprocess.run(["pkill", "-9", "-f", "server.js"], stderr=subprocess.DEVNULL)
subprocess.run(["pkill", "-9", "-f", f"cloudflared.*{PORT}"], stderr=subprocess.DEVNULL)
time.sleep(1)

# 4. Khởi chạy Server Node.js
print(f"🚀 Đang khởi chạy Server Game trên cổng {PORT}...")
env = os.environ.copy()
env["PORT"] = PORT
if TIKTOK_USERNAME:
    env["TIKTOK_USERNAME"] = TIKTOK_USERNAME

server_log = open("/tmp/game_server.log", "w")
server_proc = subprocess.Popen(["node", "server.js"], cwd=GAME_DIR, env=env, stdout=server_log, stderr=subprocess.STDOUT)
time.sleep(3)

# 5. Khởi chạy Cloudflare Tunnel
print(f"🌐 Đang tạo đường dẫn HTTPS công khai cho cổng {PORT}...")
cf_log = open("/tmp/game_cloudflared.log", "w")
tunnel_proc = subprocess.Popen([cloudflared_bin, "tunnel", "--url", f"http://localhost:{PORT}"], stdout=cf_log, stderr=subprocess.STDOUT)

public_url = None
for _ in range(25):
    time.sleep(1)
    if os.path.exists("/tmp/game_cloudflared.log"):
        with open("/tmp/game_cloudflared.log", "r") as f:
            content = f.read()
            match = re.search(r'https://[a-zA-Z0-9-]+\.trycloudflare\.com', content)
            if match:
                public_url = match.group(0)
                break

if public_url:
    print("\n" + "=" * 70)
    print("✅ KHỞI CHẠY GAME RUNG CHUÔNG VÀNG THÀNH CÔNG!")
    print(f"👉 Link Màn hình Game cho OBS (Browser Source 1080x1920):")
    print(f"   {public_url}/index.html")
    print(f"👉 Link Bảng điều khiển giả lập (Admin Mock Panel):")
    print(f"   {public_url}/admin.html")
    print("=" * 70 + "\n")
    print("💡 Giữ nguyên tab Colab này để server tiếp tục chạy.")
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n🛑 Đang dừng Server...")
        server_proc.terminate()
        tunnel_proc.terminate()
else:
    print("❌ Không lấy được đường dẫn Cloudflare Tunnel. Vui lòng kiểm tra lại log tại /tmp/game_cloudflared.log")
