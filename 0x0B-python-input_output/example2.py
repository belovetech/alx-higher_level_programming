#!/usr/bin/python3
import os


with open('myfile.txt', mode="w", encoding="utf-8") as f:
    f.write(
        "Some text\nsome random text\nother text\nmore random text and numbers")

with open("myfile.txt", encoding="utf-8") as f:
    lineNum = 1

    while True:
        line = f.readline()

        if not line:
            break

        print("Line : {}".format(lineNum))

        wordlist = line.split()
        wordCount = len(wordlist)

        charCount = 0
        for word in wordlist:
            for char in word:
                charCount += 1

        print("Number of words: {}".format(wordCount))
        print("Number of characters: {}".format(charCount))

        avgCharCount = charCount / wordCount

        print("Average char count: {:.2f}".format(avgCharCount))

        lineNum += 1
