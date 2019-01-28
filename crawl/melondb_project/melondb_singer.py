from bs4 import BeautifulSoup
import requests
import re
import pprint
import pymysql
import melondb_func as mf

soup = mf.request_soup()

def get_singers_data():

    singers = soup.select('div.ellipsis.rank02 > a')

    # print(singers)

    singer_no_lst = []
    singer_name_lst = []

    dic = {}

    for singer in singers:
    
        singer_no = singer.get("href")
        sn = re.compile('goArtistDetail\(\'(.*)\'.*')
        singer_no2 = re.findall(sn, singer_no)[0]
        
        
        # print(singer_no2)
        singer_no_lst.append(singer_no2)

        singer_name = singer.text
        # print(singer_name)
        # singer_name_lst.append(singer_name)


        dic[singer_no2] = {'singer_name': singer_name}

        
        singer_exist_lable_lst = []
        label_name_lst = []



    for i in singer_no_lst:
        html = requests.get('https://www.melon.com/artist/timeline.htm?artistId={}'.format(i), headers = headers)
        soup2 = BeautifulSoup(html.text, 'html.parser')

        # print(soup)
        
        labels = soup2.select('#conts > div.wrap_dtl_atist > div > div.wrap_atist_info > dl.atist_info.clfix > dt, dd')

    
        for j, element in enumerate(labels):
                
            if labels[j].text == "소속사":
            #  print(labels[i+1].text)

                label_name_lst.append(labels[j+1].text)
                singer_exist_lable_lst.append(i)

                
                
                dic[i]['label'] = labels[j+1].text



            # [i][singer_name][label] = labels[j+1].text

    singer_not_label = list(set(singer_no_lst).difference(singer_exist_lable_lst))


    singer_insert_lst_1= []
    singer_insert_lst_2= []

    for i in singer_exist_lable_lst:
        singer_insert_lst_1.append([i, dic[i]['singer_name'], dic[i]['label']])

    for j in singer_not_label:
        singer_insert_lst_2.append([j, dic[j]['singer_name']])

                
    singer_insert_list = singer_insert_lst_1 + singer_insert_lst_2

    return singer_insert_lst









    