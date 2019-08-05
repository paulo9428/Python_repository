import bigquery
import sys
import pymysql
from pprint import pprint
from google.cloud import bigquery as bq


client = bigquery.get_client(json_key_file='./bigquery.json', readonly=False)

DATABASE = "bqdb"
TABLE = "songs"

if not client.check_table(DATABASE, TABLE):
    print("Create table {0}.{1}".format(DATABASE, TABLE), file=sys.stderr)

    client.create_table(DATABASE, TABLE, [
        {'name': 'song_no', 'type': 'string', 'description': 'song id'},
        {'name': 'title', 'type': 'string', 'description': 'song title'},
        {'name': 'genre', 'type': 'string', 'description': 'genre name'},
        {'name': 'album_id', 'type':'record', 'description': 'album detail',
        'fields':  [ 
        { "name": "album_id", "type":"string"},
        { "name": "album_title", "type":"string"},
        { "name": "album_genre", "type":"string"},
        { "name": "rating", "type":"float"}
        ]
}
       ])


conn = pymysql.connect(
        host='35.243.74.84',
        user='root',
        password='1234567',
        port=3306,
        db='melondb',
        cursorclass=pymysql.cursors.DictCursor,
        charset='utf8')

insert_dic = {}

with conn:                                                            
    # cursor를 만들어줍니다
    cur = conn.cursor()

    cur.execute("select s.*, a.* from Song s inner join Album a on s.album_id = a.album_id")
    
    s_rows = cur.fetchall()


    for row in s_rows:
        # print(row['song_no'], row['title'], row['genre'], row['album_id'])
        # print(row)
        
        insert_dic['song_no'] = row['song_no']
        insert_dic['title'] = row['title']
        insert_dic['genre'] = row['genre']
        insert_dic['album_id'] = {'album_id': row['a.album_id'], 'album_title': row['album_title'], 'album_genre': row['album_genre'], 'rating': str(row['rating'])}


        # print(insert_dic)

        insert_ttt_s = [insert_dic]
        
      

        pushResult = client.push_rows(DATABASE, TABLE, insert_ttt_s, insert_id_key='song_no')
        print("Pushed Result is", pushResult)



client = bq.Client()

# Perform a query.
QUERY = ('select song_no, title, genre, album_id.album_title from `big-query-232802.bqdb.songs`')
query_job = client.query(QUERY)  # API request
rows = query_job.result()        # Waits for query to finish

for row in rows:
    print(row)






