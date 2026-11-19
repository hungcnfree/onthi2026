import os
import re
import json
import random
import zipfile
import sys

def gen_rand_code(length=16):
    chars = "abcdefghijkmnpqrstuvwxyz23456789"
    return "".join(random.choice(chars) for _ in range(length))

def configure_firebase(workspace_dir, firebase_url="", teacher_code="", student_code=""):
    """
    Cấu hình Firebase Realtime Database cho hệ thống Đề thi tự học 2026:
    1. Chuẩn hóa URL Firebase (bỏ đuôi .json, dấu gạch chéo cuối).
    2. Tự sinh mã giáo viên t (24 ký tự) và mã học sinh p (16 ký tự) nếu chưa có.
    3. Ghi vào cloud-config.json.
    4. Cập nhật nhúng trực tiếp vào index.html (đảm bảo chạy cả online lẫn offline).
    5. Đóng gói lại tệp zip sẵn sàng phân phối.
    """
    index_html_path = os.path.join(workspace_dir, "index.html")
    cloud_config_path = os.path.join(workspace_dir, "cloud-config.json")
    rules_path = os.path.join(workspace_dir, "database.rules.json")
    zip_path = os.path.join(workspace_dir, "He_Thong_Day_Hoc_2026_Ban_Giao_Vien.zip")
    
    if not os.path.exists(index_html_path):
        print(f"[ERROR] Không tìm thấy file index.html tại {index_html_path}")
        return False
        
    # Chuẩn hóa URL
    u = firebase_url.strip().rstrip('/')
    if u and not u.startswith("http"):
        u = "https://" + u
    if u.endswith(".json"):
        u = u[:-5]
        
    t = teacher_code.strip() if teacher_code else gen_rand_code(24)
    p = student_code.strip() if student_code else gen_rand_code(16)
    
    print(f"--- THÔNG SỐ CẤU HÌNH FIREBASE ---")
    print(f"1. URL Database : {u if u else '(Chưa điền - để trống cho giáo viên tự nhập)'}")
    print(f"2. Mã Giáo viên : {t} (24 ký tự bảo mật)")
    print(f"3. Mã Học sinh  : {p} (16 ký tự phân vùng)")
    
    # 1. Cập nhật cloud-config.json
    cfg = {
        "u": u,
        "p": p,
        "note": "Đặt tệp này cùng thư mục với index.html trên GitHub. Mọi máy học sinh/giáo viên mở trang sẽ tự nhận đúng kho dữ liệu này."
    }
    with open(cloud_config_path, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)
    print(f"[OK] Đã ghi cấu hình vào: {cloud_config_path}")
    
    # 2. Cập nhật index.html nhúng APP_CONFIG
    with open(index_html_path, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()
        
    app_config_replacement = f'<script id="app-config">window.APP_CONFIG = {{ firebaseUrl: \'{u}\', studentCode: \'{p}\', token: \'\' }};</script>'
    html = re.sub(
        r'<script id="app-config">.*?</script>',
        app_config_replacement,
        html,
        count=1
    )
    
    with open(index_html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] Đã nhúng APP_CONFIG vào: {index_html_path}")
    
    # 3. Tạo database.rules.json nếu chưa có
    rules_content = '''{
  "rules": {
    ".read": false,
    ".write": false,
    "t": {
      "$code": {
        ".read": "$code.length >= 16",
        ".write": "$code.length >= 16"
      }
    },
    "s": {
      "$code": {
        ".read": "$code.length >= 12",
        ".write": "$code.length >= 12"
      }
    }
  }
}
'''
    with open(rules_path, "w", encoding="utf-8") as f:
        f.write(rules_content)
    print(f"[OK] Đã tạo file Rules chuẩn: {rules_path}")
    
    # 4. Đóng gói lại ZIP phân phối
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(index_html_path, "index.html")
        zipf.write(cloud_config_path, "cloud-config.json")
        zipf.write(rules_path, "database.rules.json")
        nojekyll = os.path.join(workspace_dir, ".nojekyll")
        if os.path.exists(nojekyll):
            zipf.write(nojekyll, ".nojekyll")
        readme = os.path.join(workspace_dir, "README.md")
        if os.path.exists(readme):
            zipf.write(readme, "README.md")
            
    print(f"[DONE] Đã cập nhật và đóng gói lại tệp: {zip_path}")
    return True

if __name__ == "__main__":
    target_dir = r"E:\test mã nguồn\Ban_Phan_Phoi_Giao_Vien"
    url = sys.argv[1] if len(sys.argv) > 1 else ""
    configure_firebase(target_dir, firebase_url=url)
