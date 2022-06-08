#!/usr/bin/python3

fruits = {'Apple', 'Banana', 'Orange', 'Pineapple', 'Mango', 'Banana'}
# print(fruits)

a = set('abracadabra')
b = set('alacazam')
print("a = {}".format(a))  # Letter unique in a
print("a - b = {}".format(a - b))  # letter in a not in b
print("a | b = {}".format(a | b))  # letter in a or b and both
print("a & b = {}".format(a & b))  # letter in both a and b
print("a ^ b = {}".format(a ^ b))   # letter in a or b but not in both


a = [x for x in a if x not in 'abc']
print("{}".format(a))
