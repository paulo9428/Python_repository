import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import pymysql

def get_conn(db):
    return pymysql.connect(
        host='35.200.103.240',
        user='root',
        password='dl014532.',
        port=3306,
        db=db,
        charset='utf8')


url = "https://www.melon.com/chart/index.htm"

heads = {
    "Referer": "https: // www.melon.com/chart/index.htm",
    "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

res = requests.get(url, headers=heads)
html = res.text

soup = BeautifulSoup(html, "html.parser")
trs = soup.select('div#tb_list table tbody tr[data-song-no]')
# print(len(trs))
# print(trs[0])

date = soup.select_one('#real_conts > div.multi_row > div.calendar_prid > span.yyyymmdd > span')
time = soup.select_one('#real_conts > div.multi_row > div.calendar_prid > span.hhmm > span')

print(date, time)


dic = {}   # { song_no: {title:'...', singer: '...' } }

for tr in trs:
    song_no = tr.attrs['data-song-no']
    ranking = tr.select_one('span.rank').text
    # title = tr.select_one('div.ellipsis.rank01 a').text
    # singers = tr.select('div.ellipsis.rank02 a')
    # singers = tr.select('div.ellipsis.rank02 span a')
    # singer = ",".join([a.text for a in singers])
    # dic[song_no] = {'ranking': int(ranking), 'title':title, 'singer': singer}
    
    # dic[song_no] = {'ranking': int(ranking), 'rank_dt' : date + ' ' + time}

# pprint(dic[song_no])

likeUrl = "https://www.melon.com/commonlike/getSongLike.json"          ### json 파일 구조 안에서 좋아요 수를 추출
likeParams = {
    "contsIds": ",".join(dic.keys())
}

resLikecnt = requests.get(likeUrl, headers=heads, params=likeParams)
# print(resLikecnt.url)
jsonData = json.loads(resLikecnt.text)
# pprint(jsonData)
for j in jsonData['contsLike']:                             
    key = str(j['CONTSID'])           ## song_no 를 문자열화
    songDic = dic[key]
    songDic['likecnt'] = j['SUMMCNT']  ## json 문서 안의 j['SUMMCNT'] 좋아요수를 dic 안의 songDic value에

dic = sorted(dic.items(), key=lambda d: d[1]['ranking'])      ##dic.items(): key와 value가 함께 온다

# pprint(dic)

SongRank_insert_list = []