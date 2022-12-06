#!/usr/bin/env python3

# ---------- helper
def readfile(filename: str) -> list[str]:
    with open(filename) as f:
        buf = f.read()
    lines = buf.split("\n")
    return lines

def printF(message: str, value):
    print(f"{message} {value}")
# ---------- helper


def is_unique(input: str, minlength: int) -> bool:
    if(len(input) < minlength):
        return False    
    for c in input:
        if input.count(c) > 1:
            return False
    return True


def find_marker(input: str, minlength: int) -> int:    
    max = len(input)+1        
    for i in range(max):
        if(i < minlength):
            next
        if is_unique(input[(i-minlength): i], minlength) == True:
            return i
    return -1

# -- prog
rawinput = readfile("day06/day06-input.txt")
for input in rawinput:
    print(input)
    printF("Ergebnis Aufgabe 1: ", find_marker(input, 4))
    printF("Ergebnis Aufgabe 2: ", find_marker(input, 14))
