#!/usr/bin/env python3

# ---------- helper
def readfile(filename: str) -> list[int]:
    with open(filename) as f:
        buf = f.read()
    lines = [int(line or -1) for line in buf.split("\n")]
    lines.append(-1)
    return lines

def getmax(a: int, b: int) -> int:
    if a > b:
        return a
    return b

def printF(message: str, value):
    print(f"{message} {value}")
# ---------- helper

def aufgabe1_maxcal(lst: list[int]) -> int:
    maxElf = 0
    currentElf=0
    for cal in lst:
        if cal == -1:
            maxElf = getmax(currentElf, maxElf)
            currentElf = 0
        else: 
            currentElf += cal
    return getmax(currentElf, maxElf)

def aufgabe2_top3(lst: list[int]) -> int:
    idx = [i for i in range(len(lst)) if lst[i] == -1]
    toplist = list()
    for i in range(len(idx)):        
        if(i > 0):        
           toplist.append(sum(lst[idx[i-1]+1 : idx[i]]))
        else:
            toplist.append(sum(lst[0 : idx[i]]))

    return sum(sorted(toplist, reverse=True)[:3])


print("Advent of code 2022 - day 01")
rawinput = readfile("day01/day01-input.txt")
printF("Aufgabe 1:", aufgabe1_maxcal(rawinput))
printF("Aufgabe 2:", aufgabe2_top3(rawinput))