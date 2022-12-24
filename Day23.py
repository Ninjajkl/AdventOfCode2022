def multipleMoveCheck(mapDict : dict, r : int, c : int,currDir : int):
    counter = 0
    directionCheck = [(-1,0),(1,0),(0,-1),(0,1)]
    for d in range(0,4):
        nR = r+directionCheck[(currDir+d)%4][0]
        nC = c+directionCheck[(currDir+d)%4][1]
        if nR not in mapDict or (nC not in mapDict[nR]):
            continue
        if checkNextPos(nR,nC,currDir,mapDict) == (True,r,c):
            counter+=1
        if counter > 1:
            return True
    return False

def checkNextPos(r : int, c : int, currDir : int, mapDict : dict):
    #check if surroundings are empty
    if r-1 not in mapDict or (r-1 in mapDict and c-1 not in mapDict[r-1] and c not in mapDict[r-1] and c+1 not in mapDict[r-1]):
        if c-1 not in mapDict[r] and c+1 not in mapDict[r]:
            if r+1 not in mapDict or (r+1 in mapDict and c-1 not in mapDict[r+1] and c not in mapDict[r+1] and c+1 not in mapDict[r+1]):
                return True,r,c
    directionCheck = [(-1,0),(1,0),(0,-1),(0,1)]
    for d in range(0,4):
        nR = r+directionCheck[(currDir+d)%4][0]
        nC = c+directionCheck[(currDir+d)%4][1]
        clear = False
        if directionCheck[(currDir+d)%4][0] != 0:
            if nR not in mapDict or (nR in mapDict and nC-1 not in mapDict[nR] and nC not in mapDict[nR] and nC+1 not in mapDict[nR]):
                clear = True
        else:
            if (nR-1 not in mapDict or nC not in mapDict[nR-1]) and (nR not in mapDict or nC not in mapDict[nR]) and (nR+1 not in mapDict or nC not in mapDict[nR+1]):
                clear = True
        if clear:
            return clear, nR, nC
    return clear, nR, nC

def main(inputName, Part1 : bool):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        Input = [line.rstrip("\n") for line in f]
    mapDict = {}
    for r, line in enumerate(Input):
        lineDict = {}
        for c, pos in enumerate(line):
            if pos == "#":
                lineDict.update({c:0})
        if not lineDict == {}:
            mapDict.update({r:lineDict})
    currDir = 0
    for i in range(1,100000):
        newMapDict = {}
        for r in mapDict.keys():
            for c in mapDict[r]:
                clear, nR, nC = checkNextPos(r,c,currDir,mapDict)
                if not clear or multipleMoveCheck(mapDict,nR,nC,currDir):
                    nR = r
                    nC = c
                if nR not in newMapDict:
                    newMapDict.update({nR:{}})
                newMapDict[nR].update({nC:0})
        currDir = (currDir+1)%4
        if not Part1 and mapDict == newMapDict:
            return i
        mapDict = newMapDict
        if Part1 and i == 10: break
    rMin = min(mapDict.keys())
    rMax = max(mapDict.keys())+1
    cMin = min([min(mapDict[k].keys()) for k in mapDict.keys()])
    cMax = max([max(mapDict[k].keys()) for k in mapDict.keys()])+1
    return (rMax-rMin) * (cMax-cMin) - sum([len(mapDict[k].keys()) for k in mapDict.keys()])

def Part1(inputName):
    return main(inputName,True)
                    
def Part2(inputName):
    return main(inputName,False)