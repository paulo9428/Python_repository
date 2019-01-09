import pymysql

def get_mysql_conn(db):
    return pymysql.connect(
        host = 'localhost', 
        user = 'dooo', 
        password = '1234', 
        port = 3307, 
        db = db, 
        charset = 'utf8'
        )

def trun_table(conn, tbl):
    cur = conn.cursor()   
    cur.execute('truncate ' + tbl)


def get_count(conn, tbl, where = ''):
    cur = conn.cursor()
    sql = "Select count(*) from " + tbl
    if where != '':
        sql = sql + "where" + where
    cur.execute(sql)

    return cur.fetchone()[0]

import cx_Oracle

def get_oracle_conn():
    return cx_Oracle.connect("hr", "hrpw", "localhost:1521/xe")


def valid (ora_column , ora_table, mys_column, mys_table, mys_id = 'id'): 

    connection = get_oracle_conn()
    with connection:
        curs = connection.cursor()
        rand = 'select * from (select ' + ora_column + ' from ' + ora_table + ' order by DBMS_RANDOM.RANDOM) where rownum <= 5 '
                
        curs.execute(rand)
        rand_oracle_employee = curs.fetchall()
        emp_id = []
        for i in range(0,5):
            if ora_table == 'Job_history':
                emp_id.append((rand_oracle_employee[i][0] ,rand_oracle_employee[i][3]))
            else:
                emp_id.append(rand_oracle_employee[i][0])

    conn_dooodb = get_mysql_conn('dooodb')
    with conn_dooodb:
        cur = conn_dooodb.cursor()
        if ora_table == 'Job_history':
            vr = 'select ' + mys_column + ' from ' + mys_table + '  where ' + mys_id + '= %s and Job_id = %s'
            vr_dooodb = []
            for i in emp_id:
                cur.execute(vr, (i[0], i[1]))
                vr_dooodb.append(cur.fetchone())

        else :
            vr = 'select ' + mys_column + ' from ' + mys_table + '  where ' + mys_id + '= %s'
            vr_dooodb = []
            for i in emp_id:
                cur.execute(vr, i)
                vr_dooodb.append(cur.fetchone())
            
        if rand_oracle_employee == list(vr_dooodb):
            print("---------------------" + mys_table + " OK----------")
        else:
            print("!!!!!!!!!!!!!!!!" + mys_table + " Wrong data--------")
