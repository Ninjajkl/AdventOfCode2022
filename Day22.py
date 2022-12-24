import re


class mapRegion:
    def __init__(self, fullMap, regionsize, sR, sC) -> None:
        self.regionSize = regionsize
        self.sPos = (sR,sC)
        self.regionArea = []
        for r in range(sR,sR+regionsize):
            rowArea = []
            for c in range(sC, sC+regionsize):
                rowArea.append(fullMap[r][c])
            self.regionArea.append(rowArea)
        '''
        regionGuide[0] = region on right face
        regionGuide[1] = region on bottom face
        regionGuide[2] = region on left face
        regionGuide[3] = region on top face
        regionGuide[4] = region on front face (always self)
        regionGuide[5] = region on back face
        '''
        self.regionGuide = [(-1,None),(-1,None),(-1,None),(-1,None),(0,self),(-1,None)]

    def updateRegionGuide(self, givenRG : list, relativeRegionPos : int):
        #used to check if a change occured, if not, stop to prevent a loop
        #print(self)
        if abs(self.sPos[0]-givenRG[4][1].sPos[0]) + abs(self.sPos[1]-givenRG[4][1].sPos[1]) > self.regionSize:
            return
        match relativeRegionPos:
            case 0:
                self.regionGuide[0] = ((givenRG[5][0]+2)%4,givenRG[5][1])
                self.regionGuide[1] = ((givenRG[1][0]+1)%4,givenRG[1][1])
                self.regionGuide[2] = givenRG[4]
                self.regionGuide[3] = ((givenRG[3][0]-1)%4,givenRG[3][1])
                self.regionGuide[5] = ((givenRG[2][0]+2)%4,givenRG[2][1])
            case 1:
                self.regionGuide[0] = ((givenRG[0][0]-1)%4,givenRG[0][1])
                self.regionGuide[1] = givenRG[5]
                self.regionGuide[2] = ((givenRG[2][0]+1)%4,givenRG[2][1])
                self.regionGuide[3] = givenRG[4]
                self.regionGuide[5] = givenRG[3]
            case 2:
                self.regionGuide[0] = givenRG[4]
                self.regionGuide[1] = ((givenRG[1][0]-1)%4,givenRG[1][1])
                self.regionGuide[2] = ((givenRG[5][0]+2)%4,givenRG[5][1])
                self.regionGuide[3] = ((givenRG[3][0]+1)%4,givenRG[3][1])
                self.regionGuide[5] = ((givenRG[0][0]+2)%4,givenRG[0][1])
            case 3:
                self.regionGuide[0] = ((givenRG[0][0]+1)%4,givenRG[0][1])
                self.regionGuide[1] = givenRG[4]
                self.regionGuide[2] = ((givenRG[2][0]-1)%4,givenRG[2][1])
                self.regionGuide[3] = givenRG[5]
                self.regionGuide[5] = givenRG[1]
        for i, nextRegion in enumerate(self.regionGuide):
            if nextRegion[1] is not None and i != 4 and nextRegion[1] is not givenRG[4][1]:
                noneCounter = 0
                for j in nextRegion[1].regionGuide:
                    if None in j:
                        noneCounter = 1
                        break
                if noneCounter != 0:
                    nextRegion[1].updateRegionGuide(self.regionGuide, i)

    def __repr__(self) -> str:
        stringBuilder = str(self.sPos) + " ["
        for i in self.regionGuide:
            if i[1] is None:
                stringBuilder += "(-1,N), "
                continue
            stringBuilder += "("+ str(i[0]) + "," + str(i[1].sPos) + "), "
        stringBuilder += "]"
        return stringBuilder

def setRegionGuide(mapDir: dict, reg: mapRegion, prevVisited = set()):
    prevVisited.add(reg.sPos)
    frontier = []
    for k in mapDir.keys():
        if k != reg.sPos and k not in prevVisited and ((k[0] == reg.sPos[0] and abs(k[1]-reg.sPos[1])==reg.regionSize) or (k[1] == reg.sPos[1]and abs(k[0]-reg.sPos[0])==reg.regionSize)):
            prevVisited.add(k)
            frontier.append(k)
    for j in [mapDir[l] for l in frontier]:
        #finds relative position
        if j.sPos[0] == reg.sPos[0]:
            if j.sPos[1] < reg.sPos[1]:
                reg.regionGuide[2] = (0,j)
            else:
                reg.regionGuide[0] = (0,j)
        elif j.sPos[1] == reg.sPos[1]:
            if j.sPos[0] < reg.sPos[0]:
                reg.regionGuide[3] = (0,j)
            else:
                reg.regionGuide[1] = (0,j)
        reg.updateRegionGuide(reg.regionGuide,4)
        #for k in mapDir.keys():
        #    print(mapDir[k])
        #print()
        setRegionGuide(mapDir,j,prevVisited)
    return

