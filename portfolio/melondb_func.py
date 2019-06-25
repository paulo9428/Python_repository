import pymysql
import requests
from bs4 import BeautifulSoup



def get_conn(db):
    return pymysql.connect(
        host='35.200.103.240',
        user='root',
        password='dl014532.',
        port=3306,
        db=db,
        charset='utf8')



def request_soup():    
    
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }

    source_url = "http://vlg.berryservice.net:8099/melon/list"

    html = requests.get(source_url, headers = headers)
    soup = BeautifulSoup(html.text, 'html.parser')

    return soup

def save_data(sql_insert, lst):

    try:
        conn = get_conn('melondb')
        conn.autocommit = False
        cur = conn.cursor()
        cur.executemany(sql_insert, lst)
        conn.commit()
        
    except Exception as err:
        conn.rollback()
        print("Error!!", err)

    finally:
        try:
            cur.close()
        except Exception as err2:
            print("Fail to close cursor!!", err2)
        try:
            conn.close()
        except Exception as err3:
            print("Fail to connect!!", err3)

