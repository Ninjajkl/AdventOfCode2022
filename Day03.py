priDict = {}

def CreateDict():
    for i in range(1,27):
        priDict.update({chr(i+96) : i})
    for i in range(1,27):
        priDict.update({chr(i+64) : i+26})

def CompareHalves(str1 : str, str2 : str):
    for c in str1:
        if(str2.find(c) != -1):
            return c

def Part1(inputName):
    textFile = open("Inputs\\" + inputName + "Input.txt", "r")
    RawInput = textFile.readlines()
    CreateDict()
    count = 0
    for line in RawInput:
        count += priDict[CompareHalves(line[:len(line)//2], line[len(line)//2:])]
    return count

def Part2(inputName):
    textFile = open("Inputs\\" + inputName + "Input.txt", "r")
    RawInput = textFile.readlines()
    convertedList = []
    for line in RawInput:
        convertedList.append(line.replace("\n", ""))
    CreateDict()
    count = 0
    group = []
    visitedChar = []
    for line in convertedList:
        group.append(line)
        if len(group) == 3:
            for c in group[0]:
                if group[1].find(c) != -1 and group[2].find(c) != -1:
                    count += priDict[c]
                    group.clear()
                    break
    return count

                    