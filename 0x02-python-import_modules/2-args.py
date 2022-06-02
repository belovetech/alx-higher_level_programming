#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number and list of arguements."""
    import sys

    argc = len(sys.argv) - 1

    print("{} arguements:".format(argc))

    for i in range(1, argc + 1):
        print("{}: {}".format(i, sys.argv[i]))
