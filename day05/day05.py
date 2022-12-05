#!/usr/bin/env python3

# ---------- helper
def readfile(filename: str) -> list[str]:
    with open(filename) as f:
        buf = f.read()
    lines = buf.split("\n")
    return lines

def find_container_stacks(lst: list[str]) -> list[list[str]]:
    arr = list()
    n = 4
    for i in range(len(lst)):
        if (lst[i].startswith(' 1')):
            break    
        r = lst[i]        
        row = [r[j:j+n] for j in range(0, len(r), n)]
        arr.append(row)
    
    arr.reverse()
    return arr
        
def transform_containers_to_valid_arraylist(lst: list[list[str]]):
    ret = list()
    for i in range(len(lst)+1):        
        ret.append(list())

    for row in lst:        
        for i in range(len(row)):
            val = row[i].strip()            
            if(val != ''):    
                #print(i, "->", val, len(ret))            
                ret[i].append(val.replace("[", "").replace("]", ""))                
    return ret

def generate_moves(lst: list[str]) -> list[list[str]]:
    start = False
    movelist = list()

    for row in lst:
        if start == True:
           elems = row.split(" ")
           movelist.append([elems[1], elems[3], elems[5]])
        elif row == '':
            start = True
    return movelist

def printF(message: str, value):
    print(f"{message} {value}")
# ---------- helper

def aufgabe1(stacks:list[list[str]], moves: list[list[str]]) -> str:
    for move in moves:
        source = int(move[1])-1
        destination = int(move[2])-1
        amount = int(move[0])
        for i in range(0, amount):
            stacks[destination].append(stacks[source].pop())
    
    retStr = ""
    for elem in stacks:
        if len(elem) > 0:
            retStr += elem[len(elem) -1]
    return retStr


def aufgabe2(stacks:list[list[str]], moves: list[list[str]]) -> str:
    for move in moves:
        source = int(move[1])-1
        destination = int(move[2])-1
        amount = int(move[0])

        tmpList = list()
        for i in range(0, amount):        
            tmpList.append(stacks[source].pop())
        tmpList.reverse()

        for elem in tmpList:
            stacks[destination].append(elem)
    
    retStr = ""
    for elem in stacks:
        if len(elem) > 0:
            retStr += elem[len(elem) -1]
    return retStr

# -- prog
rawinput = readfile("day05/day05-input.txt")
moves = generate_moves(rawinput)
stacks = find_container_stacks(rawinput)

transformed_stacks = transform_containers_to_valid_arraylist(stacks)
printF("Ergebnis Aufgabe 1:", aufgabe1(transformed_stacks, moves))
#print("stacks: ", stacks)
#print("array list: ", transformed_stacks)
#print("moves: ", moves)

transformed_stacks = transform_containers_to_valid_arraylist(stacks)
printF("Ergebnis Aufgabe 2:", aufgabe2(transformed_stacks, moves))
