import random
from pprint import pprint
data = {
    "A" : [
        [9, -9, -4,  3,  6],
        [7, -3, -8,  4,  4],
        [7, -9,  1, -2,  8],
        [5, -3, -4, -9, -8],
        [8,  5, -5,  4,  6]
    ],

    "B" : [
        [ 2, -7,  2, -2,  0],
        [ 1,  8,  2,  2, -2],
        [ 6, -2,  5, -2,  5],
        [-4,  9, -5, -9, -7],
        [ 8,  0, -9,  2, -7]
    ],

    "C" : [
        [-9,  5, -1,  9,  4],
        [ 3, -4, -6, -3,  3],
        [ 6,  6,  7, -3, -6],
        [-8,  9,  6, -1, -2],
        [-10, 2, -8, -4,  9]
    ]
}

pprint(data)


data['A'][0][0] + data['A'][1][1] + data['A'][2][2] + data['A'][3][3] + data['A'][4][4]

data['A'][0][4] + data['A'][1][3] + data['A'][2][2] + data['A'][3][1] + data['A'][4][0]

ms = {}

for k in ['A', 'B', 'C']:
    sum1 = 0
    sum2 = 0
    
    for i in range(0, 5):
        sum1 += data[k][i][i]
        sum2 += data[k][i][4-i]

    ms[k] = sum1 + sum2

print(ms)

ssss

msl = list((v, k) for k,v in ms.items())

print(msl)
        