import sqlite3
import random

fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")

first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")

conn = sqlite3.connect("test.db")


def make_name():


    a = random.choice(fam_names)
    b = "".join(random.sample(first_names, k=2))

    full_name = a + b[0] + b[1]
    
    return (full_name,)

print(make_name())

data = []

for i in (0,100):
    data.append(make_name())

exit()

with conn:
    cur = conn.cursor()
    sql = "insert into test(name) values(data)"
    cur.executemany(sql, data)

    conn.commit()

    
       
    
        