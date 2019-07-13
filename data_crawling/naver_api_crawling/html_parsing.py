from bs4 import BeautifulSoup

html = '''
    <dl>
        <dt>국적</dt>
        <dd>대한민국</dd>

        <dt>활동장르</dt>
        <dd>Dance, Ballad, Drama</dd>
    
        <dt>데뷔</dt>
        <dd class="debut_song">
            <span class="ellipsis">
                2016.05.05
                <span class="bar">
                    TTT
                </span>
                <a href="#">TTTTTTTTTTTTT</a>
            </span>
        </dd>
        
        <dt>수상이력</dt>
        <dd class="awarded">
            <span class="ellipsis">
                2018 하이원 서울가요대상
                <span class="bar">|</span>본상
            </span>
        </dd>
    </dl>
'''

col_names = {'국적': 'nation', '활동장르': 'act_genre', '데뷔': 'debut', '수상이력': 'award'}

soup = BeautifulSoup(html, 'html.parser')

dl = soup.find('dl')
dts = []
dds = []

for d in dl:
    if not d.name: continue

    if d.name == 'dt':
        dts.append(d.text)
    else:                                   ## dd
        span = d.select_one('span')
        if span != None:
            dds.append(span.next.strip())
            
        else:
            dds.append(d.text)
            
            

print(dts)
print(dds)

col = []

for i in range(len(dts)):
    col.append(col_names[dts[i]])

print(col)


a = tuple(col)
b = tuple(dds)
# print(a,b)


sql_insert = 'insert into Singer{} values{};'.format(a, b)
print(sql_insert)





