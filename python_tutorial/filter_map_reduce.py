# filter(filter_fn, iter) : filter object
def fn(x):
	return x < 0

int_numbers = range(-5, 6)
print(list(int_numbers))
negatives = filter(fn, int_numbers)
print(list(negatives))


# map(mapped_fn, iter) : map object
def make_double(n):
	return n * 2

numbers = (1, 2, 3, 4)
double_numbers = map( make_double, numbers )
print( list(double_numbers) )

triple_nubmers = map(lambda x: x * 3, numbers)
print( list(triple_nubmers) )


# reduce(reduce_fn, iter) : one result
from functools import reduce
product = 1
lst = [1, 2, 3, 4]
for num in lst:
    product = product * num

print("product1>>", product)

product2 = reduce(lambda x, y: x * y, lst)
print("product2>>", product2)



