import heapq
#please don't read this
#I call it desperate heuristics

def Part1(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        Input = [[ord(c) for c in line.rstrip("\n")] for line in f]
    startPos = (-1,-1)
    endPos = (-1,-1)
    for i in enumerate(Input):
        if i[1].count(83) == 1:
            startPos = (i[0], i[1].index(83))
        if i[1].count(69) == 1:
            endPos = (i[0], i[1].index(69))
            Input[i[0]][i[1].index(69)] = 123
        if startPos != (-1,-1) and endPos != (-1,-1):
            break
    step.boardHeight = len(Input)
    step.boardlength = len(Input[0])
    step.ePos = endPos
    step.Input = Input
    currStep = step(startPos[0], startPos[1], 96, 0)
    visitedSet = set()
    frontier = []
    frontier.append((0,1,currStep))
    i = 1
    while True:
        if len(frontier) == 0:
            return "broke"
        currStep = frontier.pop(0)[2]
        if currStep.getX()==endPos[0] and currStep.getY()==endPos[1]:
            break
        visitedSet.add(str(currStep.getX()) + " " + str(currStep.getY()))
        successors = currStep.getSuccessors(visitedSet)
        for s in successors:
            i+=1
            heapq.heappush(frontier,(s.getEDis()+s.getHeight()*2, i, s))
    print(i)
    return currStep.getSDis()

def Part2(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        Input = [[ord(c) for c in line.rstrip("\n")] for line in f]
    startPos = (-1,-1)
    for i in enumerate(Input):
        if i[1].count(69) == 1:
            startPos = (i[0], i[1].index(69))
            break
    step.boardHeight = len(Input)
    step.boardlength = len(Input[0])
    step.Input = Input
    step.ePos = (-1,-1)
    currStep = step(startPos[0], startPos[1], 123, 0)
    visitedSet = set()
    frontier = []
    frontier.append((0,1,currStep))
    i = 1
    while True:
        if len(frontier) == 0:
            return "broke"
        currStep = frontier.pop(0)[2]
        if Input[currStep.getX()][currStep.getY()] == 97:
            break
        visitedSet.add(str(currStep.getX()) + " " + str(currStep.getY()))
        successors = currStep.getSuccessors(visitedSet,True)
        for s in successors:
            i+=1
            heapq.heappush(frontier,(s.getADis()+s.getHeight()*4, i, s))
    return currStep.getSDis()

class step:
    boardHeight : int
    boardlength : int
    ePos : set
    Input : list[list[int]]
    def __init__(self, x = -1, y = -1, height = 0, sDis = 0) -> None:
        self.x = x
        self.y = y
        self.height = height
        self.sDis = sDis
        self.eDis = self.sDis + (abs(self.x-self.ePos[0]) + abs(self.y-self.ePos[1]))
        self.aDis = self.sDis + self.y

    def inGraph(self, x : int, y : int ):
        return (x > -1 and x < self.boardHeight and y > -1 and y < self.boardlength)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getEDis(self):
        return self.eDis

    def getSDis(self):
        return self.sDis
    
    def getADis(self):
        return self.aDis

    def getHeight(self):
        return self.height

    def getSuccessors(self, visitedSet : set, reverse = False):
        surrounding = [(1,0),(-1,0),(0,1),(0,-1)]
        successors = []
        for pos in surrounding:
            nX = self.x+pos[0]
            nY = self.y+pos[1]
            if nX > -1 and nX < self.boardHeight and nY > -1 and nY < self.boardlength and ((self.height - self.Input[nX][nY] > -2 and reverse == False) or (self.height - self.Input[nX][nY] < 2 and reverse == True)):
                if not (str(nX) + " " + str(nY)) in visitedSet:
                    newStep = step(nX, nY, self.Input[nX][nY], self.sDis+1)
                    successors.append(newStep)
        return successors