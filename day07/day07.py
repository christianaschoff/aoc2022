#!/usr/bin/env python3

# ---------- helper
def readfile(filename: str) -> list[str]:
    with open(filename) as f:
        buf = f.read()
    lines = [l.strip() for l in buf.split("\n")]
    return lines

def printF(message: str, value):
    print(f"{message} {value}")
# ---------- helper

directorysizes = list()

def get_size(node):    
    if "size" in node:
        return int(node.get("size"))
    sumtotal = 0

    if "children" in node :    
        for child in node.get("children").values():            
            dirsize = get_size(child)
            sumtotal += dirsize
        directorysizes.append(sumtotal)

    return sumtotal

def create_node(parent): 
    return {"parent": parent, "children": {}}

def build_tree(input: list[str]):
    tree =  create_node(None)
    current = tree
    for row in input:   
        if(row.startswith("$ cd")):
            destination = row.split(" ")[2]
            if destination == "..": 
                current = current["parent"]
            elif destination == "/":
                current = tree
            else:
                if(destination not in current.get("children")): 
                    current["children"][destination] = create_node(current)
                current = current["children"][destination]
        elif row.startswith("dir"):
            directory = row.split(" ")[1]
            current["children"][directory] = create_node(current)
        elif not row.startswith('$ ls'):
            file = row.split(" ")
            current["children"][file[1]] = {"parent": current, "size": file[0]}    
    return tree

def aufgabe1() -> int:    
    summe = 0
    for no in directorysizes:        
        if(int(no) <= 100000):
            summe += int(no)      
    return summe

def aufgabe2() -> int:
    hddsize = 70000000
    updatesize = 30000000                  
                  
    directorysizes.sort()
    hddsize_used = directorysizes[-1]
    free = hddsize - hddsize_used
    needs_to_be_freed = (updatesize - free)

    for s in directorysizes:
        if s > needs_to_be_freed:
            return s    
    
#----- prog
rawinput = readfile('day07/day07-input.txt')
m = build_tree(rawinput)
get_size(m)
printF("Ergebnis Aufgabe 1: ", aufgabe1())
printF("Ergebnis Aufgabe 2: ", aufgabe2())