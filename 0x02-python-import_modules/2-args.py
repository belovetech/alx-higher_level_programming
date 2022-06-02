#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number and list of arguements."""
    import sys

    argcount = len(sys.argv) - 1

    if argcount == 0:
        print("0 arguements.")
    elif argcount == 1:
        print("1 arguement:")
    else:
        print("{} arguements:".format(argcount))

    for i in range(argcount):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
