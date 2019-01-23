import pymysql
import csv
import codecs

def get_conn(db):
    return pymysql.connect(
        host='localhost',
        user='dooo',
        password='dooo!',
        port=3306,
        db=db,
        charset='utf8')

# sql_truncate = "truncate table Meltop"    ## truncate 는 DDL 이라서 TRANSACTION 이 안먹음
sql_truncate = "delete from Meltop"
sql_insert = "insert into SongRank(song_no, rank, rank_date, likecnt, sing_no, album_no) values(%s,%s,%s,%s,%s,%s)"
isStart = True

def save(lst):                                        ## 여러 단계에서 에러를 내본다
    try:
        conn = get_conn('dadb')
        conn.autocommit = False
        cur = conn.cursor()

        global isStart
        if isStart:
            cur.execute(sql_truncate)
            isStart = False

       
        cur.executemany(sql_insert, lst)
        conn.commit()
        print("Affected RowCount is", cur.rowcount, "/", len(lst))

    except Exception as err:
        try:
            conn.rollback()
        except:
            print("Error!!", err)

    finally:
        try:
            cur.close()
        except:
            print("Error on close cursor")

        try:
            conn.close()
        except Exception as err2:
            print("Fail to connect!!", err2)


csvFile = codecs.open("../crawl/data/meltop100.csv", "r", "utf-8")
reader = csv.reader(csvFile, delimiter=',', quotechar='"')

lst = []
for i, row in enumerate(reader):
    
    lst.append([row[0] , row[1], row[2], row[3]])


print("00>>", lst[0])
print("11>>", lst[1])
del lst[0]
del lst[ len(lst) - 1 ]

save(lst)