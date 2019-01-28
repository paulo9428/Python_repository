from bs4 import BeautifulSoup
import requests
import re
import pymysql
from time import sleep
from pprint import pprint
import melondb_func as mf

soup = mf.request_soup()

def get_song_data():

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

	return sss

		









