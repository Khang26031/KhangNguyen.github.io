import re
import os


trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam = '\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
vua = "\033[1;31m\033[1m\033[1m[\033[1;37m\033[1m=.=\033[1;31m\033[1m\033[1m] \033[1;37m\033[1m=> \033[1;32m\033[1m"


banner = """

\033[1;33m ██████╗ ██╗  ██╗██████╗ ███████╗██╗   ██╗
\033[1;35m██╔════╝ ██║ ██╔╝██╔══██╗██╔════╝██║   ██║
\033[1;36m██║  ███╗█████╔╝ ██║  ██║█████╗  ██║   ██║
\033[1;37m██║   ██║██╔═██╗ ██║  ██║██╔══╝  ╚██╗ ██╔╝
\033[1;32m╚██████╔╝██║  ██╗██████╔╝███████╗ ╚████╔╝ 
\033[1;31m ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝  ╚═══╝  

\033[1;97mTool By: \033[1;32mGia Khang            \033[1;97mPhiên Bản: \033[1;32m4.0\


════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m☞ \033[1;36mKhang Dev - Kiếm Tiền Online \033[1;31m♔ \033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;97m☞\033[1;31m0\033[1;37m3\033[1;36m4\033[1;35m9\033[1;34m2\033[1;33m5\033[1;33m5\033[1;34m8\033[1;35m6\033[1;37m4☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Facebook\033[1;31m : \033[1;97mKhang.Develop
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;97m☞\033[1;32mhttps://t.me/Boo_Khang🔫\033[1;97m☜
\033[97m════════════════════════════════════════════════

"""

os.system('cls' if os.name == 'nt' else 'clear')
print(banner)

def extract_links_from_file(input_file, output_file):
    # Kiểm tra xem file đầu vào có tồn tại không
    if not os.path.exists(input_file):
        print(f"{vua}{do}File '{input_file}' không tồn tại.")
        return
    
    # Mở file đầu vào để đọc
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = f.read()
    except Exception as e:
        print(f"{vua}{do}Không thể mở file '{input_file}':{vang} {e}")
        return
    
    # Biểu thức chính quy để tìm các URL
    url_pattern = re.compile(r'(https?://[^\s]+)')
    
    # Tìm tất cả các liên kết
    links = url_pattern.findall(data)
    
    # Mở file đầu ra để ghi
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for link in links:
                link = link.replace("'", "")  # Loại bỏ dấu nháy đơn
                f.write(link + '\n')
        print(f"{vua}Các liên kết đã được lưu vào '{output_file}'.")
    except Exception as e:
        print(f"{vua}{do}Không thể ghi vào file '{output_file}': {e}")

# Ví dụ cách sử dụng
input_file = input(f'{vua}Nhập File Cần Get Link: {vang}')  # Đường dẫn tới file chứa dữ liệu
output_file = input(f'{vua}Nhập Tên File Lưu: {vang}')  # File để lưu các liên kết đã lọc
extract_links_from_file(input_file, output_file)
