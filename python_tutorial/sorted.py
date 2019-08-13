numbers = [5,3,4,2,1]
sort_numbers = sorted(numbers)     # cf. reversed(numbers)
print("sort_numbers=", sort_numbers)
print("numbers=", numbers)

numbers.sort()
print("asc>>", numbers)

numbers.sort(reverse=True)
print("desc>>", numbers)
