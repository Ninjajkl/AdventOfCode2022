import math
import operator


def Part1(inputName):
    return monkeyMode(inputName, 3, 20)

def Part2(inputName):
    return monkeyMode(inputName, 1, 10000)

def monkeyMode(inputName : str, worryReducer : int, limit : int):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        Input = [line.rstrip("\n") for line in f]
    monkeyBarrel = []
    i = 0
    monkeyGCF = 1
    while i < len(Input):
        startingItems = list(map(int, Input[i+1].rstrip("\n").replace("Starting items: ","").replace(",","").split()))
        operation = Input[i+2].rstrip("\n").replace("Operation: new = ","").split()
        test = int(Input[i+3].rstrip("\n").replace("Test: divisible by ",""))
        monkeyGCF *= test
        tMonkey = Input[i+4].rstrip("\n")[-1:]
        fMonkey = Input[i+5].rstrip("\n")[-1:]
        monkeyBarrel.append(Monkey(startingItems, operation, test, monkeyBarrel, tMonkey, fMonkey))
        i += 7
    currMonkey = monkeyBarrel[0]
    for i in range(0, limit):
        for j in range(0, len(monkeyBarrel)):
            currMonkey = monkeyBarrel[j]
            while(len(currMonkey.getItems()) > 0):
                currMonkey.monkeyMove(worryReducer, monkeyGCF)
    topInspection = [0,0]
    for monkey in monkeyBarrel:
        #monkey.screech()
        if monkey.getMonkeyMoves() > topInspection[0]:
            topInspection[1] = topInspection[0]
            topInspection[0] = monkey.getMonkeyMoves()
        elif monkey.getMonkeyMoves() > topInspection[1]:
            topInspection[1] = monkey.getMonkeyMoves()
    #print(topInspection)
    return topInspection[0] * topInspection[1]

class Monkey:
    def __init__(self, items : list[int], operation : list[str], test : int, monkeyBarrel, tMonkey : int, fMonkey : int):
        ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul
        }
        self.items = items
        self.operation = operation
        self.opFunction = ops[self.operation[1]]
        self.test = test
        self.monkeyBarrel = monkeyBarrel
        self.tMonkey = tMonkey
        self.fMonkey = fMonkey
        self.monkeyMoves = 0
    
    def addItem(self, item: int) -> None:
        self.items.append(item)
    
    def getItems(self):
        return self.items

    def getMonkeyMoves(self):
        return self.monkeyMoves

    def monkeyMove(self, worryReducer : int, monkeyGCF : int):
        item = self.items.pop(0)
        item = self.opFunction(item if self.operation[0] == "old" else int(self.operation[0]),item if self.operation[2] == "old" else int(self.operation[2]))
        item = math.floor(item/worryReducer) if worryReducer != 1 else item%monkeyGCF
        self.monkeyBarrel[int(self.tMonkey)].addItem(item) if item % self.test==0 else self.monkeyBarrel[int(self.fMonkey)].addItem(item)
        self.monkeyMoves += 1
    
    def screech(self):
        print("Items", end = ": ")
        print(self.items)
        #print("Operation", end = ": ")
        #print(self.operation)
        #print("test", end = ": ")
        #print(self.test)
        #print("tMonkey", end = ": ")
        #print(self.tMonkey)
        #print("fMonkey", end = ": ")
        #print(self.fMonkey)
        print("monkeyMoves", end = ": ")
        print(self.monkeyMoves)



