#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        """Change to uppercase character."""
        if ord(ch) >= 97 and ord(ch) <= 123:
            print("{}".format(chr(ord(ch) - 32)), end="")
        else:
            print("{}".format(chr(ord(ch))), end="")
    print()
