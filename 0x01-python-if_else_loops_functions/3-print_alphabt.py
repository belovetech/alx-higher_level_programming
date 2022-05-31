#!/usr/bin/python3
for ch in range(97, 123):
    if ch == 99 or ch == 113:
        continue
    else:
        print("{}".format(chr(ch)), end="")
