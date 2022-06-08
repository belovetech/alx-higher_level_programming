#!/usr/bin/python3

# Transformation function
def square(num):
    return num ** 2


# Variables
nums = [1, 2, 3, -4, 5, -5, -3]
str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]
words = ["Welcome", "to", "Real", "Python"]

# map usage
abs_nums = list(map(abs, nums))
square_nums = list(map(square, nums))
int_nums = list(map(int, str_nums))
len_words = list(map(len, words))

# print result
print(nums)
print(abs_nums)
print(square_nums)
print(int_nums)
print(len_words)
