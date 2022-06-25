
matrix = [[1, 2.3, 3], [4, 5.2, 6.7]]
# new_list = []

x = ([list(map(lambda x: round(x / 3.2, 2), num))for num in matrix])
print(x)
