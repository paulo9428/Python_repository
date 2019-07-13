
# for i in ['A', 'B', 'C']
# dic['COMPANY']['{} Incorp'.format(i)] = 


# def func2(a, **kargs):
#     args['b'] = 50         # => **kargs는 딕셔너리 형으로 전달 되므로 값 변경 가능
#     print( {a : args} )

# func2( 'A Incorp', place='서울', people_count=30, phone_number='02-2345-2323', email='a@a.com')      # 10 {'b': 50, 'c': 30}


from bs4 import BeautifulSoup

html = '''
<table>
    <tr>
        <th>회사</th>                  
        <th>A사</th>
        <th>B사</th>
        <th>C사</th>
    </tr>
    <tr>
        <th>주소</th>
        <td>서울</td>
        <td>강원도</td>
        <td>부산</td>
    </tr>
    <tr>
        <th>직원수</th>
        <td>30명</td>
        <td>55명</td>
        <td>200명</td>
    </tr>
    <tr>
        <th>전화번호</th>
        <td>02-2345-2323</td>
        <td>033-223-2323</td>
        <td>051-121-1212</td>
    </tr>
    <tr>
        <th>대표메일</th>
        <td>a@a.com</td>
        <td>b@b.com</td>
        <td>c@c.com</td>
    </tr>
</table>
'''


soup = BeautifulSoup(html, 'html.parser')
trs = soup.select('table tr')
# trd = soup.select('table tr td')

for tr in trs:
    head = tr.select('th')           ##### th 는 json의  key 값
    d = tr.select('td')
    
    


# dic = 
# {'회사' : [{ 'A사' : { '주소': '서울' , '직원수': '30명' , '전화번호': '02-2345-2323' , '대표메일': 'a@a.com',  }},
# { 'B사' : {} },
# { 'C사' : {} }]}


# {'회사' : {'A사'}}
# { '주소': '서울' , '직원수': '30명' , '전화번호': '02-2345-2323' , '대표메일': 'a@a.com',  }



companies = {}
data = {}

for i, tr in enumerate(trs):      ###필요없는 태그 제끼기 위해 enumerate 사용
    if i == 0:
        for j, th in enumerate





















