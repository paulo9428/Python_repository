N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# result = [3,4,2,1,5]

stages_challenged = 0
stages_failed = 0

# for i in stages:
#     if i > 1:
#         stages_challenged += 1
#     if i == 1:
#         stages_challenged +=1
#         stages_failed += 1

#     return (stages_failed/stages_challenged)


# for i in stages:
#     if i > 2:
#         stages_challenged += 1
#     if i == 2:
#         stages_challenged +=1
#         stages_failed += 1

# ----------------------------------
import math

dic = {}
result = []

for n in range(1, N+1):
    for i in stages:
        
        if i > n:
            stages_challenged += 1
        if i == n:
            stages_challenged +=1
            stages_failed += 1
        

    if stages_challenged == 0:
        continue
    else:
        dic[n] = (stages_failed/stages_challenged)
        
dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
for i in dic:
    result.append(i[0])

print(result)




    

        






