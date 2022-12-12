#!/usr/bin/env python3

#--------- helper ---------
def readfile(filename: str) -> list[str]:
    with open(filename) as f:
        buf = f.read()
    lines = [l.strip() for l in buf.split("\n")]
    return lines

#--------- helper ---------

class Monkey:     
    def __init__(self, lst: list[str]):
        self.elements = [(int(elem.strip())) for elem in lst[1].split(":")[1].split(",")]
        op = lst[2].split(" ")
        if(op[5].isnumeric()):
            self.operation = op[4]
            self.factor = int(op[5])
        else:
            self.operation = "^"
            self.factor = 2
        self.devisible = int(lst[3].split(" ")[-1])
        self.true_case = int(lst[4].split(" ")[-1])
        self.false_case = int(lst[5].split(" ")[-1])
        self.inspection_counter = 0

    def operate(self, reduce_panic: bool) -> tuple():
        if(len(self.elements) == 0):
            return (None)

        old = self.elements.pop(0)
        new = 0
        match self.operation:
            case "*":
               new = old * self.factor
            case "+":
               new = old + self.factor
            case "^":
               new = pow(old, self.factor)
               #print(new)
        if reduce_panic:
            new = new // 3
        self.inspection_counter += 1

        if new % self.devisible == 0:
            return (self.true_case, new)
        else:
            return (self.false_case, new)
    
    def print(self):
        print("Monkey:", self.elements)
        print("operation:", self.operation)
        print("factor:", self.factor)
        print("devisable:", self.devisible)
        print("true:", self.true_case)
        print("false:", self.false_case)
#------------------------------
def print_monkeys(lst: list[Monkey]):
    for i, monkey in enumerate(monkeys):
        print("Monkey ", i, ":", monkey.elements)
    print("------")

def create_monkeys(lst: list[str]) -> list:
    ml = list()
    for i in range(0, len(lst), 7):        
        monkey = lst[i:i+6]        
        mc = Monkey(monkey)        
        ml.append(mc)
    return ml

def play_round(monkeys: list[Monkey], reduce_panic: bool):
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        while len(monkey.elements) > 0:
            result = monkey.operate(reduce_panic)
            monkeys[result[0]].elements.append(result[1])    

def play_rounds(monkeys: list[Monkey], rounds: int, reduce_panic: bool) -> int:
    for r in range(rounds):        
        print("Round:", (r+1))
        play_round(monkeys, reduce_panic) 
        print_monkeys(monkeys)

    res = [int(m.inspection_counter) for m in monkeys]
    res.sort(reverse=True)
    return res[0] * res[1]

## ---- prog ---
rawinput = readfile("day11/day11-input.txt")
monkeys = create_monkeys(rawinput)
result = play_rounds(monkeys, 20, True)
print("Das Ergebnis von Aufgabe 1 ist: ", result)
