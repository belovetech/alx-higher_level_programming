#!/usr/bin/python3


fibonacci = [0,1,1,2,3,5,8,13,21,34,55]

odd_nums = list(filter(lambda x: x % 2, fibonacci))
even_nums = list(filter(lambda x : x % 2 == 0, fibonacci))

print(odd_nums)
print(even_nums)
