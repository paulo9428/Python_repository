sum = 0
for i in range(1,101):
    if i == 1:
        continue
    if i == 2:
        sum += i
    for x in range (2,i):
        if i % x == 0:
            break
        elif x == i - 1:
            sum += i
print(sum)  
