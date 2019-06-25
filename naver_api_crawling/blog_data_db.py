import os
import sys
import urllib.request
import json
from pprint import pprint
import pymysql

client_id = "7u2Iu2IU18BGZQz8uekp"
client_secret = "OP5l6EaQPj"

encText = urllib.parse.quote("파이썬") 

url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=100&sort=date" # json 결과
request = urllib.request.Request(url)

request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request)
rescode = response.getcode()

#display = 100
# sort = 'date'
# query = 'title', 'link', 'bloggername', 'postdate'

def get_conn(db):
    return pymysql.connect(
        host='35.200.103.240',
        user='root',
        password='1234567',
        port=3306,
        db=db,
        charset='utf8')

    


if(rescode==200):

    response_body = response.read()
    a = response_body.decode('utf-8')
    # print(a)
    
    json_Data = json.loads(a, encoding='utf-8')
    # pprint(json_Data)
    
    
else:
    print("Error Code:" + rescode)

blogger_insert_lst = []
blogpost_insert_lst = []
sql_blogger_insert = "insert into Blogger(blogger_id, blog_name, blogger_link) values(%s,%s,%s)"
sql_blogpost_insert = "insert into BlogPost(title, title_link, blogger, post_date) values(%s,%s,%s,%s)"


for j in json_Data['items']:
    blogger_insert_lst.append([j['bloggerlink'][22:], j['bloggername'], j['bloggerlink']])
    blogpost_insert_lst.append([j['title'], j['link'], j['bloggerlink'][22:], j['postdate']])

# pprint(blogger_insert_lst)
# pprint(blogpost_insert_lst)

        

conn = get_conn('melondb')
    
with conn:
    cur = conn.cursor()
    cur.executemany(blogger_insert_lst, sql_blogger_insert)
    cur.executemany(blogpost_insert_lst, sql_blogpost_insert)




    



