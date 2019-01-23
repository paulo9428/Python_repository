from bs4 import BeautifulSoup
import requests
import re

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

source_url = "https://www.melon.com/chart/index.htm"

html = requests.get(source_url, headers = headers)
soup = BeautifulSoup(html.text, 'html.parser')

urls = soup.select('div[class=wrap] > a[href]')
# trs = soup.select('div#tb_list table tbody tr[data-song-no]')


song_id = []
album_id = []



def get_id(url, slist, alist):
	for u in urls:
		url = u.get('href')
		sp = re.compile('goSongDetail\(\'(.*)\'.*')
		ap = re.compile('goAlbumDetail\(\'(.*)\'.*')
		sid = re.findall(sp, url)
		aid = re.findall(ap, url)	
		slist += aid
		alist += sid
    

get_id(urls, song_id, album_id)



song_table = []

def song (table_name):
	for tr in trs:
		song_no = tr.attrs['data-song-no']
		ranking = tr.select_one('span.rank').text
		title = tr.select_one('div.ellipsis.rank01 a').text
		singers = tr.select('div.ellipsis.rank02 span a')
		singer = ",".join([a.text for a in singers])
		albums = tr.select('div.ellipsis.rank03 > a')
		for a in albums:
			album = a.text
		table_name.append([album, singer])
	print(table_name)

song(song_table)