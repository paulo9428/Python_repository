import bigquery
import sys
client = bigquery.get_client(json_key_file='./bigquery.json', readonly=False)

DATABASE = "bqdb"
TABLE = "test"
if not client.check_table(DATABASE, TABLE):
    pri: 'albumid', 'type': 'string', 'description': 'album id'},
    ])nt("Create table {0}.{1}".format(DATABASE, TABLE), file=sys.stderr)

    client.create_table(DATABASE, TABLE, [
        {'name': 'songno', 'type': 'string', 'description': 'song id'},
        {'name': 'title', 'type': 'string', 'description': 'song title'},
        {'name': 'albumid', 'type': 'string', 'description': 'album id'},
    ])


#     [ { 
#     'songno': '111', 'title':..., 
#     'rec':  { 'id': 123, 'name': "abc1" }
#   } ]


ttt = [
    {'songno': '111', 'title': '홍1', 'albumid': '121212121', 'rec':  { 'id': 123, 'name': "abc1" } },
    # {'songno': '222', 'title': '홍2', 'albumid': '121212121'},
    # {'songno': '333', 'title': '홍3', 'albumid': '121212121'},
 ]
pushResult = client.push_rows(DATABASE, TABLE, ttt, insert_id_key='songno')
print("Pushed Result is", pushResult)