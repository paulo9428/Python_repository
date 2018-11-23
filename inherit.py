class Dog:
    def__init__(self):
        self.name = "Baduk"
        print("Dog was Born")

    def speak(self):
        print("hey!", self.name)

    def __del__(self):
        print("Destroy!!")

civa = Dog()

civa.__init__()


