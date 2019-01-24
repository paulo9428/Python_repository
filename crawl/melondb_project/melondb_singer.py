
from bs4 import BeautifulSoup
import requests
import re
import pprint
import pymysql

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

dic = {}

for singer in singers:
    
    
    singer_no = singer.get("href")
    sn = re.compile('goArtistDetail\(\'(.*)\'.*')
    singer_no2 = re.findall(sn, singer_no)[0]
    
    
    # print(singer_no2)
    singer_no_lst.append(singer_no2)

    singer_name = singer.text
    # print(singer_name)
    # singer_name_lst.append(singer_name)


    dic[singer_no2] = {'singer_name': singer_name}

# print(singer_no_lst)
# print(len(singer_no_lst))
# print(singer_name_lst)
# print(len(singer_name_lst))

singer_exist_lable_lst = []
label_name_lst = []



# print(dic)
# print(singer_no_lst)

for i in singer_no_lst:
    html = requests.get('https://www.melon.com/artist/timeline.htm?artistId={}'.format(i), headers = headers)
    soup = BeautifulSoup(html.text, 'html.parser')

    # print(soup)
    
    labels = soup.select('#conts > div.wrap_dtl_atist > div > div.wrap_atist_info > dl.atist_info.clfix > dt, dd')

   
  
    

    for j, element in enumerate(labels):
        
        if labels[j].text == "소속사":
            #  print(labels[i+1].text)

            label_name_lst.append(labels[j+1].text)
            singer_exist_lable_lst.append(i)

            
            
            dic[i]['label'] = labels[j+1].text



            # [i][singer_name][label] = labels[j+1].text

singer_not_label = list(set(singer_no_lst).difference(singer_exist_lable_lst))





# listA = ["a","b"]
# listB = ["b", "c"]
# listC = list(set(listB).difference(listA))
# print listC




            

# print(label_name_lst)
# print(len(label_name_lst))

# print(dic)

print(dic)
print(dic.keys())

singer_insert_lst_1= []
singer_insert_lst_2= []

for i in singer_exist_lable_lst:
    singer_insert_lst_1.append([i, dic[i]['singer_name'], dic[i]['label']])

for j in singer_not_label:
    singer_insert_lst_2.append([j, dic[j]['singer_name']])




def get_conn(db):
    return pymysql.connect(
        host='35.200.103.240',
        user='root',
        password='dl014532.',
        port=3306,
        db=db,
        charset='utf8')


conn = get_conn('melondb')
with conn:
    cur = conn.cursor()

    sql_insert1 = "insert ignore into Singer(singer_no, singer_name, label) values(%s,%s,%s)"
    sql_insert2 = "insert ignore into Singer(singer_no, singer_name) values(%s,%s)"
    
    
    # pprint(SongRank_insert_list)
    cur.executemany(sql_insert1, singer_insert_lst_1)
    cur.executemany(sql_insert2, singer_insert_lst_2)





