#!/usr/bin/python3
def safe_print_integer_err(value):
    """prints an integer"""
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as err:
        print("Exception:", err.args)
        return False
    else:
        return True
