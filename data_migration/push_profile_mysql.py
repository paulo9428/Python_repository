data = ((), (), ())                                                 ##튜플에만 담겨야 하나??

with open("students.csv", "r", encoding= 'utf8') as file:
    for line in file:                                                ##첫 줄 어떻게 거르지?
        
        elements = line.split(',')

class Transform:

    def name(): #elements[0]

        return elements[0][1] + "**"
    
    def gender(): 
        
        if elements[1] == '남':
                return "M"
        if elements[1] == '여':
                return "F"

        
    def age():  #elements[2]

        return elements[2][1] + "0대"

    
    def grade(): #elements[3]

        

    def address(): #elements[4]
        gu_dong = elements[4].split[" "]

        return gu_dong[1] + " " + gu_dong[2]






          
import sqlite3

conn = sqlite3.connect("exam.db")

with conn:
    cur = conn.cursor()
    sql = "insert in Students(name, gender, age, grade, address) value(?, ?, ?, ?, ?); select * from Students order by grade desc;"      ## 성적이 같다면 어떻게 정렬??

    cur.executemany(sql, data)

    con commit


        
