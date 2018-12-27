class Rectang:
    def __init__(self):
        self.name = "Rectang"
        self.width = 0
        print("사각형의 넓이는 다음과 같습니다.")
    
class Verti(Rectang):
    
    def verti_width(self, garo, sero):
        
        p = garo * sero
        self.width += p
    
class Horizon(Rectang):
    
    def horizon_width(self, bottom, height):
        
        q = bottom * height
        self.width += q
    
shape_1 = Verti()

shape_1.verti_width(2,5)

print(shape_1.width)

        
