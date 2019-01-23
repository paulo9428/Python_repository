from bs4 import BeautifulSoup
import requests
import re
import pprint

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

for singer in singers:
    
    
    singer_no = singer.get("href")
    sn = re.compile('goArtistDetail\(\'(.*)\'.*')
    singer_no2 = re.findall(sn, singer_no)[0]
    
    
    # print(singer_no2)
    singer_no_lst.append(singer_no2)

    singer_name = singer.text
    # print(singer_name)
    singer_name_lst.append(singer_name)

print(singer_no_lst)
print(len(singer_no_lst))
print(singer_name_lst)
print(len(singer_name_lst))


label_name_lst = []

for i in singer_no_lst:
    html = requests.get('https://www.melon.com/artist/timeline.htm?artistId={}'.format(i), headers = headers)
    soup = BeautifulSoup(html.text, 'html.parser')

    # print(soup)
    
    labels = soup.select('#conts > div.wrap_dtl_atist > div > div.wrap_atist_info > dl.atist_info.clfix > dt, dd')

   
  
    

    for i, element in enumerate(labels):
        
        if labels[i].text == "소속사":
            #  print(labels[i+1].text)

            label_name_lst.append(labels[i+1].text)

        

print(label_name_lst)
print(len(label_name_lst))


    
    #conts > div.section_info > div > div.entry > div.meta > dl > dt:nth-child(7)