#!/usr/bin/python3
"""Module 5-text_indentation.

Provides a function that prints a text with 2 new lines
after each of these characters: '.', '?' and ':'.
"""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?' and ':'.

    Raises TypeError if text is not a string."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for char in text:
        line += char
        if char in ".?:":
            print(line.strip(" "), end="\n\n")
            line = ""
    print(line.strip(" "), end="")