def Part1(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        Input = [line.rstrip("\n") for line in f]
        RawMap = Input[:-2]
        Instructions = re.split("(\D)",Input[-1])
    mapDict = {}
    for i in range(0,len(RawMap)):
        lineDict = {}
        for j in range(0,len(RawMap[i])):
            if RawMap[i][j] != " ":
                lineDict.update({j+1:RawMap[i][j]})
        mapDict.update({i+1:lineDict})
    #for k in mapDict.keys():
    #    print(k, mapDict[k])
    #print(Instructions)
    degDict = {
        0 : (0,1),
        1 : (1,0),
        2 : (0,-1),
        3 : (-1,0)
    }
    deg = 0
    pos = (min(mapDict.keys()),min(mapDict[min(mapDict.keys())].keys()))
    #print(pos)
    for instr in Instructions:
        if not instr.isdigit(): deg = (deg+1)%4 if instr == "R" else (deg-1)%4
        else:
            for i in range(0,int(instr)):
                nextPos = (pos[0]+degDict[deg][0],pos[1]+degDict[deg][1])
                if degDict[deg][1] == 0 and (nextPos[0] not in mapDict or nextPos[1] not in mapDict[nextPos[0]]):
                    nextPos = (min([k for k in mapDict.keys() if nextPos[1] in mapDict[k]]),nextPos[1]) if deg == 1 else (max([k for k in mapDict.keys() if nextPos[1] in mapDict[k]]),nextPos[1])
                elif degDict[deg][0] == 0 and nextPos[1] not in mapDict[nextPos[0]]:
                    nextPos = (nextPos[0],min(mapDict[nextPos[0]].keys())) if deg == 0 else (nextPos[0],max(mapDict[nextPos[0]].keys()))
                if nextPos[0] in mapDict and mapDict[nextPos[0]][nextPos[1]] == ".":
                    pos = nextPos
                else:
                    break
                #print(pos)
    return pos[0]*1000 + pos[1]*4+deg

def Part2(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        Input = [line.rstrip("\n") for line in f]
        RawMap = Input[:-2]
        Instructions = re.split("(\D)",Input[-1])
    mapDir = {}
    regionSize = 50
    for r in range(0,len(RawMap)//regionSize):
        for c in range(0, len(RawMap[r*regionSize])//regionSize):
            if not RawMap[r*regionSize][c*regionSize] == " ":
                mapDir.update({(r*regionSize,c*regionSize): mapRegion(RawMap,regionSize,r*regionSize,c*regionSize)})
    setRegionGuide(mapDir,mapDir[list(mapDir.keys())[0]])
    #for k in mapDir.keys():
    #    print(mapDir[k])
    #print(Instructions)
    degDict = {
        0 : (0,1),
        1 : (1,0),
        2 : (0,-1),
        3 : (-1,0)
    }
    deg = 0
    currReg = mapDir[list(mapDir.keys())[0]]
    pos = (0,0)
    #print((pos[0]+currReg.sPos[0]+1,pos[1]+currReg.sPos[1]+1))
    for instr in Instructions:
        if not instr.isdigit(): deg = (deg+1)%4 if instr == "R" else (deg-1)%4
        else:
            for i in range(0,int(instr)):
                nextPos = (pos[0]+degDict[deg][0],pos[1]+degDict[deg][1])
                tReg = currReg
                tDeg = 0
                #print((pos[0]+currReg.sPos[0]+1,pos[1]+currReg.sPos[1]+1))
                if nextPos[0] >= regionSize:
                    tReg = currReg.regionGuide[1][1]
                    tDeg = currReg.regionGuide[1][0]
                    match tDeg:
                        case 0: nextPos = (0,pos[1])
                        case 1: nextPos = (pos[1],pos[0])
                        case 2: nextPos = (pos[0],regionSize-1-pos[1])
                        case 3: nextPos = (regionSize-1-pos[1],0)
                elif nextPos[0] < 0:
                    tReg = currReg.regionGuide[3][1]
                    tDeg = currReg.regionGuide[3][0]
                    match tDeg:
                        case 0: nextPos = (regionSize-1,pos[1])
                        case 1: nextPos = (pos[1],pos[0])
                        case 2: nextPos = (regionSize-1,regionSize-1-pos[1])
                        case 3: nextPos = (regionSize-1-pos[1],regionSize-1)
                elif nextPos[1] >= regionSize:
                    tReg = currReg.regionGuide[0][1]
                    tDeg = currReg.regionGuide[0][0]
                    match tDeg:
                        case 0: nextPos = (pos[0],0)
                        case 1: nextPos = (0,regionSize-1-pos[0])
                        case 2: nextPos = (regionSize-1-pos[0],regionSize-1)
                        case 3: nextPos = (pos[1],pos[0])
                elif nextPos[1] < 0:
                    tReg = currReg.regionGuide[2][1]
                    tDeg = currReg.regionGuide[2][0]
                    match tDeg:
                        case 0: nextPos = (pos[0],regionSize-1)
                        case 1: nextPos = (regionSize-1,regionSize-1-pos[0])
                        case 2: nextPos = (regionSize-1-pos[0],0)
                        case 3: nextPos = (0,pos[0])
                if 0 <= nextPos[0] < regionSize and 0 <= nextPos[1] < regionSize and tReg.regionArea[nextPos[0]][nextPos[1]] != "#":
                    currReg = tReg
                    deg = (deg + tDeg)%4
                    pos = nextPos
                    continue
                else: 
                    break
    pos = ((pos[0]+currReg.sPos[0]+1,pos[1]+currReg.sPos[1]+1))
    return pos[0]*1000 + pos[1]*4+deg