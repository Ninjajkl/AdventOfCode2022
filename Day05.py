import collections

cargoStack = [[str]]
instructions = []

def InterpretInput(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        RawInput = [line.rstrip("\n") for line in f]
    cargoStack.clear()
    cargoStack.append([])
    instructions.clear()
    onInstructions = False
    currInstruction = 0
    for line in RawInput:
        if not onInstructions:
            if len(line) == 0:
                onInstructions = True
                continue
            for i in range(0, len(line)):
                c = line[i]
                if c != '[' and c != ']' and c != ' ' and ord(c) > 57:
                    index = i%4 + round(i/4)
                    while len(cargoStack) <= index:
                        cargoStack.append([])
                    cargoStack[index].insert(0,c)
        else:
            numBuilder = ""
            instructions.append([])
            for i in range(0,len(line)):
                n = line[i]
                if ord(n) >= 48 and ord(n) <= 57:
                    numBuilder += n
                if n == ' ' or i == len(line)-1:
                    if len(numBuilder) !=0:
                        instructions[currInstruction].append(int(numBuilder))
                        numBuilder = ""
            currInstruction += 1
    

def Part1(inputName):
    InterpretInput(inputName)
    for i in range(0, len(instructions)):
        for j in range(0, instructions[i][0]):
            cargoStack[instructions[i][2]].append(cargoStack[instructions[i][1]].pop())
    cargoStack.pop(0)
    topBuilder = ""
    for stack in cargoStack:
        topBuilder += stack[len(stack)-1]
    return topBuilder

def Part2(inputName):
    InterpretInput(inputName)
    for i in range(0, len(instructions)):
        cargoEnd = len(cargoStack[instructions[i][2]])
        for j in range(0, instructions[i][0]):
            cargoStack[instructions[i][2]].insert(cargoEnd, cargoStack[instructions[i][1]].pop())
    cargoStack.pop(0)
    topBuilder = ""
    for stack in cargoStack:
        topBuilder += stack[len(stack)-1]
    return topBuilder