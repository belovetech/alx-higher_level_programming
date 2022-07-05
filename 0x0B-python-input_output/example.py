#!/usr/bin/python3
import os


# with open('myfile.txt', mode="r", encoding="utf-8") as f:
#     for line in f:
#         print(line, end="")
#     print()

with open('myfile.txt', mode="w", encoding="utf-8") as f:
    f.write("Some text\nsome random text\nother random text")

with open("myfile.txt", encoding="utf-8") as f:
    print(f.read())

print(f.closed)
print(f.mode)
print(f.name)

# os.rename("yourfile.txt", "myfile.txt")
# os.remove("myfile.txt")
os.mkdir("mydir")
os.chdir("mydir")

print("Current Directory", os.getcwd())
os.rmdir("mydir")
