from bs4 import BeautifulSoup
import requests

url = 'https://www.melon.com/chart/index.htm'
lurl = "https://www.melon.com/commonlike/getSongLike.json"

headers = {"Referer": "https://www.melon.com/artist/timeline.htm?artistId=982316",
           'user-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

#tr[song_no]
rank_sel = '#lst50 > td:nth-of-type(2) > div > span.rank'    # 순위
rank_sel2 = '#lst100 > td:nth-child(2) > div > span.rank'

ranks = soup.select(rank_sel) + soup.select(rank_sel2)


for span in ranks:
    
    print(span.text + '위')
    
    


song_tit_sel = '#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a' #곡명
song_tit_sel2 = '#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a'

song_tit = soup.select(song_tit_sel) + soup.select(song_tit_sel2)

for a in song_tit:
    
    print(a.text)
    
   


singer_sel = '#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a' #가수
singer_sel2 = '#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank01 > a'

singer = soup.select(singer_sel) + soup.select(singer_sel2)

for a in singer:
    
    print(a.text)




    
    

# likecnt_sel = '#lst50 > td:nth-child(8) > div > button > span.cnt'
# like_num = soup.select(likecnt_sel)

# for span in like_num:
#     print(span.text)

















# for span in ranks:
#     print(span.text)


# if len(imgs) < 1:
#     exit()

# img = imgs[0]




# src = img.get('src')
# print("img>>", src)
# # write to file

# # 순위, 곡명, 가수, 좋아요 수

# '#lst50 > td:nth-child(2) > div > span.rank'  :순위

# '#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a'  :곡명

# '#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a'  :가수


# '#lst100 > td:nth-child(2) > div > span.rank'

# '#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a'

# '#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank01 > a'





# trs = soup.select('#lst50')

# print(trs)

# # trs = soup.select('tbody tr')

# for tr in trs:
#     a = tr.select('td:nth-of-type(2)')

#     print(a)