#!/usr/bin/env python3

#--------- helper ---------
def readfile(filename: str) -> list[str]:
    with open(filename) as f:
        buf = f.read()
    lines = [l.strip() for l in buf.split("\n")]
    return lines

# -------- helper ---------

def fill_signal_list(lst: list[str]):
    retLst = list()
    retLst.append(1)
    val = 1
    for signals in lst:
        if(signals.startswith("noop")):
            val = val
        else:
            a, v = signals.split(" ")
            if a == "addx":
                retLst.append(val)                
                val += int(v)
        retLst.append(val)                    
    return retLst

def caluclate_values(lst: list[str]) -> int:
    
    retVal = 0
    steps= [20, 60, 100, 140, 180, 220]
    for i, v in enumerate(steps):
        print(i, ":", v, "*", lst[(v-1)])
        retVal += (v * lst[(v-1)])
    return retVal
    
# ----- program -----
rawinput = readfile('day10/day10-input.txt')
lst = fill_signal_list(rawinput)
print(lst)
print ("Ergebnis Aufgabe 1:", caluclate_values(lst))