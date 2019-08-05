import requests
from bs4 import BeautifulSoup
import csv, codecs
import openpyxl
from PIL import Image

url = "https://www.melon.com/chart/index.htm"

heads = {
    "Referer": "https: // www.melon.com/chart/index.htm",
    "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

res = requests.get(url, headers=heads)
html = res.text

soup = BeautifulSoup(html, "html.parser")
trs = soup.select('div#tb_list table tbody tr[data-song-no]')

for i, tr in enumerate(trs):
    tr_img = tr.select_one('a.image_typeAll img')
    src = tr_img.attrs['src']
    
    # print("./image/{}.jpg".format((i + 1)))
    with open("./image/{}.jpg".format((i + 1)), "wb") as file:
        file.write(requests.get(src).content)













