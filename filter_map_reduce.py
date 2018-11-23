int_numbers = range(-5, 6)

print(list(int_numbers))

negatives = map(lambda x: x * 2, int_numbers)

print(list(negatives))

def file_write():
    with open("stu_info.csv", "w", encoding="utf-8") as file:
        file.write("이름,성별,나이,성적\n")
        file.write("다람쥐,남,25,90\n")
        file.write("하마,여,15,80\n")
        file.write("참새,여,43,70\n")
        file.write("고양이,남,15,60\n")
        file.write("박쥐,여,25,74\n")
        file.write("여우,여,41, 90\n")
        file.write("사마귀,남,25,88\n")
        file.write("메뚜기,여,24,76\n")
        file.write("두부,남,27,86\n")
        file.write("앵무새,여,34,95\n")

def file_read():
    with open("stu_info.csv","r", encoding="utf-8") as file:
        for line in file:
            print(line)
