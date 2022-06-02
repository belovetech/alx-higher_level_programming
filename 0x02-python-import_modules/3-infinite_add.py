#!/usr/bin/python3

if __name__ == "__main__":
    """print the result of the addition of all arguments"""
    import sys

    sum = 0
    argc = len(sys.argv)
    for i in range(1, argc):
        sum += int(sys.argv[i])

    print("{}".format(sum))
