#!/usr/bin/env python3
LEFT_BIGGER = 1
RIGHT_BIGGER = -1
SAME = 0

class Pairs:
    def __init__(self, lst: list[str]):
        self.left = eval(lst[0])
        self.right = eval(lst[1])

    def compare_int(self, left, right):
            if left < right:
                return RIGHT_BIGGER
            if right < left:
                return LEFT_BIGGER
            else:
                return SAME

    def compare_array_len(self, left, right):
        if len(left) == 0 and len(right) != 0:
            return RIGHT_BIGGER
        elif len(left) != 0 and len(right) == 0:
            return LEFT_BIGGER
        elif len(left) == 0 and len(right) == 0:
            return SAME
        else:
            return None

    def compare_element(self, left, right):
        if (isinstance(left, int) and isinstance(right, int)):
            return self.compare_int(left, right)
        elif isinstance(left, int) and isinstance(right, list):
            return self.compare_element([left], right)
        elif isinstance(left, list) and isinstance(right, int):
            return self.compare_element(left, [right])
        else:            
            lst_compare = self.compare_array_len(left, right)
            if(lst_compare != None):
                return lst_compare
            else:
                comp = self.compare_element(left[0], right[0])
                if(comp == SAME):
                    return self.compare_element(left[1:], right[1:])
                return comp
    
    def rightorder(self) -> int:
        return self.compare_element(self.left, self.right)

#--------- helper ---------
def readfile(filename: str) -> list[str]:
    with open(filename) as f:
        buf = f.read()
    lines =  buf.split("\n")
    return lines

#--------- helper ---------

def build_pairs(rawinput: list[str]) -> list[Pairs]:
    ret_list = list()
    for i in range(0, len(rawinput), 3):
        ret_list.append(Pairs(rawinput[i: i+2]))
    return ret_list

def check_lists(lst: list[Pairs]):    
    return sum((index+1) for index, element in enumerate(lst) if element.rightorder() == RIGHT_BIGGER)
    
#---------- prog -----------

rawinput = readfile('day13/day13-input.txt')
all_pairs = build_pairs(rawinput)
ergebnis = check_lists(all_pairs)
print(f"Ergbnis aus Aufgabe 1 ist: {ergebnis}")