from bs4 import BeautifulSoup
import requests
import makeurl
import time
import random
import datetime

now = datetime.datetime.now()
page_num = 0
url2 = []
savename = "crawl_site.csv"

url_lst = []
with open(savename, mode = 'r', encoding = 'utf-8') as crawl_site:
    for line in crawl_site:
        url_lst.append(line.split(',')[1])

b = len(url_lst) + 1

with open(savename, mode="r", encoding="utf-8") as file:
    for h in range(0,20):
        page_num = h + 1

        url = "http://www.jobkorea.co.kr/Recruit/Home/_GI_List/"

        params = {
            'isDefault': 'true',
            'duty': '1000100,1000101,1000102,1000096,1000097',
            'menucode':'',
            'page': str(page_num),
            'pagesize': '50',
            'direct': '0',
            'order': '2',
            'tabindex': '0',
            'fulltime': '0',
            'confirm': '0'
        }
        headers = {
            'Host': 'www.jobkorea.co.kr',
            'Origin' : 'http://www.jobkorea.co.kr',
            'Referer': 'http://www.jobkorea.co.kr/recruit/joblist?menucode=duty',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

        html = requests.post(url, params=params, headers = headers).text

        soup = BeautifulSoup(html, 'html.parser')

        sel_comptitle = "div.tplList div.titBx a"
        sel_compname = "div.tplList td.tplCo "    

        get_url = soup.select(sel_comptitle)
        get_name = soup.select(sel_compname)

        company_name = []
        d = 0
    
        for j in get_name :
            comp = j.select_one('a').text
            company_name.append(comp)

        for i in get_url :
            a = i.get('href')
            c = ("http://www.jobkorea.co.kr" + a )
            
            if c not in url_lst:
                with open(savename, mode="a", encoding="utf-8") as file2:
                    file2.write("{},{},{},{},{}".format(b, c, company_name[d], now.strftime('%Y-%m-%d %H:%M:%S'), "\n"))
                    b = b + 1
                    d = d + 1