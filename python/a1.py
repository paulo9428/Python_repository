class TestClass:
    
    name = "Test"

    def static_method():
        print('STATIC!!')

    def get_name(self):
        print('qqqqqqqq')
        return self.name

    def area(self, x, y):
        return x * y

class Child(TestClass):

    def __init__(self):
        super().__init__()
        print('my init!!')

    def get_name(self):
        t = super().get_name()
        return "child name:" + self.name

    def area(self, x, y):
        t = super().area(x,y)
        return t / 2
