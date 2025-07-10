# sdt.py (Phiên bản đã sửa lỗi)
# -*- coding: utf-8 -*-
import time
import os
import random
import sys

# --- HÀM SỬA LỖI ĐÃ ĐƯỢC THÊM VÀO ---
def clear_screen():
    # Dành cho Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Dành cho Mac và Linux
    else:
        _ = os.system('clear')

# --- CÁC THÀNH PHẦN CỦA TOOL ---
def display_banner():
    # (Giữ nguyên code banner của bạn)
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

def loading_animation():
    # (Giữ nguyên code loading_animation của bạn)
    print("\033[1;97m[\033[1;36m+\033[1;97m] \033[1;32mĐang truy vấn dữ liệu...")
    time.sleep(2)
    print("\033[1;32mHoàn tất!\033[0m\n")

# ... (Giữ nguyên các hàm khác như get_carrier, generate_fake_data) ...

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

def generate_fake_data(phone_number):
    # (Giữ nguyên code generate_fake_data của bạn)
    first_names = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh"]
    middle_names = ["Văn", "Thị", "Minh", "Hữu"]
    last_names = ["An", "Bình", "Cường", "Dũng", "Hà", "Linh"]
    full_name = f"{random.choice(first_names)} {random.choice(middle_names)} {random.choice(last_names)}"
    return { "Họ và tên": full_name, "Nhà mạng": get_carrier(phone_number) }

# --- HÀM CHÍNH CHẠY CHƯƠNG TRÌNH ---
def main():
    while True:
        clear_screen() # Lệnh này bây giờ sẽ hoạt động
        display_banner()
        
        try:
            phone_input = input("\033[1;97m[\033[1;31m❣\033[1;97m] \033[1;96mNhập SĐT cần tra (nhập 'exit' để thoát): \033[1;92m")
            if phone_input.lower() == 'exit':
                break
            
            # (Code xử lý input của bạn)
            loading_animation()
            fake_info = generate_fake_data(phone_input)
            print(f"\033[1;97m[\033[1;36m+\033[1;97m] \033[1;94mHọ và tên: \033[1;97m{fake_info['Họ và tên']}\033[0m")
            print(f"\033[1;97m[\033[1;36m+\033[1;97m] \033[1;94mNhà mạng: \033[1;97m{fake_info['Nhà mạng']}\033[0m")

            input("\n\033[1;97mNhấn Enter để tiếp tục tra cứu...\033[0m")

        except KeyboardInterrupt:
            print("\n\n\033[1;31mChương trình đã bị ngắt. Tạm biệt!\033[0m")
            break

# --- ĐIỂM BẮT ĐẦU CHƯƠNG TRÌNH ---
if __name__ == "__main__":
    main()

