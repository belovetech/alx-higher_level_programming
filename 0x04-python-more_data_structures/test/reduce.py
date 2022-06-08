#!/usr/bin/python3
from functools import reduce

num = [47, 11, 42, 13]

sum = reduce(lambda x, y: x + y, num)
max = reduce(lambda a, b: a if a > b else b, num)
min = reduce(lambda a, b: a if a < b else b, num)
factorial = reduce(lambda x, y: x * y, range(1, 6))


# print result
print(sum)
print(max)
print(min)
print(factorial)
