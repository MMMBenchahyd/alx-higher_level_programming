#!/usr/bin/python3

def remove_char_at(str, n):
    strcpy = ""
    total = 0

    for c in str:
        total += 1
    if n > (total - 1) or n < 0:
        return str

    b = str[n]
    for c in str:
        if c != b:
            strcpy += c

    return strcpy
