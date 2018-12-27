i=2; sum=0
while i>= 2:
    i += 1
    for m in range(2,i):
        if i % m == 0: 
            sum += i
        
    if i < 100 :
        continue
    elif i == 100 :
        print(5050-sum-2)
        break