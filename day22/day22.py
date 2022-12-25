#!/usr/bin/env python3
import time
import sys

RIGHT = "R"
LEFT = "L"
UP = "T"
DOWN = "B"

TILE = "."
WALL = "#"
VOID = " "


class Player:
    def __init__(self, start_x: int):
        self.position_x = start_x
        self.position_y = 0
        self.direction = RIGHT
    
    def turn(self, val: str):    
        if(self.direction == RIGHT):
            self.direction =  DOWN if val == RIGHT else UP
        elif(self.direction == DOWN):
            self.direction = LEFT if val == RIGHT else RIGHT

        elif(self.direction == LEFT):
            self.direction = UP if val == RIGHT else DOWN
        elif(self.direction == UP):
            self.direction = RIGHT if val == RIGHT else LEFT
        #print(self.direction)        

    def move(self, steps: int, board: list[list[str]]):
        max_cols = len(board[0]) -1
        max_rows = len(board) -1

        for i in range(steps):
            x = self.position_x
            y = self.position_y        
            if(self.direction == RIGHT):
                if(x < max_cols):
                    x += 1
                else:
                    x = 0
            if(self.direction == LEFT):
                if(x > 0):
                    x -= 1            
                else:
                    x = max_cols
            if(self.direction == UP): 
                if(y > 0):
                    y -= 1
                else:
                    y = max_rows
            if(self.direction == DOWN): 
                if(y < max_rows):
                    y += 1
                else:
                    y = 0
                        
            next_tile = board[y][x]

            if(next_tile == TILE):
                self.position_x = x
                self.position_y = y

            elif(next_tile == WALL):
                return

            elif(next_tile == VOID):
                if(self.direction == LEFT or self.direction == RIGHT):
                    row = board[y]
                    self.position_y = y
                    if(self.direction == LEFT):
                        tmpx = max(index for index, val in enumerate(row) if val != VOID)
                    else:
                        tmpx = next(index for index, val in enumerate(row) if val != VOID)                        
                    if (board[y][tmpx] != WALL):
                        self.position_x = tmpx 

                if(self.direction == UP or self.direction == DOWN):
                    self.position_x = x
                    swap_to_row = self.column(board, x)
                    if(self.direction == UP):
                        tmpy = max(index for index, val in enumerate(swap_to_row) if val != VOID)
                    if(self.direction == DOWN):
                        tmpy = next(index for index, val in enumerate(swap_to_row) if val != VOID)
                    if(board[tmpy][x] != WALL):
                        self.position_y = tmpy
            
            print_board(board, self)
            #print(self.position_x, ",", self.position_y)
            
    def column(self, board: list[list[str]], row: int):
            return [field[row] for field in board]

    def result(self):
        print(self.position_x, " ", self.position_y, " ", self.direction)

        x = self.position_x+1
        y = self.position_y+1

        ergebnis = x * 4 + y * 1000

        if(self.direction == UP):
            return ergebnis + 3
        if(self.direction == DOWN):
            return ergebnis + 1
        if(self.direction == LEFT):
            return ergebnis + 2

        return ergebnis            

#--------- methods ----------
def readfile(filename: str) -> list[str]:
    with open(filename) as f:
        buf = f.read()
    lines =  buf.split("\n")
    return lines

def extract_playfield(rawinput: list[str]) -> list[list[str]]:
    raw_board = [[*field] for field in rawinput[0 : -2]]
    max_len = max(len(row) for row in raw_board)
    for i in range(len(raw_board)):
        row = raw_board[i]
        if len(row) < max_len:
            for j in range(len(row), max_len):
                row.append(" ")
    return raw_board

def extract_moves(rawinput: list[str]) -> list[str]:    
    line = rawinput[-1]
    directions = [i for i, x in enumerate(line) if not x.isnumeric()]    

    retList = list()
    for i in range(len(directions)):        
        if(i == 0):
            von = 0
        else:
            von = directions[i -1] +1
        bis = directions[i]        
        retList.append(line[von: bis])
        retList.append(line[bis])

    if(directions[-1] != len(line)-1):        
        retList.append(line[directions[-1] + 1: len(line)]) 
    
    return retList

def find_startpos(firstrow: list[str]):
    return next(index for index, element in enumerate(firstrow) if element == ".")

def play(player: Player, steps: list[str], board: list[list[str]]):
    for i, step in enumerate(steps):
        if(step.isnumeric()):
            player.move(int(step), board)
        else:
            player.turn(step)
            print_board(board, player)

def orientation(direction: str):
    if(direction == UP):
        return "^"
    if(direction == DOWN):
        return "v"
    if(direction == LEFT):
        return "<"
    if(direction == RIGHT):
        return ">"        

def print_board(board: list[list[str]], player: Player):
    return

    for i in range(len(board)):
        s = ""
        row = board[i]
        for j in range(len(row)):
            if(player.position_x == j and player.position_y == i):
                s += orientation(player.direction)
            else:
                s += row[j]                
        sys.stdout.write(s + "\n")
    sys.stdout.flush()        
    time.sleep(.2)

# -------- programm ---------    
board = list()
steps = list()
rawinput = readfile('day22/day22-input.txt')

board = extract_playfield(rawinput)
steps = extract_moves(rawinput)
print(steps)

player = Player(find_startpos(board[0]))
print_board(board, player)
play(player, steps, board)

print(player.result())