import heapq

def createMap(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        Input = [line.rstrip("\n") for line in f]
    valleyHeight = len(Input)-2
    valleyLength = len(Input[0])-2
    dirDict = {
        '^' : (-1,0),
        'v' : (1,0),
        '<' : (0,-1),
        '>' : (0,1)
    }
    valleyMap = {}
    for r in range(1,len(Input)-1):
        valleyRow = {}
        for c in range(1,len(Input[r])-1):
            if Input[r][c] != ".":
                valleyRow.update({c:[dirDict[Input[r][c]]]})
        if len(valleyRow.keys()) > 0:
            valleyMap.update({r:valleyRow})
    return valleyMap,valleyHeight,valleyLength

def moveBlizz(valleyMap : dict, valleyHeight : int, valleyLength : int):
    newValley = {}
    for k in valleyMap.keys():
        for p in valleyMap[k].keys():
            for blizz in valleyMap[k][p]:
                newPos = ((k+blizz[0]-1)%valleyHeight+1,(p+blizz[1]-1)%valleyLength+1)
                if newPos[0] not in newValley:
                    newValley.update({newPos[0]:{}})
                if newPos[1] not in newValley[newPos[0]]:
                    newValley[newPos[0]].update({newPos[1]:[blizz]})
                else:
                    newValley[newPos[0]].update({newPos[1]:newValley[newPos[0]][newPos[1]]+[blizz]})
    return newValley

def timeToMove(mapDict : dict, valleyHeight : int, valleyLength : int, currMin : int, start, goal) -> int:
    '''
    [0] - manhatt + min from start
    [1] - minute from start
    [2] - r-value
    [3] - c-value
    '''
    successorOptions = [(0,0),(-1,0),(1,0),(0,-1),(0,1)]
    visited = set()
    frontier = [(0,currMin,start[0],start[1])]
    while True:
        if len(frontier) == 0:
            return -1
        curr = heapq.heappop(frontier)
        if curr[2] == goal[0] and curr[3] == goal[1]:
            return curr[1]
        if curr[1]+1 not in mapDict:
            mapDict.update({curr[1]+1:moveBlizz(mapDict[curr[1]],valleyHeight,valleyLength).copy()})
        for i in successorOptions:
            manhattan = abs(curr[2]+i[0]-goal[0]) + abs(curr[3]+i[1]-goal[1])
            newPos = (curr[1]+1+manhattan,curr[1]+1,curr[2]+i[0],curr[3]+i[1])
            if ((newPos[2] not in mapDict[newPos[1]] or newPos[3] not in mapDict[newPos[1]][newPos[2]]) and (1<=newPos[2]<=valleyHeight and 1<=newPos[3]<=valleyLength) and newPos not in visited) or (newPos[2]==goal[0] and newPos[3]==goal[1]) or (newPos[2]==start[0] and newPos[3]==start[1]):
                visited.add(newPos)
                heapq.heappush(frontier,newPos)

def Part1(inputName):
    valleyMap, valleyHeight, valleyLength = createMap(inputName)
    mapDict = {0:valleyMap.copy()}
    start = (0,1)
    goal = (valleyHeight+1,valleyLength)
    return timeToMove(mapDict,valleyHeight,valleyLength,0,start,goal)

def Part2(inputName):
    valleyMap, valleyHeight, valleyLength = createMap(inputName)
    mapDict = {0:valleyMap.copy()}
    start = (0,1)
    goal = (valleyHeight+1,valleyLength)
    startMin = 0
    startMin = timeToMove(mapDict,valleyHeight,valleyLength,startMin,start,goal)
    startMin = timeToMove(mapDict,valleyHeight,valleyLength,startMin,goal,start)
    return timeToMove(mapDict,valleyHeight,valleyLength,startMin,start,goal)