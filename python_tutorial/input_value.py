가로_세로 = input("가로와 세로는?? (usage: 가로,세로)")
print("1111>>", 가로_세로, 가로_세로.split(','))
가로, 세로 = 가로_세로.split(',')
print("2222>>", 가로, 세로)
결과 = rect1.넓이(가로, 세로)
print("직사각형의 넓이는 {}입니다".format(결과))