#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists"""
    result_list = []
    for x in range(list_length):
        try:
            quotient = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            print("division by  0")
            quotient = 0
        except (TypeError, ValueError):
            print("wrong type")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            result_list.append(quotient)
    return result_list
