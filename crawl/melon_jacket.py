import requests
from bs4 import BeautifulSoup
import csv, codecs
import urls
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




for i in range(1, 101):
    # insert image
    imgFile = 'C:\workspace\Learn_Python\crawl\image\{}.jpg'.format(i)

    # img = openpyxl.drawing.image.Image(imgFile)
    # sheet2.add_image(img, 'B5')


    # resize image

    img2 = Image.open(imgFile)
    new_img = img2.resize((30, 30))
    new_img.save('new.png')
    img3 = openpyxl.drawing.image.Image('new.png')
    sheet2.add_image(img3, 'A{}'.format(i))









# ifrSel = "iframe#mainFrame"
# ifr = soup.select(ifrSel)

# print(ifr)

# # sel = "#SE-9311ee77-8bde-4b1f-9e02-7ea73e016f1f > div > div > a > img"
# sel = "img.se-image-resource"

# imgs = soup.select(sel)
# # print(imgs, len(imgs))

# if len(imgs) < 1:
#     exit()

# print("--------------------------------------")
# for img in imgs:
#     src = img.get('src')
#     print("img>>", src)
#     with open("./images/" + urls.getFilename(src), "wb") as file:
#         file.write(requests.get(src).content)
