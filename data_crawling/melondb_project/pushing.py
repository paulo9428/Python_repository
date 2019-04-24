from bs4 import BeautifulSoup
import requests
import re
import pymysql
from time import sleep
from pprint import pprint
import json

def get_conn(db):
    return pymysql.connect(
        host='35.200.103.240',
        user='root',
        password='dl014532.',
        port=3306,
        db=db,
        charset='utf8')


headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }

source_url = "http://vlg.berryservice.net:8099/melon/list"

html = requests.get(source_url, headers = headers)
soup = BeautifulSoup(html.text, 'html.parser')


trs = soup.select('div#tb_list table tbody tr[data-song-no]')
Song = {}

for tr in trs:
    song_no = tr.attrs['data-song-no']                     ## 곡 번호
    # title = tr.select_one('div.ellipsis.rank01 a').text    ## 곡 제목
    
    singers = tr.select('div.ellipsis.rank02 span a')
    # singer_group = ",".join([a.text for a in singers])    ## 가수 묶음
    
    for singer in singers:
        
        singer_no_lst = []
        singer_name_lst = []
        
        singer_no = singer.get("href")
        sn = re.compile('goArtistDetail\(\'(.*)\'.*')
        singer_no2 = re.findall(sn, singer_no)[0]          ## 가수 번호(여러명 리스트에 추가)
        singer_no_lst.append(singer_no2)
        
        # singer_name = singer.text                          ## 가수 이름(여러명 리스트에 추가)
        # singer_name_lst.append(singer_name)
        
        
    
    Song[song_no] = {'singer_group': singer_no_lst}

pprint(Song)


songsing_insert_lst = []
sql_songsing_insert = "insert into SongSingMap(song, sing) values(%s,%s)"


for k in Song.keys():
    for i in (Song[k]['singer_group']):
        songsing_insert_lst.append([k, i])





try:
    conn = get_conn('melondb')
    conn.autocommit = False
    cur = conn.cursor()
    cur.executemany(sql_songsing_insert, songsing_insert_lst)
    conn.commit()
    
except Exception as err:
    conn.rollback()
    print("Error!!", err)

finally:
    try:
        cur.close()
    except Exception as err2:
        print("Fail to close cursor!!", err2)
    try:
        conn.close()
    except Exception as err3:
        print("Fail to connect!!", err3)


