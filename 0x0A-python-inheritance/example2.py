#!/usr/bin/python3

def sorted_list(list):

    for x in range(len(list)):

        min_idx = x
        for y in range(x+1, len(list)):

            if list[min_idx] > list[y]:
                min_idx = y
        list[x], list[min_idx] = list[min_idx], list[x]
    return list


a = [9, 4, 9, 7, 8]

print(a)
print(sorted_list(a))
print(a)
