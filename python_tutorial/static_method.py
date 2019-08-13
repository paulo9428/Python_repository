class Dog:
    def m1(self):
        print("m1")

    def m2():
        print("m2")

dog = Dog()

dog.m1()

# error 발생
dog.m2() 
# 인스턴스 없이 
Dog.m2()
