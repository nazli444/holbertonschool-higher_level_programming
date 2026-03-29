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
            # Strip leading/trailing spaces before printing
            print(buffer.strip())
            print()  # extra newline
            buffer = ""
        i += 1

    # Print remaining text if any
    if buffer.strip():
        print(buffer.strip())
