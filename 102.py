import requests
import os

# Định nghĩa màu sắc cho đầu ra
trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
vang = "\033[1;33m\033[1m"

hack = "\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> "
banner = f"""
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

def shorten_link(url):
    token = "59453dd758f1811e25bbd7ca15860e3a5695d5f61264b572384eadc6bd273e2c"
    api_url = f"https://yeumoney.com/QL_api.php?token={token}&format=text&url={url}"

    response = requests.get(api_url)

    if response.status_code == 200:
        return response.text  # Dữ liệu trả về là dạng text
    else:
        return "Error: " + str(response.status_code) + " - " + response.text

# Sử dụng tool
link = input(f"{hack}NHẬP LINK CẦN RÚT GỌN : {vang}")

# Rút gọn URL với API link4m.co
token_link1s = '6685a9375cd7941ad61c38f7'
response = requests.get(f'https://link4m.co/api-shorten/v2?api={token_link1s}&url={link}').json()

if response.get('status') == "error":
    print(f"Lỗi: {response.get('message')}")
else:
    shortened_link = response.get('shortenedUrl')
    print(f"{hack}{xanh_la}LINK RÚT GỌN CỦA BẠN LÀ: {vang}{shortened_link}")
