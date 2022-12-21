import heapq
import re

def interpretInput(inputName):
    value.tunnelPages = {}
    with open("Inputs\\" + inputName + "Input.txt") as f:
        Input = [line.rstrip("\n") for line in f]
        for line in Input:
            newValue = value()
            newValue.setName(line[6:8])
            newValue.setFlowRate(list(map(int, re.findall('\d+',line)))[0])
            tunnelIndex = line.find("valve")+6
            if len(line[tunnelIndex:]) == 2:
                newValue.addTunnel(line[tunnelIndex:])
            else:
                newValue.addTunnels(line[tunnelIndex+1:].replace(",","").split())
            value.tunnelPages.update({newValue.name:newValue})
    for v in value.tunnelPages.values():
        v.calculateDist()

class value:
    tunnelPages = {}

    def __init__(self) -> None:
        self.name = ""
        self.flowRate = -1
        self.tunnels = []
        self.distanceDict = {}

    def setName(self, name : str) -> None:
        self.name = name
    
    def setFlowRate(self, flowRate : int) -> None:
        self.flowRate = flowRate

    def addTunnel(self, tunnel : str) -> None:
        self.tunnels.append(tunnel)

    def addTunnels(self, tunnels : list[str]) -> None:
        for tunnel in tunnels:
            self.tunnels.append(tunnel)

    def calculateDist(self):
        if self.flowRate == 0 and self.name !="AA":
            return
        visitedTunnels = set()
        visitedTunnels.add(self.name)
        frontier = [(0,0,self)]
        i=0
        while len(frontier) != 0:
            currTunnel = frontier.pop(0)
            visitedTunnels.add(currTunnel)
            if currTunnel[2].flowRate != 0 and currTunnel[0] != 0:
                self.distanceDict.update({currTunnel[2]:currTunnel[0]})
            for tunnel in currTunnel[2].tunnels:
                if not tunnel in visitedTunnels:
                    heapq.heappush(frontier,(currTunnel[0]+1,i,self.tunnelPages[tunnel]))
                    visitedTunnels.add(tunnel)
                    i+=1

    def findPressure(self, timeLimit = 30, eValves = [], time = 0):
        if time >= timeLimit: return 0
        enabledValves = eValves + [self]
        pressure = self.flowRate * (timeLimit-time)
        if len(enabledValves) == len(self.distanceDict)+2:
            return pressure
        #otherPressure = max([other.findPressure(timeLimit,enabledValves,time+1+self.distanceDict[other]) for other in self.distanceDict if other not in enabledValves])
        otherPressure = 0
        for other in self.distanceDict:
            if other not in enabledValves:
                otherPressure = max(otherPressure,other.findPressure(timeLimit,enabledValves,time+1+self.distanceDict[other]))
        return pressure + otherPressure

    #First attempt at part2. This takes about 45 mins, but does work.
    #Tries to find the best possible path of two simultanious walkers, but takes exponentially longer than one
    def findElephantPressure(v, elephant = None, timeLimit = 26, eValves = [], time = 0, eTime = 0):
        if time >= timeLimit: return elephant.findPressure(timeLimit,eValves,eTime)
        elif eTime >= timeLimit: return v.findPressure(timeLimit,eValves,time)
        enabledValves = eValves + [v] if v.name == "AA" else eValves + [v] + [elephant]
        pressure = v.flowRate * (timeLimit-time)
        ePressure = elephant.flowRate * (timeLimit-eTime)
        if len(enabledValves) >= len(v.distanceDict)+1:
            return pressure + ePressure
        otherPressure = 0
        for other in v.distanceDict:
            if other not in enabledValves:
                for eOther in elephant.distanceDict:
                    if eOther not in enabledValves and eOther is not other:
                        otherPressure = max(otherPressure,other.findElephantPressure(eOther,timeLimit,enabledValves,time+1+v.distanceDict[other],eTime+1+elephant.distanceDict[eOther]))
        return pressure + ePressure + otherPressure

    #I realized I already searched every possible path with findPressure
    #I just need to add all of the "good" paths into a list
    #Then, I search though the list and find the two highest values that had no shared paths
    def findPressure2(self,pathList, timeLimit = 26, eValves = [], time = 0):
        if time >= timeLimit: return 0
        enabledValves = eValves + [self]
        pressure = self.flowRate * (timeLimit-time)
        if len(enabledValves) == len(self.distanceDict)+2:
            return pressure
        #otherPressure = max([other.findPressure(timeLimit,enabledValves,time+1+self.distanceDict[other]) for other in self.distanceDict if other not in enabledValves])
        otherPressure = 0
        for other in self.distanceDict:
            if other not in enabledValves:
                otherPressure = max(otherPressure,pathList,other.findPressure2(timeLimit,enabledValves,time+1+self.distanceDict[other]))
        return pressure + otherPressure

    def __str__(self) -> str:
        return(self.name + " " + str(self.flowRate))

def Part1(inputName):
    interpretInput(inputName)
    return value.findPressure(value.tunnelPages["AA"])

def Part2(inputName):
    return
    interpretInput(inputName)
    return value.findPressure2(value.tunnelPages["AA"],[])
    #call original solution
    #return value.tunnelPages["AA"].findElephantPressure(value.tunnelPages["AA"],26)
#print(Part1("Test"))
#print(Part1("Day16"))
#print(Part2("Test"))
#print(Part2("Day16"))