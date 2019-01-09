from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/marketindex/exchangeList.nhn"
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')

u = soup.select("body > div > table > tbody > tr")

#print(u)

for i in range(1, len(u)+1):
    v = soup.select("body > div > table > tbody > tr:nth-child({})".format(i))
    u = v.get('td.tit')
    print(u)
    




# usd = ifr.select("body > div > table > tbody)
# print(usd)

# for i in len():


body > div > table > tbody > tr:nth-child(1) > td.tit

body > div > table > tbody > tr:nth-child(1) > td.sale

body > div > table > tbody > tr:nth-child(1) > td:nth-child(3)

body > div > table > tbody > tr:nth-child(1) > td:nth-child(4)

#frame_ex1

