def Part1(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        RawInput = [line.rstrip("\n") for line in f]
    return findMarker(4, RawInput[0])

def Part2(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        RawInput = [line.rstrip("\n") for line in f]
    return findMarker(14, RawInput[0])

def findMarker(length : int, Input):
    visitedChars = [Input[0]]
    for i in range(1, len(Input)):
        visitedChars.append(Input[i])
        if i >= length-1:
            if(NoDuplicates(visitedChars)):
                return i+1
            visitedChars.pop(0)
    return -1

def NoDuplicates(visitedChars):
    for i in range(0, len(visitedChars)-1):
        for j in range(i+1, len(visitedChars)):
            if(visitedChars[i] == visitedChars[j]):
                return False
    return True