#!/usr/bin/env python3

# ---------- helper
def readfile(filename: str) -> str:
    with open(filename) as f:
        buf = f.read()
    return buf

def process_rawinput_1(rawinput: str) -> list[list[str]]:
    return [[line[i: i+int(len(line)/2)] for i in range(0, len(line), int(len(line)/2))] for line in rawinput.split("\n")]     

def process_rawinput_2(rawinput: str) -> list[list[str]]:
    lines = [line for line in rawinput.split("\n")] 
    return [lines[i: i+3] for i in range(0, len(lines), 3)]    

def printF(message: str, value):
    print(f"{message} {value}")
# ---------- helper

def findmatch_of_two(val1: str, val2: str) -> str:
    return "".join(set(val1).intersection(val2))

def find_match_3(val1: str, val2: str, val3) -> str:
    tmp =  "".join(set(val1).intersection(val2))
    return "".join(set(tmp).intersection(val3))

def sum_ordinals(lst: list[str]) -> int:
    #96 =  -> 97-1 -> start if acsii for lower case, but should start with 1 instead of 0 in out algorithm
    # 38 -> 65-27 -> start of ascii for uppercase, but should be in a higher range in our algorithm
    ordList = [ord(element) -(96 if ord(element) >= 97 else 38) for element in lst]    
    return sum(ordList)

def pair_double(backpacks: list[list[str]]) -> list[str]:
    retList = list()
    for backpack in backpacks:
        retList.append(findmatch_of_two(backpack[0], backpack[1]))
    return retList

def pair_triple(backpacks: list[list[str]]) -> list[str]:
    retList = list()
    for backpack in backpacks:
        retList.append(find_match_3(backpack[0], backpack[1], backpack[2]))
    return retList

## ------- prog
rawinput = readfile("day03/day03-input.txt")
input = process_rawinput_1(rawinput)
printF("Aufgabe 1:", sum_ordinals(pair_double(input)))

input = process_rawinput_2(rawinput)
printF("Aufgabe 2:", sum_ordinals(pair_triple(input)))
