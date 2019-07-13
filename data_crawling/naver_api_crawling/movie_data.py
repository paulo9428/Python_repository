import os
import sys
import urllib.request
import json
from pprint import pprint
import pymysql
from pymongo import MongoClient, DESCENDING

client_id = "7u2Iu2IU18BGZQz8uekp"
client_secret = "OP5l6EaQPj"

encText = urllib.parse.quote("사랑") 

url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText + "&display=100&sort=date" # json 결과
request = urllib.request.Request(url)

request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request)
rescode = response.getcode()

#display = 100
# sort = 'date'
# query = 'title', 'link', 'bloggername', 'postdate'

if(rescode==200):
    response_body = response.read()
    a = response_body.decode('utf-8')
    # print(a)
    
    json_Data = json.loads(a, encoding='utf-8')
    pprint(json_Data)
else:
    print("Error Code:" + rescode)


# ----------------------------------------------------------- push into mongodb

mongo_client = MongoClient('localhost', 27017)

melondb = mongo_client.get_database('melondb')
books = melondb.get_collection('Book')


for j in json_Data:

    books.insert_one(j)










