playDict = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

def Part1(inputName):
    textFile = open("Inputs\\" + inputName + "Input.txt", "r")
    RawInput = textFile.readlines()
    convertedList = [[""]]
    convertedList.pop()
    Sum = 0
    for line in RawInput:
        convertedList.append(line.replace("\n", "").split(" "))
    for line in convertedList:
        Sum += getValue(playDict[line[0]], playDict[line[1]])
    return Sum

def getValue(o : int, y: int):
    match o-y:
        case 0:
            return y+3
        case 1:
            return y
        case -2:
            return y
        case -1:
            return y+6
        case 2:
            return y+6
    return -1

def Part2(inputName):
    textFile = open("Inputs\\" + inputName + "Input.txt", "r")
    RawInput = textFile.readlines()
    convertedList = [[""]]
    convertedList.pop()
    Sum = 0
    for line in RawInput:
        convertedList.append(line.replace("\n", "").split(" "))
    for line in convertedList:
        playerMove = 0
        match playDict[line[1]]:
            case 1:
                playerMove = playDict[line[0]]-1
                if playerMove == 0:
                    playerMove = 3
            case 2:
                playerMove = playDict[line[0]]
            case 3:
                playerMove = playDict[line[0]]+1
                if playerMove == 4:
                    playerMove = 1
        Sum += getValue(playDict[line[0]],playerMove)
    return Sum

        