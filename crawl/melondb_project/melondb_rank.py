import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import pymysql
import melondb_func as mf
from datetime import datetime

soup = mf.request_soup()
headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }


def get_rank_data():
    
    trs = soup.select('div#tb_list table tbody tr[data-song-no]')
    
   
    # date = soup.select_one('#real_conts > div.multi_row > div.calendar_prid > span.yyyymmdd > span').text
    # time = soup.select_one('#real_conts > div.multi_row > div.calendar_prid > span.hhmm > span').text

    now = datetime.now()
    date = now.strftime('%Y-%m-%d')

    
    dic = {}   # { song_no: {title:'...', singer: '...' } }

    for tr in trs:
        song_no = tr.attrs['data-song-no']
        ranking = tr.select_one('span.rank').text
        
        
        dic[song_no] = {'ranking': int(ranking), 'rank_dt' : date}

    # pprint(dic[song_no])
    

    
    likeUrl = "https://www.melon.com/commonlike/getSongLike.json"          ### json 파일 구조 안에서 좋아요 수를 추출
    
    likeParams = {
        "contsIds": ",".join(dic.keys())
    }
    

    resLikecnt = requests.get(likeUrl, headers=headers, params=likeParams)
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

    for j in dic:
        SongRank_insert_list.append([j[0], j[1]['ranking'], j[1]['rank_dt'], j[1]['likecnt']])

    return SongRank_insert_list
            




    
    


