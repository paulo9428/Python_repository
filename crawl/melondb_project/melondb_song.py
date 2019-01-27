from bs4 import BeautifulSoup
import requests
import re
import pymysql
from time import sleep
from pprint import pprint
import json


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}


# source_url = "https://www.melon.com/chart/index.htm"
source_url = "http://vlg.berryservice.net:8099/melon/list"

html = requests.get(source_url, headers = headers)
soup = BeautifulSoup(html.text, 'html.parser')

##----------------------------------------------------------------


trs = soup.select('div#tb_list table tbody tr[data-song-no]')

song_no_lst = []
Song = {}

for tr in trs:
	song_no = tr.attrs['data-song-no']
	title = tr.select_one('div.ellipsis.rank01 a').text

	song_no_lst.append(song_no)

	


	Song[song_no] = {'title':title}


for i in song_no_lst:
	# surl ="https://www.melon.com/song/detail.htm?songId={}".format(s)
	surl = "http://vlg.berryservice.net:8099/melon/songdetail?songId={}".format(i)
	shtml = requests.get(surl, headers = headers)
	ssoup = BeautifulSoup(shtml.text, 'html.parser')
	g = ssoup.select_one("#downloadfrm > div > div > div.entry > div.meta > dl > dd:nth-of-type(3)").text
	
	Song[i]['genre'] = g
	

sss = []

for so in Song.keys():
	sss.append([int(so), Song[so]['title'], Song[so]['genre']])

print(sss)



def get_conn(db):
    return pymysql.connect(
        host='35.200.103.240',
        user='root',
        password='dl014532.',
        port=3306,
        db=db,
        charset='utf8')


sql_insert = "insert ignore into Song(song_no, song_name, genre) values(%s,%s,%s)"


try:
	conn = get_conn('melondb')
	conn.autocommit = False
	cur = conn.cursor()
	cur.executemany(sql_insert, sss)
	conn.commit()
	
except Exception as err:
	conn.rollback()
	print("Error!!", err)

finally:
	try:
		conn.close()
	except Exception as err2:
		print("Fail to connect!!", err2)

##--------------------------------------------

