import os
import requests


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

def get_urls_from_file(file_name):
    """Đọc các URL từ file."""
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            urls = [line.strip() for line in file if line.strip()]  # Lọc các dòng không rỗng
        return urls
    except Exception as e:
        print(f"{vua}{do}Lỗi khi đọc file: {e}")
        return []

def get_web_response(url):
    # Remove single quotes if present in URL
    url = url.replace("'", "")
    
    # Check if URL starts with 'https://'
    if not url.startswith("https://"):
        return f"{vua}{do}Error: URL không chứa https://\n{do}─────────────────────────────────────────────────", False
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text, True
        else:
            return f"{vua}{do}Error: {response.status_code}", False
    except Exception as e:
        return f"{vua}{do}An error occurred: {e}", False

def save_to_file(content, base_filename, index):
    # Create a file name with index
    file_name = f"{base_filename}{index}.py"
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)
        return f"{vua}Đã lưu phản hồi vào file:{vang} {file_name}\n\033[1;31m─────────────────────────────────────────────────"
    except Exception as e:
        return f"{vua}{do}Lỗi khi lưu vào file: {e}\n\033[1;31m─────────────────────────────────────────────────"

def main():
    try:
        base_filename = input(f"{vua}Nhập tên file cơ bản (mặc định: 'herlyscode'): {vang}") or 'herlyscode'
        choice = input(f"{vua}Chọn:\n{vua}1. Lấy tất cả link từ file\n{vua}2. Nhập tay\n{vua}Nhập lựa chọn của bạn: {vang}")
        
        if choice == '1':
            file_name = input(f"{vua}Nhập tên file chứa các URL:{vang} ")
            urls = get_urls_from_file(file_name)
            if not urls:
                return  # If there are no URLs, exit the function
        elif choice == '2':
            num_websites = int(input(f"{vua}Bạn muốn get phản hồi bao nhiêu web: {vang}"))
            urls = []
            for i in range(num_websites):
                url = input(f"{vua}{do}[{vang}{i + 1}{do}] {xanh_la}Nhập URL: {vang}")
                print('\033[1;31m─────────────────────────────────────────────────')
                urls.append(url)
        else:
            print(f"{do}Lựa chọn không hợp lệ.")
            return
        
    except ValueError:
        print(f"{vua}{do}Vui lòng nhập một số hợp lệ.")
        return

    for i, url in enumerate(urls):
        print(f"{vua}Đang lấy phản hồi từ {url}")
        response_content, success = get_web_response(url)
        if success:
            message = save_to_file(response_content, base_filename, i + 1)
            print(message)  # Display message when saved successfully
        else:
            print(response_content)  # Error message for invalid URL

if __name__ == "__main__":
    main()
