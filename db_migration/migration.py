import mig_util as mu

conn_dooodb = mu.get_mysql_conn('dooodb')
conn_dadb = mu.get_mysql_conn('dadb')

# read from source db
with conn_dooodb:
    cur = conn_dooodb.cursor()
    sql = "select id, name, prof, classroom from Subject"

    cur.execute(sql)
    rows = cur.fetchall()

# write to target db
with conn_dadb:
    cur = conn_dadb.cursor()
    # cur.execute('truncate table Subject')
    trc = mu.trunc_table(conn_dadb, 'Subject')
    print("tuncated>>", trc)

    sql = '''insert into Subject(id, name, prof, classroom)
                          values(%s, %s, %s, %s)'''
    cur.executemany(sql, rows)
    print("AffectedRowCount is", cur.rowcount)
    conn_dadb.commit()

# ----------------------------------------------------    검증

conn_dooodb = mu.get_mysql_conn('dooodb')
conn_dadb = mu.get_mysql_conn('dadb')
table = 'Subject'
cols = "id, name, prof, classroom, classroom cr2"
rand_row_count = 0
# read from source db
with conn_dooodb:
    dooo_cnt = mu.get_count(conn_dooodb, table)

    cur = conn_dooodb.cursor()
    sql = "select " + cols + " from " + table + " order by rand() limit %s"
    rand_row_count = round(dooo_cnt / 3)                                       
    cur.execute(sql, (rand_row_count,))
    
    dooo_list = cur.fetchall()    

# lst = []
# for i in dooo_list:
#     l = list(i)
#     l.append(i[3])
#     lst.append(l)

# print("lst=", lst)

with conn_dadb:
    da_cnt = mu.get_count(conn_dadb, table)

    print("dooodb =", dooo_cnt, ", dadb =", da_cnt)
    if dooo_cnt != da_cnt:
        print("Not Valid Count!! dooodb =", dooo_cnt, ", dadb =", da_cnt)
        exit()

    else:
        print("Count is OK")
        cur = conn_dadb.cursor()

        sql = '''select id, name, prof, classroom
                   from Subject
                  where id = %s
                    and name = %s
                    and prof = %s
                    and (case when %s is null 
                              then classroom is null
                              else classroom = %s end)
                  '''
        cur.executemany(sql, dooo_list)
        # cur.executemany(sql, lst)
        curcnt = cur.rowcount

        if rand_row_count == curcnt:
            print("Whole data is OK", "Verified count is", rand_row_count)

        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Fail",
                  rand_row_count, curcnt)


