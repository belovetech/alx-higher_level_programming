#!/usr/bin/python3


from hashlib import new


def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets."""
    # new_set = set_1 & set_2
    # new_set = set_1.intersection(set_2)
    new_set = []
    for i in set_1:
        for j in set_2:
            if i == j:
                new_set.append(i)
    return new_set
