#!/usr/bin/env python3

# ---------- helper
def readfile(filename: str) -> list[str]:
    with open(filename) as f:
        buf = f.read()
    rows =  buf.split("\n")

    lines = [[int(i) for i in list(row)] for row in rows]
    return lines

def printF(message: str, value):
    print(f"{message} {value}")

def printLn(lst: list[list[int]]):
    for row in lst:
        print(row)
    print("-----")

def transform(lst: list[list[int]]) -> list[list[int]]:
    ret = list()
    for i in range(len(lst)):        
        ret.append(list())

    for row in lst:  
        for i in range(len(row)):
            ret[i].append(row[i])       
    return ret
# ---------- helper

def visible_outside_grid(cell: int, before:list[int], after:list[int], top:list[int], bottom:list[int]) -> int:
    if cell > max(before) or cell > max(after):                    
        return 1
    else:                                   
        if cell >  max(top) or cell > max(bottom):                        
            return 1
    return 0


def determine_index(val: int, lst: list[int]) -> int:
    for index, item in enumerate(lst):
        if(item >= val):
            return index+1

    #print(val, lst, len(lst))
    return len(lst)

def scenic_score(cell: int, before:list[int], after:list[int], top:list[int], bottom:list[int]) -> int:
    before.reverse()
    bottom.reverse()

   # print(cell)
   # print(top)
   # print(before)
   # print(after)
   # print(bottom)
    tp = determine_index(cell, top)
    be = determine_index(cell, before)
    ar = determine_index(cell, after)
    bm = determine_index(cell, bottom)

    #print(tp, be, ar, bm)
    return (tp * be * ar * bm)

def examine_list(lst1: list[list[int]], lst2: list[list[int]]) -> int:
    retVal = 0
    maxVisibleTrees = 0
    for j in range(1, len(lst1)-1):
        row = lst1[j]
        for i in range(0, len(row)):
            rowTans = lst2[i]
            if i != 0 and (i != len(row)-1):
                cell = row[i]
                before =  row[0: i]
                after =  row[i+1: len(row)]
                top = rowTans[0:j]
                bottom = rowTans[j+1: len(rowTans)]
                retVal += visible_outside_grid(cell, before, after, top, bottom)
                localMax = scenic_score(cell, before, after, top, bottom)
                if(localMax > maxVisibleTrees):
                    maxVisibleTrees = localMax
    print(maxVisibleTrees)
    return retVal

def aufgabe1(lst1: list[list[int]], lst2: list[list[int]]) -> int:
    #fetch all borders and keep in mind not to count edges 2 times
    base = ((len(lst1) * 2) -2) + ((len(lst1[0]) * 2) -2)    
    base +=examine_list(lst1, lst2)        
    return base

rawinput = readfile("day08/day08-input.txt")
original = rawinput
transformed = transform(original)

result = aufgabe1(original, transformed)
printF("Ergebnis Aufgabe 1:", result)