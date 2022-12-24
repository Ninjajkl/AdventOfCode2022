import math

def move(boardDict,rock,topPos,leftPos):
    for i in range(len(rock)):
        if topPos-i < 0:
            return False
        for j in range(len(rock[0])):
            if leftPos + j < 0 or leftPos+ j >= 7 or (topPos - i in boardDict and leftPos + j in boardDict[topPos-i] and rock[i][j] =="#"):
                return False
    return True

def RockFall(jetSeq,currJetSeq,boardDict,rockTypes,currRockType):
    rock = rockTypes[currRockType]
    boardHighest = max(boardDict.keys())
    topPos = boardHighest+len(rock)+3
    leftPos = 2
    while True:
        jet = jetSeq[currJetSeq[0]]
        currJetSeq[0] = (currJetSeq[0]+1)%len(jetSeq)
        jetChange = 1 if jet == '>' else -1
        if move(boardDict,rock,topPos,leftPos + jetChange): leftPos += jetChange
        if move(boardDict,rock,topPos-1,leftPos): topPos -= 1
        else:
            for i in range(len(rock)):
                for j in range(len(rock[0])):
                    if rock[i][j] == '#':
                        if not topPos-i in boardDict:
                            boardDict.update({topPos-i:set()})
                        boardDict[topPos-i].add(leftPos+j)
            break

def Part1(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        jetSeq = f.readline().rstrip('\n')
    currJetSeq = [0]
    boardDict = {-1:set()}
    rockTypes = [["####"],[".#.","###",".#."],["..#","..#","###"],["#","#","#","#"],["##","##"]]
    currRockType = 0
    for i in range(2022):
        RockFall(jetSeq,currJetSeq,boardDict,rockTypes,currRockType)
        currRockType = (currRockType+1)%5
    return max(boardDict.keys())+1

def Part2(inputName):
    if inputName == "Test":
        return "The test input doesn't work for my method"
    with open("Inputs\\" + inputName + "Input.txt") as f:
        jetSeq = f.readline().rstrip('\n')
    currJetSeq = [0]
    boardDict = {-1:set()}
    rockTypes = [["####"],[".#.","###",".#."],["..#","..#","###"],["#","#","#","#"],["##","##"]]
    currRockType = 0
    #Finding where the top is full and causes a cycle to start
    repJetSeqPos,repRockTypePos = 0,0
    #Height will be in form aX + C, where a is the number of cycles
    heightC,heightX = 0,0
    #Num Rocks dropped will also be in form aX+C
    droppedC,droppedX = 0,0

    fullTops = set()

    for i in range(10000):
        RockFall(jetSeq,currJetSeq,boardDict,rockTypes,currRockType)
        currRockType = (currRockType+1)%5
        if(len(boardDict[max(boardDict.keys())])==7):
            if len(fullTops) == 0:
                fullTops.add((currJetSeq[0],currRockType))
                #print("jetPos, rockPos:",(currJetSeq[0],currRockType))
                #print("height:",max(boardDict.keys()))
                #print("rocks dropped:",i)
                continue
            if fullTops.__contains__((currJetSeq[0],currRockType)):
                #print("jetPos, rockPos:",(currJetSeq[0],currRockType))
                #print("height:",max(boardDict.keys()))
                #print("rocks dropped:",i)
                repJetSeqPos = currJetSeq[0]
                repRockTypePos = currRockType
                if heightC == 0:
                    heightC = heightX = max(boardDict.keys())
                    droppedC = droppedX = i
                else:
                    heightX = max(boardDict.keys())-heightX
                    heightC = heightC-heightX
                    droppedX = i - droppedX
                    droppedC = droppedC-droppedX
                    break
    #print("jetPos, rockPos:",(repJetSeqPos,repRockTypePos))
    #print("height: a" + str(heightX) + "+" + str(heightC))
    #print("rocks dropped: a"+ str(droppedX) + "+" + str(droppedC))

    numCycles = math.floor((1000000000000-droppedC)/droppedX)
    #print("numCycles",numCycles)

    totalHeight = numCycles*heightX+heightC
    #print("totalHeight",totalHeight)
    boardDict.clear()
    boardDict = {totalHeight:{0,1,2,3,4,5,6}}
    currJetSeq[0] = repJetSeqPos
    currRockType = repRockTypePos
    for i in range(numCycles*droppedX+droppedC, 1000000000000):
        RockFall(jetSeq,currJetSeq,boardDict,rockTypes,currRockType)
        currRockType = (currRockType+1)%5
    return max(boardDict.keys())
