import re

def findMaxGeodes(blueprint : list[int], t = [0,1,0,0,0,0,0,0], currMin = 0, maxMin = 24, notBuilt = [False,False,False,False]):
    ''' blueprint guide
    bp[0] is num ore for a ore robot
    bp[1] is num ore for a clay robot
    bp[2] is num ore for an obsidian robot
    bp[3] is num clay for an obsidian robot
    bp[4] is num ore for a geode robot
    bp[5] is num obsidian for a geode robot
    '''
    ''' tracker guide
    t[0] is num ore
    t[1] is num ore Robots
    t[2] is num clay
    t[3] is num clay Robots
    t[4] is num obsidian
    t[5] is num obsidian Robots
    t[6] is num geodes
    t[7] is num geodes Robots
    '''
    #return if out of time, or if ore/clay gets to crazy levels
    if currMin >= maxMin or t[0] >=20 or t[2] >= 80:
        return t[6]
    canBuildOre = True if blueprint[0] <= t[0] else False
    canBuildClay = True if blueprint[1] <= t[0] else False
    canBuildObsidian = True if blueprint[2] <= t[0] and blueprint[3] <= t[2] else False
    canBuildGeodes = True if blueprint[4] <= t[0] and blueprint[5] <= t[4] else False
    maxGeodes = t[6]
    #Assumes that Geodes should always be build when possible
    #Otherwise, always try to build Obsidian when possible
    if canBuildGeodes:
        maxGeodes = max(maxGeodes,findMaxGeodes(blueprint,[t[0]+t[1]-blueprint[4],t[1],t[2]+t[3],t[3],t[4]+t[5]-blueprint[5],t[5],t[6]+t[7],t[7]+1],currMin+1,maxMin))
    else:
        if canBuildObsidian:
            maxGeodes = max(maxGeodes,findMaxGeodes(blueprint,[t[0]+t[1]-blueprint[2],t[1],t[2]+t[3]-blueprint[3],t[3],t[4]+t[5],t[5]+1,t[6]+t[7],t[7]],currMin+1,maxMin))
        else:
            maxGeodes = max(maxGeodes,findMaxGeodes(blueprint,[t[0]+t[1],t[1],t[2]+t[3],t[3],t[4]+t[5],t[5],t[6]+t[7],t[7]],currMin+1,maxMin, [canBuildOre,canBuildClay,canBuildObsidian,canBuildGeodes]))
            if canBuildOre and not notBuilt[0]:
                maxGeodes = max(maxGeodes,findMaxGeodes(blueprint,[t[0]+t[1]-blueprint[0],t[1]+1,t[2]+t[3],t[3],t[4]+t[5],t[5],t[6]+t[7],t[7]],currMin+1,maxMin))
            if canBuildClay and not notBuilt[1]:
                maxGeodes = max(maxGeodes,findMaxGeodes(blueprint,[t[0]+t[1]-blueprint[1],t[1],t[2]+t[3],t[3]+1,t[4]+t[5],t[5],t[6]+t[7],t[7]],currMin+1,maxMin))
    return maxGeodes

def Part1(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        Input = [list(map(int, re.findall('\d+',line[13:]))) for line in f]
    totalQuality = 0
    for i, line in enumerate(Input):
        totalQuality += (i+1)*findMaxGeodes(line)
    return totalQuality

def Part2(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        Input = [list(map(int, re.findall('\d+',line[13:]))) for line in f]
    return findMaxGeodes(Input[0], [0,1,0,0,0,0,0,0], 0, 32) * findMaxGeodes(Input[1], [0,1,0,0,0,0,0,0], 0, 32) * findMaxGeodes(Input[2], [0,1,0,0,0,0,0,0], 0, 32)