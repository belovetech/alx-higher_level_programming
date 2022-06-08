#!/usr/bin/python3

tel = {'Bob': '08134758846', 'Doe': '08163747884'}
tel['Joe'] = '09024464774'

# del tel['Bob']
# print(list(tel))
# print(sorted(tel))
# print(tel)

# looping techniques
for n, t in tel.items():
    print(n, t)

print("___________________\n")

# Enumerate function to print position index and corresponding value
for n, t in enumerate(['Joe', 'Bob', 'Sam', 'Ken']):
    print(n, t)

print("___________________\n")

# Using zip to pair enteries
questions = ['name', 'class', 'favourite color']
answers = ['James Ken', 'Ss1b', 'red']

for q, a in zip(questions, answers):
    print("What is your {0}? It is {1}".format(q, a))

print("___________________\n")

# Using sorted to sort item
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for i in sorted(basket):
    print(i)

print("___________________\n")

# Using set and sorted to print out unique item
for i in sorted(set(basket)):
    print(i)
