import requests
from bs4 import BeautifulSoup
import csv, codecs
import openpyxl
from PIL import Image

book = openpyxl.Workbook()

sheet2 = book.create_sheet()
sheet2.title = "두번째 시트"
# sheet2['A1'] = datetime.datetime.now()
# sheet2['A2'] = datetime.date.today()


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


book.save("./output3.xlsx")