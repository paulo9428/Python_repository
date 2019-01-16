from bs4 import BeautifulSoup
import requests
import urls

url = 'http://www.jobkorea.co.kr/Recruit/GI_Read_Comt_Ifrm?Gno=27394825&blnKeepInLink=0&rPageCode=PL'  # 요기요 사이트 이미지 iframe

headers = {
    'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

# print(soup.prettify())

img_sel = '#container > div.detailHeader > p > img'
imgs = soup.select(img_sel)

print(imgs)


if len(imgs) < 1:
    exit()

print("--------------------------------------")
for img in imgs:
    src = img.get('src')
    print("img>>", src)
    with open("./image" + urls.getFilename(src), "wb") as file:
        file.write(requests.get(src).content)


    
