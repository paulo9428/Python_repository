import os
import sys
import urllib.request
import json

client_id = "7u2Iu2IU18BGZQz8uekp"
client_secret = "OP5l6EaQPj"

encText = urllib.parse.quote("파이썬") 

url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=100&sort=date" # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
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
    for j in json_Data['items']:
        print('{}-{}-{}-{}'.format(j['title'], j['link'], j['bloggername'], j['postdate']))

else:
    print("Error Code:" + rescode)


# curl  "https://openapi.naver.com/v1/search/blog.xml?query=%EB%A6%AC%EB%B7%B0&display=10&start=1&sort=sim"


    