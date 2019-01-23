import pymysql

def get_conn(db):
    return pymysql.connect(
        host='35.243.74.84',
        user='root',
        password='1234567',
        port=3306,
        db=db,
        charset='utf8')

sql_insert_rank = "insert into SongRank(song_no, rank, rank_date, likecnt) values(%s,%s,%s,%s)"
sql_insert_song = "insert into Song(song_no, title, singer_no, album_no) values(%s,%s,%s,%s)"
sql_insert_singer = "insert into Singer(singer_no, singer_name, label_name) values(%s,%s,%s)"
sql_insert_album = "insert into Album(album_no, album_name, ratings) values(%s,%s,%s)"

insert_rank_lst = []
insert_song_lst = []
insert_singer_lst = []
insert_album_lst = []


lst = []

conn = get_conn(melondb)
cur = conn.cursor()

cur.executemany(sql_insert, lst)

##---------------------------------------------------------------------------------------------------------

import requests                                                   
from bs4 import BeautifulSoup
from pprint import pprint
import json
import csv, codecs
import re

url = "https://www.melon.com/chart/index.htm"

headers = {
    "Referer": "https: // www.melon.com/chart/index.htm",
    "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

res = requests.get(url, headers=headers)
html = res.text

soup = BeautifulSoup(html, "html.parser")


##-----------------------------------------------------------------------------

from bs4 import BeautifulSoup
import requests
import re
import pprint

headers = {
   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

source_url = "https://www.melon.com/chart/index.htm"

html = requests.get(source_url, headers = headers)
soup = BeautifulSoup(html.text, 'html.parser')

singers = soup.select('div.ellipsis.rank02 > a')

# print(singers)

singer_no_lst = []
singer_name_lst = []

for singer in singers:
    
    
    singer_no = singer.get("href")
    sn = re.compile('goArtistDetail\(\'(.*)\'.*')
    singer_no2 = re.findall(sn, singer_no)[0]
    
    
    # print(singer_no2)
    singer_no_lst.append(singer_no2)

    singer_name = singer.text
    # print(singer_name)
    singer_name_lst.append(singer_name)

print(singer_no_lst)
print(len(singer_no_lst))
print(singer_name_lst)
print(len(singer_name_lst))


label_name_lst = []

for i in singer_no_lst:
    html = requests.get('https://www.melon.com/artist/timeline.htm?artistId={}'.format(i), headers = headers)
    soup = BeautifulSoup(html.text, 'html.parser')

    # print(soup)
    
    labels = soup.select('#conts > div.wrap_dtl_atist > div > div.wrap_atist_info > dl.atist_info.clfix > dt, dd')

   
    for i, element in enumerate(labels):
        
        if labels[i].text == "소속사":
            #  print(labels[i+1].text)

            label_name_lst.append(labels[i+1].text)

print(label_name_lst)
print(len(label_name_lst))


  
    



    














