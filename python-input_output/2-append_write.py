#!/usr/bin/python3

def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as f:
        characters_written = f.write(text)
        return characters_written
