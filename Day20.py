import sys
sys.setrecursionlimit(6000)

from copy import copy

class IntRef:
    Head = None
    Tail = None
    length = 0
    def __init__(self,val,prev = None, next = None):
        IntRef.length+=1
        self.val = val
        if IntRef.Head == None:
            IntRef.Head = self
            IntRef.Tail = self
            self.prev = self
            self.next = self
        else:
            self.prev = prev
            self.next = next

    def add(self,ref):
        ref.prev = IntRef.Tail
        IntRef.Tail.next = ref
        IntRef.Tail = ref
        ref.next = IntRef.Head
        IntRef.Head.prev = ref

    def printList(self):
        print("val:",self.val,"prev:", self.prev.val, "next:", self.next.val)
        if self != IntRef.Tail: self.next.printList()

    def __repr__(self) -> str:
        return "val: " + str(self.val) + " prev: " + str(self.prev.val) + " next: " + str(self.next.val)

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        if IntRef.Tail == self: IntRef.Tail = self.prev
        self.prev = None
        self.next = None

    def insert(self,ref):
        self.next.prev = ref
        ref.next = self.next
        self.next = ref
        ref.prev = self
        if ref == IntRef.Head: IntRef.Tail = self
        elif IntRef.Tail == self: IntRef.Tail = ref

    def move(self):
        adjustedPos = self
        adjustedVal = abs(self.val)%(IntRef.length-1)
        adjustedVal = -adjustedVal if self.val < 0 else adjustedVal
        if adjustedVal > 0:
            adjustedPos = self
            for i in range(0,adjustedVal):
                adjustedPos = adjustedPos.next
        elif adjustedVal < 0:
            adjustedPos = self
            for i in range(-1,abs(adjustedVal)):
                adjustedPos = adjustedPos.prev
        if adjustedPos != self:
            self.remove()
            adjustedPos.insert(self)
    
    def findXAfter(self,num):
        adValue = self
        for i in range(0, num%IntRef.length):
            adValue = adValue.next
        return adValue.val

def createAdjustedGrove(rawInput : list[int],numMix = 1):
    currGrove = IntRef(rawInput[0])
    orderDict = {0:currGrove}
    for i, line in enumerate(rawInput,0):
        if i == 0: continue
        intReference = IntRef(line)
        orderDict.update({i:intReference})
        currGrove.add(intReference)
    #print(orderDict)
    for i in orderDict:
        if orderDict[i].val == 0:
            zeroLoc = orderDict[i]
            break
    for i in range(0,len(rawInput)*numMix):
        orderDict[i%len(rawInput)].move()
    return currGrove, zeroLoc

def Part1(inputName):
    IntRef.length = 0
    IntRef.Head = None
    IntRef.Tail = None
    with open("Inputs\\" + inputName + "Input.txt") as f:
        Input = [int(line.rstrip("\n")) for line in f]
    currGrove, zeroLoc = createAdjustedGrove(Input,1)
    return (zeroLoc.findXAfter(1000) + zeroLoc.findXAfter(2000) + zeroLoc.findXAfter(3000))

def Part2(inputName):
    IntRef.length = 0
    IntRef.Head = None
    IntRef.Tail = None
    with open("Inputs\\" + inputName + "Input.txt") as f:
        Input = [int(line.rstrip("\n"))*811589153 for line in f]
    currGrove, zeroLoc = createAdjustedGrove(Input,10)
    return (zeroLoc.findXAfter(1000) + zeroLoc.findXAfter(2000) + zeroLoc.findXAfter(3000))