import requests, re
from time import sleep
import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
import random
from pystyle import *
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#đánh dấu bản quyền
thanh_xau=trang+'~'+red+'['+vang+'⟨⟩'+red+'] '+trang+'➩ '+luc
thanh_dep=trang+'~'+red+'['+luc+'✓'+red+'] '+trang+'➩ '+luc
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

# =======================[ NHẬP KEY ]=======================
os.system("cls" if os.name == "nt" else "clear")
print(banner)
import json,requests,time
from time import strftime

dem = 0
def check_live(cookie):
	headers = {
		'authority': 'mbasic.facebook.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3,gom;q=0.2,und;q=0.1',
		'cache-control': 'max-age=0',
	    'cookie': cookie,
		'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-ch-ua-platform-version': '"0.1.0"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
	}

	try:
		user_id = cookie.split('c_user=')[1].split(';')[0]
		name = requests.get(f'https://mbasic.facebook.com/profile.php?id={user_id}', headers = headers).text.split(f'<title>')[1].split(f'<')[0]
		return f'\033[1;31m─────────────────────────────────────────────────\n\033[1;36mFacebook: {name} | UserID: {user_id}\n\033[1;31m─────────────────────────────────────────────────'
	except:
		return False

cookie = input(f'\033[1;31m[\033[1;37m=.=\033[1;31m] {xnhac}Nhập Cookie Facebook : ')

if check_live(cookie) == False:
	exit(f'\033[1;34mCookie Facebook Die Hoặc Bị Văng !!')
else:
	print(check_live(cookie))
headers = {
	'authority': 'mbasic.facebook.com',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3,gom;q=0.2,und;q=0.1',
	'cache-control': 'max-age=0',
	'cookie': cookie,
	'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Windows"',
	'sec-ch-ua-platform-version': '"0.1.0"',
	'sec-fetch-dest': 'document',
	'sec-fetch-mode': 'navigate',
	'sec-fetch-site': 'same-origin',
	'sec-fetch-user': '?1',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

while True:
	access = requests.get(f'https://mbasic.facebook.com/friends/center/suggestions/', headers = headers).text
	find = re.findall(f'\/a\/friends\/add\/\?encrypted_id\=.*?"', access)
	for add in find:
		
		dem = dem + 1
		add = add.replace(f'amp;', '').replace(f'"', '')
		id = add.split(f'subject_id=')[1].split(f'&')[0]
		name_ = requests.get(f'https://mbasic.facebook.com/profile.php?id={id}', headers = headers).text.split(f'<title>')[1].split(f'<')[0]
		requests.get(f'https://mbasic.facebook.com/'+add, headers = headers)
		print(f'\033[1;31m[\033[1;37m=.=\033[1;31m] {xnhac}[{dem}] \033[1;32mĐ𝙰𝙽𝙶 𝙺𝙴̂́𝚃 𝙱𝙰̣𝙽 𝚅𝙾̛́𝙸 \033[1;33m{name_} - {vang}[{xnhac}{id}{vang}] ')
		sleep(1)
