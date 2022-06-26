#!/usr/bin/python3
matrix = [
    [1, 2.3, 3],
    [4, 5.2, 6.7],
    [4, 5.2, 6.7, 5],
    [4, 5.2, 6.7]
]
# new_list = []

len1 = len(matrix[0])
flag = 0
for row in matrix:
    if len(row) != len1:
        flag = 0
        break
    else:
        flag = 1


if flag:
    print("Equal")
else:
    print("Not equal")


# for i in range(len(matrix)):
#     if len(matrix[i]) == len(matrix[i+1]):
#         print("Yes, Same")
#         break
#     else:
#         print("No, Not the same!")
#         break
