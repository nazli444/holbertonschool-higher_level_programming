#!/usr/bin/python3
"""
Module that prints a text with 2 new lines after '.', '?', and ':'
"""


def text_indentation(text):
    """
    Prints text with 2 newlines after '.', '?', ':'
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    buffer = ""

    while i < length:
        char = text[i]
        buffer += char
        if char in ".?:":
            print(buffer.strip(), end="\n\n")
            print()
            buffer = ""
        i += 1

    if buffer.strip():
        print(buffer.strip(), end="")
