#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str):
        return str
    if n < len(str):
        return str
    return str.replace(str[n], "")
