import sqlite3
conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    sql = ""