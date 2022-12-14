def Part1(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        rocksDir = rockFormer([line.rstrip("\n").replace(" ", "").replace("-", "") for line in f])
    # [0] = leftLim, [1] = rightLim, [2] = downLim
    limits = (min(rocksDir.keys()),max(rocksDir.keys()),max(max(value) for value in rocksDir.values()))
    sandPoint = (500, 0)
    sandCounter = 0
    while True:
        if moveSand(rocksDir, sandPoint, limits, False) != -1:
            sandCounter +=1
        else:
            return sandCounter

def Part2(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        rocksDir = rockFormer([line.rstrip("\n").replace(" ", "").replace("-", "") for line in f])
    # [0] = leftLim, [1] = rightLim, [2] = downLim
    limits = (min(rocksDir.keys()),max(rocksDir.keys()),max(max(value) for value in rocksDir.values())+2)
    for rock in rocksDir:
        rocksDir[rock].add(limits[2])
    sandPoint = (500, 0)
    sandCounter = 0
    while True:
        if moveSand(rocksDir, sandPoint, limits, True) != -1:
            sandCounter +=1
        else:
            return sandCounter + 1

def rockFormer(Input : list[str]):
    rockDir = {}
    for line in Input:
        p1 = [-1,-1]
        p2 = [-1,-1]
        intBuilder = ""
        for i, c in enumerate(line):
            if ord(c)>=48 and ord(c) <=57:
                intBuilder += c
            if c == ",":
                if p1[0] == -1: p1[0] = int(intBuilder)
                else: p2[0] = int(intBuilder)
                intBuilder = ""
                continue
            if c == ">" or i == len(line)-1:
                if p1[1] == -1: p1[1] = int(intBuilder)
                else: p2[1] = int(intBuilder)
                intBuilder = ""
                if p2[0] == -1: continue
                for j in range(p1[0], p2[0]+(1 if p1[0]<p2[0] else -1), 1 if p1[0]<p2[0] else -1):
                    if not j in rockDir:
                        rockDir.update({j:set()})
                    for k in range(p1[1], p2[1]+(1 if p1[1]<p2[1] else -1), 1 if p1[1]<p2[1] else -1):
                        rockDir[j].add(k)
                p1[0] = p2[0]
                p1[1] = p2[1]
    return rockDir

def moveSand(rocksDir : dir, sandLoc : tuple[int,int], limits : tuple[int,int,int], floorMode : bool):
    #checks if sand is in abyss
    if not floorMode and (sandLoc[1] >= limits[2] or not sandLoc[0] in rocksDir): return -1
    #0 is directly below, -1 is down 1 left 1, and 1 is down 1 right 1
    checkList = [0,-1,1]
    for i in checkList:
        if not sandLoc[0]+i in rocksDir: 
            if not floorMode: return -1
            rocksDir.update({sandLoc[0]+i:{limits[2]}})
        if not sandLoc[1]+1 in rocksDir[sandLoc[0]+i]:
            return moveSand(rocksDir, [sandLoc[0]+i,sandLoc[1]+1], limits, floorMode)
    if floorMode and sandLoc == (500,0): return -1
    rocksDir[sandLoc[0]].add(sandLoc[1])
    return 0
