from bs4 import BeautifulSoup
import requests

class Game:
    
    title = ""
    
    def __init__(self, tag):
        self.title = self.get_text(tag, 'a.title')
        self.comp = self.get_attr(tag, 'a.subtitle')

    def get_text(self, parent, selector):

        t = self.get_tag(parent_tag, selector)

    def get_attr(self, parent, selector, attr_name):

    def get_tag(self, parent, selector):
       

url = 

res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
card_list = soup.select('div.card-list')