from bs4 import BeautifulSoup
import requests
import re
import pprint
import pymysql
import time
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

albums = soup.select('div.ellipsis.rank03 > a')

# print(albums)

album_no_lst = []
album_name_lst = []

dic = {}

for album in albums:
    
    
    album_no = album.get("href")
    sn = re.compile('goAlbumDetail\(\'(.*)\'.*')
    album_no2 = re.findall(sn, album_no)[0]
   #  print(album_no2)
    
    
    # print(album_no2)
    album_no_lst.append(album_no2)

    album_name = album.text
    # print(album_name)
    album_name_lst.append(album_name)

    dic[album_no2] = {'album_name': album_name}


    
# print(album_no_lst)
# print(len(album_no_lst))
# print(album_name_lst)
# print(len(album_name_lst))

# print(dic)

# publisher_name_lst = []

for i in album_no_lst:
   
 
    html = requests.get('http://vlg.berryservice.net:8099/melon/detail?albumId={}'.format(i), headers = headers)
    soup = BeautifulSoup(html.text, 'html.parser')

    # print(soup)
   
    publisher = soup.select('#conts > div.section_info > div > div.entry > div.meta > dl > dt, dd')

   #  print(publisher)




    for j, element in enumerate(publisher):

      
       if publisher[j].text == "발매사":


         # print(publisher[j+1].text)
         # publisher_name_lst.append(publisher[j+1].text)

         dic[i]['publisher'] = publisher[j+1].text



# print(dic)
          
# time.sleep(0.5)        

# print(publisher_name_lst)
# print(len(publisher_name_lst))

##---------------------------------------------------------------- 좋아요, 평점 구하기
for i in album_no_lst:

   likeUrl = "https://www.melon.com/commonlike/getAlbumLike.json?contsIds={}".format(i)
   rateUrl = "https://www.melon.com/album/albumGradeInfo.json?albumId={}".format(i)
   
   likeParams = {
    "contsIds": "i"
   }
   rateParams = {
    "albumId" : "i"
   }

   resLikecnt = requests.get(likeUrl, headers=headers, params=likeParams)
   resRating = requests.get(rateUrl, headers=headers, params=rateParams) 
   # print(resLikecnt.url)
   jsonData1 = json.loads(resLikecnt.text)
   jsonData2 = json.loads(resRating.text)
   # pprint(jsonData)
   dic[i]['likecnt'] = jsonData1['contsLike'][0]['CONTSID']
   dic[i]['rating'] = round(float(jsonData2["infoGrade"]['TOTAVRGSCORE']))


# print(dic)
# print(len(dic.keys()))
   
      

   # result = sorted(dic.items(), key=lambda d: d[1]['ranking'])

##----------------------------------------------------------------------


album_insert_lst = []

for i in album_no_lst:
   album_insert_lst.append([i, dic[i]['album_name'], dic[i]['publisher'], dic[i]['likecnt'], dic[i]['rating']])

# print(album_insert_lst)

conn = get_conn('melondb')
with conn:
    cur = conn.cursor()

    sql_insert = "insert ignore into Album(album_no, album_name, publisher, likecnt, rating) values(%s,%s,%s,%s,%s)"
    
  
    # pprint(SongRank_insert_list)
    cur.executemany(sql_insert, album_insert_lst)