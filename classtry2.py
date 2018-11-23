class Rectang:
    
    def __init__(self):
        self.name = "Rectang"
        self.width = 0
        print("사각형의 넓이는 다음과 같습니다.")
    
class Verti(Rectang):
    
    def verti_width(self, garo, sero):
        
        p = garo * sero
        self.width += p
        
        return self.width
    
class Horizon(Rectang):
    
    def horizon_width(self, bottom, height):
        
        q = bottom * height
        self.width += q

        return self.width
    
class Marm(Rectang):
    
    def marm_width(self, cross_1, cross_2):

        r = (cross_1 * cross_2) / 2
        self.width += r
        
        return self.width

cmd = input("사각형의 종류는? \n[1]직사각형 \n[2]평행사변형 \n[3]마름모")


if cmd.strip() == "직사각형":
    
    cmd_length = input("가로와 세로는? 2,3")
    
    cmds = cmd_length.split(',')

    if cmd_length == "m,n":

        m = int(cmds[0].strip()); n = int(cmds[1])
        print(m, n)
        
        shape_1 = Verti()
    
        result = shape_1.verti_width(m, n)

        print(result)

        
       
elif cmd == "평행사변형":

    cmd_length = input ("밑변과 높이는? (2, 3)")

    if cmd_length == "(s, t)":

        shape_2 = Horizon()

        shape_2.horizon_width(s, t)

elif cmd == "마름모" :

    cmd_length = input ("두 대각선 길이는? (2, 3)")

    if cmd_length == "(q, r)":

        shape_3 = Marm()

        shape_3.marm_width(q, r)



     


