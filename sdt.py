# -*- coding: utf-8 -*-
import time
import os
import random
import sys

# Hàm xóa màn hình console cho sạch sẽ
def clear_screen():
    # Dành cho Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Dành cho Mac và Linux
    else:
        _ = os.system('clear')

# Banner của bạn đã được tích hợp
def display_banner():
    banner_text = """
\033[1;33m ██████╗ ██╗  ██╗██████╗ ███████╗██╗   ██╗
\033[1;35m██╔════╝ ██║ ██╔╝██╔══██╗██╔════╝██║   ██║
\033[1;36m██║  ███╗█████╔╝ ██║  ██║█████╗  ██║   ██║
\033[1;37m██║   ██║██╔═██╗ ██║  ██║██╔══╝  ╚██╗ ██╔╝
\033[1;32m╚██████╔╝██║  ██╗██████╔╝███████╗ ╚████╔╝ 
\033[1;31m ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝  ╚═══╝  

\033[1;97mTool By: \033[1;32mGia Khang            \033[1;97mPhiên Bản: \033[1;32m5.0 (High-Speed)\

\033[97m════════════════════════════════════════════════
    """
    print(banner_text)

# Hiệu ứng loading giả
def loading_animation():
    print("\033[1;97m[\033[1;36m+\033[1;97m] \033[1;32mĐang kết nối tới máy chủ...", end="")
    sys.stdout.flush()
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
        sys.stdout.flush()
    print("\033[1;32m Kết nối thành công!\033[0m")
    time.sleep(0.5)
    
    sys.stdout.write("\033[1;97m[\033[1;36m+\033[1;97m] \033[1;32mĐang truy vấn dữ liệu ")
    for _ in range(15):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(random.uniform(0.05, 0.2))
    print("\033[1;32m Hoàn tất!\033[0m\n")
    time.sleep(1)

# Hàm nhận diện nhà mạng từ đầu số
def get_carrier(phone_number):
    prefix = phone_number[:3]
    carriers = {
        "Viettel": ["032", "033", "034", "035", "036", "037", "038", "039", "096", "097", "098"],
        "MobiFone": ["070", "079", "077", "076", "078", "090", "093"],
        "VinaPhone": ["083", "084", "085", "081", "082", "091", "094"],
        "Vietnamobile": ["092", "056", "058"],
        "Gmobile": ["099", "059"]
    }
    for carrier, prefixes in carriers.items():
        if prefix in prefixes:
            return carrier
    return "Không xác định"

# Hàm tạo thông tin giả
def generate_fake_data(phone_number):
    first_names = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Võ", "Phan", "Trương", "Bùi", "Đặng"]
    middle_names = ["Văn", "Thị", "Minh", "Hữu", "Gia", "Bảo"]
    last_names = ["An", "Bình", "Cường", "Dũng", "Hà", "Linh", "Khang", "Huy", "My", "Nam", "Phúc", "Quân"]
    
    streets = ["Lê Lợi", "Trần Hưng Đạo", "Nguyễn Huệ", "Quang Trung", "Hai Bà Trưng", "Lý Thường Kiệt"]
    districts = ["Quận 1", "Quận Ba Đình", "Quận Hải Châu", "Quận Ninh Kiều", "Quận Sơn Trà"]
    cities = ["TP. Hồ Chí Minh", "TP. Hà Nội", "TP. Đà Nẵng", "TP. Cần Thơ"]

    gender = random.choice(["Nam", "Nữ"])
    full_name = f"{random.choice(first_names)} {random.choice(middle_names)} {random.choice(last_names)}"
    dob = f"{random.randint(1, 28)}/{random.randint(1, 12)}/{random.randint(1980, 2003)}"
    address = f"{random.randint(1, 1000)} {random.choice(streets)}, {random.choice(districts)}, {random.choice(cities)}"
    carrier = get_carrier(phone_number)
    
    # Tạo chuỗi username giả từ tên
    username_part = full_name.lower().replace(" ", "")[:8]

    return {
        "Họ và tên": full_name,
        "Giới tính": gender,
        "Ngày sinh": dob,
        "Địa chỉ": address,
        "Nhà mạng": carrier,
        "Tình trạng": "\033[1;32mĐang hoạt động\033[0m",
        "Đăng ký": "Chính chủ",
        "Facebook": f"https://facebook.com/****{username_part}",
        "Zalo": "\033[1;32mĐã liên kết\033[0m",
        "Telegram": f"@{username_part}***"
    }

# Hàm chính chạy chương trình
def main():
    while True:
        clear_screen()
        display_banner()
        
        try:
            phone_input = input("\033[1;97m[\033[1;31m❣\033[1;97m] \033[1;96mNhập SĐT cần tra (nhập 'exit' để thoát): \033[1;92m")
            
            if phone_input.lower() == 'exit':
                print("\n\033[1;31mCảm ơn đã sử dụng tool của Gia Khang!\033[0m")
                break
            
            # Kiểm tra định dạng SĐT
            if not phone_input.isdigit() or len(phone_input) != 10 or not phone_input.startswith('0'):
                print("\n\033[1;31m[LỖI] Số điện thoại không hợp lệ! Vui lòng nhập SĐT 10 số bắt đầu bằng 0.\033[0m")
                time.sleep(2)
                continue
            
            print(f"\n\033[1;97m[\033[1;36m~\033[1;97m] \033[1;93mBắt đầu tra cứu cho số điện thoại: {phone_input}\033[0m")
            time.sleep(1)
            loading_animation()
            
            # Tạo và hiển thị thông tin giả
            fake_info = generate_fake_data(phone_input)
            
            print("\033[97m═════════[ \033[1;32mKẾT QUẢ TÌM THẤY\033[0m \033[97m]═════════\033[0m")
            for key, value in fake_info.items():
                print(f"\033[1;97m[\033[1;36m+\033[1;97m] \033[1;94m{key:<12}: \033[1;97m{value}\033[0m")
                time.sleep(0.1)
            print("\033[97m════════════════════════════════════════════════\033[0m")

            input("\n\033[1;97mNhấn Enter để tiếp tục tra cứu...\033[0m")

        except KeyboardInterrupt:
            print("\n\n\033[1;31mChương trình đã bị ngắt. Tạm biệt!\033[0m")
            break

# Điểm bắt đầu của chương trình
if __name__ == "__main__":
    main()
