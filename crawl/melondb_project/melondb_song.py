from bs4 import BeautifulSoup
import requests
import re

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

source_url = "http://vlg.berryservice.net:8099/melon/list"

html = requests.get(source_url, headers = headers)
trs = soup.select('div#tb_list table tbody tr[data-song-no]')
for tr in trs:
	song_no = tr.attrs['data-song-no']
	title = tr.select_one('div.ellipsis.rank01 a').text
	Song[song_no] = {'song_no': song_no, 'title':title, 'singer': singer_name}

sss = []

for so in Song.keys():
	sss.append([int(so), Song[so]['title']])


genre = []

for s in song_id:
	# surl ="https://www.melon.com/song/detail.htm?songId={}".format(s)
	surl = "http://vlg.berryservice.net:8099/melon/songdetail?songId={}".format(s)
	shtml = requests.get(surl, headers = headers)
	ssoup = BeautifulSoup(shtml.text, 'html.parser')
	g = ssoup.select_one("#downloadfrm > div > div > div.entry > div.meta > dl > dd:nth-of-type(3)").text
	genre.append(g)