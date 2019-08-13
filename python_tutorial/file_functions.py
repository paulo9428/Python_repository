class Student:
    def __init__(self, line):
        name, gender, age, score = line.strip().split(',')
        self.name = name
        self.sex = gender
        self.age = age
        self.grade = score

    def __str__(self):
        return "{}\t{}\t{}\t{}".format(self.name[0], self.gender,
        self.age, self.score)

    def make

students = []

with open ('students(2).csv','r') as file:
    for i, line in enumerate(file):
        if i == 0: continue:
            students.append(Student(line))

students.sort(key = lambda stu: stu.score, reverse = True)