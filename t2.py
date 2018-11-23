lst = ['오렌지', '사과', '배']
dic = {'오렌지': 400, '사과': 200, '바나나': 300}

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))
exit()
def default_param(a, vp = 100):
    print(a, vp)

default_param(1)

print(dic.keys())

en = enumerate(lst)
print("list=", list(en))

for key in dic:
    print("key=", key, dic[key])

for i, value in enumerate(lst):
    print("tt=",i, value)

print(dic.items())
for key, element in dic.items():
    print("items.key=", key, ", element=", element)

for i in range(0, 20, 2):
    print(i)

arr = [i ** 2 for i in range(1, 20, 2)]
print(arr)

print("최소값:", min(arr))
print("최대값:", max(arr))

outs = [f for f in lst if f != '사과']
print(outs)

outs2 = []
for f in lst:
    if f != '사과':
        outs2.append(f)

print(outs2)
