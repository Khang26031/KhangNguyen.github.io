import os,sys,aiohttp,asyncio,datetime,time

# SETUP TOOL
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb = "\033[1;37m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
vua = "\033[1;31m\033[1m\033[1m[\033[1;37m\033[1m=.=\033[1;31m\033[1m\033[1m] \033[1;37m\033[1m=> \033[1;32m\033[1m"

def he():
    os.system('cls' if os.name == 'nt' else 'clear')
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
    for i in banner:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.00)

success = []
list_token = []

# API PHỤ
async def getid(session, link):
    async with session.post('https://id.traodoisub.com/api.php', data={"link": link}) as response:
        rq = await response.json()
        if 'success' in rq:
            return rq["id"]
        else:
            exit(f"{do}Link post sai!!! Vui lòng nhập lại")

async def get_token(session, token, cookie):
    params = {
        'access_token': token
    }
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'max-age=0',
        'cookie': cookie,
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    async with session.get('https://graph.facebook.com/me/accounts', params=params, headers=headers) as r:
        rq = await r.json()
        if 'data' in rq:
            return rq
        else:
            exit("Token Hoặc Cookie Sai! Vui lòng nhập lại")

# API SHARE
async def shareao(session, tk, ck, post):
    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        params = {
            'method': 'POST',
            'link': f'https://m.facebook.com/{post}',
            'published': '0',
            'access_token': tk
        }
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'max-age=0',
            'cookie': ck,
            'priority': 'u=0, i',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
        }
        async with session.post('https://graph.facebook.com/v12.0/me/feed', params=params, headers=headers) as response:
            json = await response.json()
            if 'id' in json:
                print(vua,luc,current_time,":",json['id'],": Thành Công :",len(success))
                success.append(json['id'])
            else:
                print(f"{vua}{do}{current_time}: Thất Bại :",len(success))
                break

async def main(link, cookie, token):
    he()
    async with aiohttp.ClientSession() as session:
        post = await getid(session, link)
        token_data = await get_token(session, token, cookie)
        for token in token_data["data"]:
            list_token.append(token["access_token"])
            print(token["access_token"])
        he()
        print(vua,luc,"Có tổng",len(list_token), "token chính và page pro5!")
        await asyncio.gather(*[shareao(session, tk, cookie, post) for tk in list_token])
        print(f"{vua}Đã xong tổng share thành công là:",len(success))

# RUN TOOL
if __name__ == "__main__":
    he()
    link = input(f"{vua}Nhập link bài viết: {vang}")
    cookie = input(f"{vua}Nhập cookie acc cầm token: {vang}")
    token = input(f"{vua}Nhập token acc cầm page: {vang}")
    asyncio.run(main(link, cookie, token))
