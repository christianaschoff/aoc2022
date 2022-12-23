#!/usr/bin/env python3



class Monkey:
    def __init__(self, raw:str):
        base = raw.split(":")
        self.data =  base[1].strip().split(" ")
        self.name = base[0].strip()
    
    def operate(self, allmonkeys: list):        
        if (self.data[0].isnumeric()):
            return int(self.data[0])        
        else:
            #left = (x for x in allmonkeys if x.name == self.data[0])
            li = next(i for i, x in enumerate(allmonkeys) if x.name == self.data[0])
            ri = next(i for i, x in enumerate(allmonkeys) if x.name == self.data[2])
            left = allmonkeys[li]
            operation = self.data[1]
            right = allmonkeys[ri]
            if(right != None and left != None):                
                match(operation):
                    case '+':                        
                        return left.operate(allmonkeys) + right.operate(allmonkeys)
                    case '-':
                        return left.operate(allmonkeys) - right.operate(allmonkeys)
                    case '/':
                        return left.operate(allmonkeys) // right.operate(allmonkeys)
                    case '*':
                        return left.operate(allmonkeys) * right.operate(allmonkeys)

    def print_me(self, val):        
        print("".join(val))


def find_root(allmonkeys: list) -> Monkey:
    li = next(i for i, x in enumerate(allmonkeys) if x.name == 'root')
    return allmonkeys[li]

#--------- methods ----------
def readfile(filename: str) -> list[str]:
    with open(filename) as f:
        buf = f.read()
    lines =  buf.split("\n")
    return lines



#--------- prog --------------
rawinput = readfile('day21/day21-input.txt')
lst = list()
lst = [Monkey(row) for row in rawinput]

root = find_root(lst)
print(root.operate(lst))