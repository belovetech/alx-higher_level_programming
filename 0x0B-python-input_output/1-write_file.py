#!/usr/bin/python3
"""
Writes a string to a text file
"""


from xml.dom.minidom import CharacterData


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8)

    Args:
        filename (str): name of the file to write
        text (str): text to write to the file

    Returns:
        number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)

        characterRead = 0
        for char in text:
            characterRead += 1

        return characterRead
