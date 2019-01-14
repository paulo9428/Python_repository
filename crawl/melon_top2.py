from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.melon.com/chart/index.htm'

headers = {"Referer": "https://www.melon.com/artist/timeline.htm?artistId=982316",
           'user-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')


dic = {}

song_no = tr.get('data-song-no')
# likecnt_sel = '#lst50 > td:nth-child(8) > div > button > span.cnt'
likecnt = button[data-song-no = song_no] > span.cnt

tempDic = {'id': song_no, 'rank':  , 'song_name': , 'singer_name': , 'likecnt': }

strJson = '{"Top100":[],"httpDomain":"http://www.melon.com","httpsDomain":"https://www.melon.com","staticDomain":"https://static.melon.co.kr"}'


a = json_loads(strJson, encoding = 'utf-8')

for :


dic{song_no} = tempDic


a['Top100'] 














# dic = {}

# # html 파싱 데이터
# for i in range(100):
#     song_no = i + 1
#     tempDic = {"CONTSID": song_no, "name": "name" + str(i + 1)}
#     dic[song_no] = tempDic


# print(dic)
# print("-------------------------------------")

# # json data
# strJson = '{"contsLike":[{"CONTSID":1,"LIKEYN":"N","SUMMCNT":11111},{"CONTSID":3,"LIKEYN":"N","SUMMCNT":70128},{"CONTSID":100,"LIKEYN":"N","SUMMCNT":100000},{"CONTSID":5,"LIKEYN":"N","SUMMCNT":22821},{"CONTSID":7,"LIKEYN":"N","SUMMCNT":70128},{"CONTSID":9,"LIKEYN":"N","SUMMCNT":63636}],"httpDomain":"http://www.melon.com","httpsDomain":"https://www.melon.com","staticDomain":"https://static.melon.co.kr"}'

# jsonData = json.loads(strJson)
# for j in jsonData['contsLike']:
#     print("jjj=", j)
#     k = j['CONTSID']
#     print(dic[k])
#     dic[k]['likecnt'] = j['SUMMCNT']
#     print()

# print("===============================")
# print(dic)