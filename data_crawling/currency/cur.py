from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/marketindex/exchangeList.nhn"
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')






trs = soup.select("body > div > table > tbody > tr")

for tr in trs:
    tds = tr.select("td")
    
    if(len(tds)) < 4:
        continue

    title = tds[0].text                        ###### .text -> element(tag) 를 없애준다
    rate = tds[1].text

    print("{},{}".format(title, rate))


# u = v.get('.tit')
# print(u)
    