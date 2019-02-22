import bigquery
import sys
import pymysql
from pprint import pprint
from google.cloud import bigquery


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



client = bigquery.Client()

# Perform a query.
QUERY = ('select * from `delta-transit-221316.bqdb.songs`')
query_job = client.query(QUERY)  # API request
rows = query_job.result()        # Waits for query to finish

for row in rows:
    print(row)



















































# insert_dic = {}
# insert_lst = []

# with conn:                                                            
#     # cursor를 만들어줍니다
#     cur = conn.cursor()

#     cur.execute("SELECT * FROM Song ORDER BY song_no")
    
#     s_rows = cur.fetchall()


#     for row in s_rows:
#         # print(row['song_no'], row['title'], row['genre'], row['album_id'])
#         insert_dic['song_no'] = row['song_no']
#         insert_dic['title'] = row['title']
#         insert_dic['genre'] = row['genre']
#         insert_dic['album_id'] = row['album_id']

#         # print(insert_dic)

#         insert_ttt_s = [insert_dic]
#         # print(insert_ttt_s)

#         pushResult = client.push_rows(DATABASE, TABLE, insert_ttt_s, insert_id_key='song_no')

#         # print("Pushed Result is", pushResult)

# insert_dic2 = {}    

# with conn:                                                                      ## song 의 album_id 랑 album 의 album_id 어떻게 매치시키나....
#                                                                                 ## foreign key 걸어준 다음에 추출하나??
#     cur2 = conn.cursor()

#     cur2.execute("SELECT * FROM Album order by album_id")
    
#     a_rows = cur2.fetchall()


#     for row in a_rows:
        
        
#         insert_dic2['album_id'] = {'album_id': row['album_id'], 'album_title': row['album_title'], 'album_genre': row['album_genre'], 'rating': row['rating']}
#         # print(insert_dic2)
        
#         # {row['album_id']: {'album_title': row['album_title'], 'album_genre': row['album_genre'], 'rating': row['rating']}}
#         if insert_d

#         insert_ttt_a = [insert_dic2] 
        


#         pushResult = client.push_rows(DATABASE, TABLE, insert_ttt_a, insert_id_key='album_id')
#         print("Pushed Result is", pushResult)


# # cols = [c[0] for c in cur.description]
# # Song = namedtuple('Song', " ".join(cols))
# # dset = [Song(*r)._asdict() for r in rows]

# ##튜플에 담은 다음에 리스트에 append 해준다?

# ##제이슨 하나하나 바로 바로 bigquery 에 들어간다?


