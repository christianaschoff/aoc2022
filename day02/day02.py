#!/usr/bin/env python3

# ---------- helper
def readfile(filename: str) -> list[int]:
    with open(filename) as f:
        buf = f.read()
    lines = [[elem for elem in line.split(" ")] for line in buf.split("\n")]    
    return lines

def printF(message: str, value):
    print(f"{message} {value}")
# ---------- helper

rock = 'A'
paper = 'B'
scissor = 'C'

def harmonizeInput(code: str) -> str:        
    if code == 'X':
        return rock
    if code == 'Z':
        return scissor
    if code == 'Y':
        return paper

def decode(elf: str, code: str) -> str:
    if code == 'X': #lose
        if elf == rock:
            return scissor
        if elf == paper:
            return rock
        if elf == scissor:
            return paper

    if code == 'Z': #win  
        if elf == rock:
            return paper
        if elf == paper:
            return scissor
        if elf == scissor:
            return rock

    if code == 'Y': #draw
        return elf

def shapescore(shape: str) -> int:
    if shape == rock:
        return 1
    if shape ==  paper:
        return 2
    if shape ==  scissor: 
        return 3
    return 0

def matchset(opponent: str, me: str) -> int:
    result: int = 0
    if opponent == me:
        result = 3        
    if me == rock and opponent == scissor:
        result = 6 
    if me == paper and opponent == rock:
        result = 6
    if me == scissor and opponent == paper:
        result = 6        
    return result + shapescore(me)

def matches(input: list[list[str]], aufgabe: int) -> int:
    score:int = 0
    for m in input:
        if aufgabe == 1:
            score += matchset(m[0], harmonizeInput(m[1]))
        else:
            score += matchset(m[0], decode(m[0], m[1]))
    return score


print("Advent of code 2022 - day 02")
rawinput = readfile("day02/day02-input.txt")
printF("Aufgabe 1:", matches(rawinput, 1))
printF("Aufgabe 2:", matches(rawinput, 2))