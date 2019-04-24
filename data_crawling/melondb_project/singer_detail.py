from bs4 import BeautifulSoup

html = '''<dl class="info_02 clfix">
    <dt>국적</dt>
    <dd>대한민국</dd>

    <dt>활동유형</dt>
    <dd>여성, 솔로</dd>

    <dt>활동년대</dt>
    <dd>2010</dd>
    
    <dt>활동장르</dt>
    <dd>Dance, Ballad, Drama</dd>

    <dt>데뷔</dt>
    <dd class="debut_song">
        <span class="ellipsis">
            2016.05.05
            <span class="bar">
                TTT
            </span>
        </span>
    </dd>
    
    <dt>생일</dt>
    <dd>1996.02.09</dd>
</dl>'''

col_names = {'국적': 'nation', '활동유형': 'act_type', '활동연대': 'act_year', '활동장르': 'act_genre', '데뷔': 'debut', '생일': 'birth'}


soup = BeautifulSoup(html, 'html.parser')

dls = soup.select('dl')
dts = soup.select('dl dt')
dds = soup.select('dl dd')

# print(dts)
# print(dds)

for i, dl in enumerate(dls):
   
