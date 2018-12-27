from bs4 import BeautifulSoup
import requests

url = 
res =  requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
card_list = soup.select('div.card-list')

print(">>>>>", )