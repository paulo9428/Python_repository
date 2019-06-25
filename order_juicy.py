def Order():
    juice_dic = {"A":3900, "C":4500, "G":5000, "J":5500}
    j = juice_dic[input1]
    
    return j

def Size():
    size_dic = {"G":1000, "R":500, "S":0}
    s = size_dic[input2]

    return s 

def Price():

    juice = Order()
    size = Size() 
    p = juice + size
    
    return p 

while True:

    print("덕성 카페에 오신 것을 환영합니다.^^")
    print("커피 종류와 사이즈를 선택해 주세요\n")
    input1 = input("A(아메리카노)/C(카페라떼)/G(그린티)/J(오렌지주스):")
    input2 = input("G(Grande)/R(Regular)/S(Shot):")

    price = Price()

    print("총 금액은 {}원 입니다".format(price))
    print("맛있게 드세요~~\n")




