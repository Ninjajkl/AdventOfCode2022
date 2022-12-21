import operator

class monkey:
    def __init__(self,monkeyDict,Input : str,part1 : bool) -> None:
        self.part1 = part1
        self.monkeyDict = monkeyDict
        self.name = Input[:4]
        if len(Input) < 17:
            if not self.part1 and self.name == "humn":
                self.type = "h"
                return
            self.num = int(Input[6:])
            self.type = "n"
        else:
            if not part1 and self.name == "root":
                self.op = operator.eq
            elif Input.count("+") > 0:
                self.op = operator.add
            elif Input.count("-") > 0:
                self.op = operator.sub
            elif Input.count("*") > 0:
                self.op = operator.mul
            else:
                self.op = operator.floordiv
            self.m1 = Input[6:10]
            self.m2 = Input[13:]
            self.type = "o"

    def getYell(self):
        if self.type == "n":
            return self.num
        elif self.part1:
            return self.op(self.monkeyDict[self.m1].getYell(),self.monkeyDict[self.m2].getYell())
        elif self.type == "h":
            return self.type
        elif self.name == "root":
            m1Yell = self.monkeyDict[self.m1].getYell()
            m2Yell = self.monkeyDict[self.m2].getYell()
            return self.findH(self.op,m1Yell,m2Yell)
        else:
            m1Yell = self.monkeyDict[self.m1].getYell()
            m2Yell = self.monkeyDict[self.m2].getYell()
            if type(m1Yell) == int and type(m2Yell) == int: 
                return self.op(m1Yell,m2Yell)
            else:
                return (self.op,m1Yell,m2Yell)

    def findH(self,op,m1,m2,goalNum = 0):
        m2Num = True if type(m2)==int else False
        m1 = (operator.mod,"h",0) if m1 == "h" else m1
        m2 = (operator.mod,"h",0) if m2 == "h" else m2
        if op == operator.eq:
            return self.findH(m1[0],m1[1],m1[2],m2) if m2Num else self.findH(m2[0],m2[1],m2[2],m1)
        elif op == operator.add:
            return self.findH(m1[0],m1[1],m1[2],goalNum-m2) if m2Num else self.findH(m2[0],m2[1],m2[2],goalNum-m1)
        elif op == operator.sub:
            return self.findH(m1[0],m1[1],m1[2],goalNum+m2) if m2Num else self.findH(m2[0],m2[1],m2[2],m1-goalNum)
        elif op == operator.mul:
            return self.findH(m1[0],m1[1],m1[2],goalNum//m2) if m2Num else self.findH(m2[0],m2[1],m2[2],goalNum//m1)
        elif op == operator.floordiv:
            return self.findH(m1[0],m1[1],m1[2],goalNum*m2) if m2Num else self.findH(m2[0],m2[1],m2[2],m1//goalNum)
        elif op == operator.mod:
            return goalNum

    def __repr__(self) -> str:
        if self.type == "n":
            return "Name: " + self.name + ", Val: " + str(self.num)
        else:
            return "Name: " + self.name + ", Operator: " + str(self.op) + ", Monkey1: " + self.m1 + ", Monkey2: " + self.m2

def Part1(inputName):
    monkeyDict = {}
    with open("Inputs\\" + inputName + "Input.txt") as f:
        Input = [monkeyDict.update({(line.rstrip("\n"))[:4]:monkey(monkeyDict,line.rstrip("\n"),True)}) for line in f]
    return monkeyDict["root"].getYell()

def Part2(inputName):
    monkeyDict = {}
    with open("Inputs\\" + inputName + "Input.txt") as f:
        Input = [monkeyDict.update({(line.rstrip("\n"))[:4]:monkey(monkeyDict,line.rstrip("\n"),False)}) for line in f]
    return monkeyDict["root"].getYell()