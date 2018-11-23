import sqlite3 

conn = sqlite3.connect("tt.db")

date = (
    (21, '010'),
    (22, '010')
)

with conn:
    cur = conn.cursor()
    sql = "insert into tt(id, name) values("