# https://cskstory.tistory.com/entry/%EB%A7%B5%EB%A6%AC%EB%93%80%EC%8A%A4-MapReduce-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0

samples = [
    (2001, 23),
    (2002, 7),
    (2002, -12),
    (2001, 21),
    (2003, 20),
    (2005, 13),
    (2003, 3),
    (2005, -2),
    (2003, 22),
    (2001, -3),
]

dic = {}
a = []

for i in samples:
    if i[0] in dic.keys():
        dic[i[0]].append(i[1])

    else:
        dic[i[0]] = .append(i[1])

print(dic)


    
    
    
#     if i[0] in dic.keys()
    
#     dic[i[0]]   

# print(dic)
    