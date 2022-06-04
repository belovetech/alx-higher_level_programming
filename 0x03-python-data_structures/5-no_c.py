#!/usr/bin/python3
def no_c(my_string):
    new_str = [s for s in my_string if s != 'c' or s != 'C']
    return ("".join(new_str))
