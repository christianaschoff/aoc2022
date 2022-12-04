#!/usr/bin/env python3

# ---------- helper
def readfile(filename: str) -> list[list[str]]:
    with open(filename) as f:
        buf = f.read()
    lines = [[bounds for bounds in line.split(",")] for line in buf.split("\n")] 
    return lines

def printF(message: str, value):
    print(f"{message} {value}")
# ---------- helper

def check_intersection(l1: int, u1: int, l2: int, u2: int) -> bool:
    if(l1 >= l2 and u1 <= u2): # first is in second        
        return True
    if(l1 <= l2 and u1 >= u2): # second in first        
        return True
    return False

def check_contains_any(l1: int, u1: int, l2: int, u2: int) -> bool: 
    one = range(l1, (u1+1))
    two = range(l2, (u2+1))
    oneSet = set(one)
    result = oneSet.intersection(two) 
    
    return len(result) > 0

def process_aufgabe(lst: list[list[str]], aufgabe: int) -> int:
    cnt = 0
    for pair in lst:
        assign1 = pair[0].split("-")
        assign2 = pair[1].split("-")
        if aufgabe == 1 and check_intersection(int(assign1[0]), 
                                               int(assign1[1]), 
                                               int(assign2[0]), 
                                               int(assign2[1])):
            cnt += 1
        elif aufgabe == 2 and check_contains_any(int(assign1[0]), 
                                                 int(assign1[1]), 
                                                 int(assign2[0]), 
                                                 int(assign2[1])):
            cnt += 1

    return cnt

rawinput = readfile("day04/day04-input.txt")
result = process_aufgabe(rawinput, 1)
printF("Ergebnis Aufgabe 1: ", result)

result2 = process_aufgabe(rawinput, 2)
printF("Ergebnis Aufgabe 2: ", result2)