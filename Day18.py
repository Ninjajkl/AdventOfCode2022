def calcTotalSurfaceArea(cubeWorld : dict, cubeList : list[list[int]]):
    totalSurface = 0
    for cube in cubeList:
        if cube[0] not in cubeWorld:
            cubeWorld.update({cube[0]:{}})
        if cube[1] not in cubeWorld[cube[0]]:
            cubeWorld[cube[0]].update({cube[1]:set()})
        if cube[2] not in cubeWorld[cube[0]][cube[1]]:
            cubeWorld[cube[0]][cube[1]].add(cube[2])
        sidesChanged = 6
        surrCubes = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
        for sCube in surrCubes:
            if (cube[0]+sCube[0]) not in cubeWorld or (cube[1]+sCube[1]) not in cubeWorld[cube[0]+sCube[0]] or (cube[2]+sCube[2]) not in cubeWorld[cube[0]+sCube[0]][(cube[1]+sCube[1])]:
                continue
            sidesChanged -= 2
        totalSurface += sidesChanged
    return totalSurface

def calcOutterSurfaceArea(cubeWorld : dict, cubeList : list[list[int]]):
    lb = ub = (cubeList[0][0],cubeList[0][1],cubeList[0][2])
    for cube in cubeList:
        lb = (min(lb[0],cube[0]-1),min(lb[1],cube[1]-1),min(lb[2],cube[2]-1))
        ub = (max(ub[0],cube[0]+1),max(ub[1],cube[1]+1),max(ub[2],cube[2]+1))
        if cube[0] not in cubeWorld:
            cubeWorld.update({cube[0]:{}})
        if cube[1] not in cubeWorld[cube[0]]:
            cubeWorld[cube[0]].update({cube[1]:set()})
        if cube[2] not in cubeWorld[cube[0]][cube[1]]:
            cubeWorld[cube[0]][cube[1]].add(cube[2])
    totalSurface = 0
    surrCubes = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    visitedPoints = set()
    frontier = [lb]
    while True:
        if len(frontier) == 0:
            return totalSurface
        cCube = frontier.pop()
        for sCube in surrCubes:
            if cCube[0]+sCube[0] < lb[0] or cCube[1]+sCube[1] < lb[1] or cCube[2]+sCube[2] < lb[2] or cCube[0]+sCube[0] > ub[0] or cCube[1]+sCube[1] > ub[1] or cCube[2]+sCube[2] > ub[2]:
                continue
            if (cCube[0]+sCube[0]) not in cubeWorld or cCube[1]+sCube[1] not in cubeWorld[cCube[0]+sCube[0]] or cCube[2]+sCube[2] not in cubeWorld[cCube[0]+sCube[0]][cCube[1]+sCube[1]]:
                if (cCube[0]+sCube[0],cCube[1]+sCube[1],cCube[2]+sCube[2]) not in visitedPoints:
                    frontier.append((cCube[0]+sCube[0],cCube[1]+sCube[1],cCube[2]+sCube[2]))
                    visitedPoints.add((cCube[0]+sCube[0],cCube[1]+sCube[1],cCube[2]+sCube[2]))
            else: totalSurface+=1

def Part1(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        Input = [[int(numlist) for numlist in line.rstrip("\n").split(",")] for line in f]
    cubeWorld = {}
    return calcTotalSurfaceArea(cubeWorld,Input)

def Part2(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        Input = [[int(numlist) for numlist in line.rstrip("\n").split(",")] for line in f]
    cubeWorld = {}
    return calcOutterSurfaceArea(cubeWorld,Input)