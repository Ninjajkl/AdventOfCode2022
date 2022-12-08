def Part1(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        trees = [[int(t) for t in line.rstrip("\n")] for line in f]
    counter = 0
    for treeLine in enumerate(trees):
        for tree in enumerate(treeLine[1]):
            if visibleTree(trees, tree[1], 0, tree[0], treeLine[0]):
                counter += 1
    return counter

def Part2(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        trees = [[int(t) for t in line.rstrip("\n")] for line in f]
    maxTrees = 0
    for treeLine in enumerate(trees):
        for tree in enumerate(treeLine[1]):
            maxTrees = max(maxTrees, numVisibleTree(trees, tree[1], 0, tree[0], treeLine[0]))
    return maxTrees

def visibleTree(treeGrid : list[list[int]], treeHeight : int, direction : int, x : int, y : int):
    if x<0 or y<0 or y>=len(treeGrid) or x>=len(treeGrid[0]):
        return True
    if treeHeight <= treeGrid[y][x] and direction !=0:
        return False
    match direction:
        case 0:
            #starting tree, no direction
            return visibleTree(treeGrid, treeHeight, -1, x-1, y) or visibleTree(treeGrid, treeHeight, -2, x, y-1) or visibleTree(treeGrid, treeHeight, 1, x+1, y) or visibleTree(treeGrid, treeHeight, 2, x, y+1)
        case -1:
            return visibleTree(treeGrid, treeHeight, -1, x-1, y)
        case -2:
            return visibleTree(treeGrid, treeHeight, -2, x, y-1)
        case 1:
            return visibleTree(treeGrid, treeHeight, 1, x+1, y)
        case 2:
            return visibleTree(treeGrid, treeHeight, 2, x, y+1)

def numVisibleTree(treeGrid : list[list[int]], treeHeight : int, direction : int, x : int, y : int):
    numTrees = 0
    if(direction!=0):
        numTrees += 1
    if x<0 or y<0 or y>=len(treeGrid) or x>=len(treeGrid[0]):
        return 0
    if treeHeight <= treeGrid[y][x] and direction !=0:
        return 1
    match direction:
        case 0:
            #starting tree, no direction
            numTrees += numVisibleTree(treeGrid, treeHeight, -1, x-1, y) * numVisibleTree(treeGrid, treeHeight, -2, x, y-1) * numVisibleTree(treeGrid, treeHeight, 1, x+1, y) * numVisibleTree(treeGrid, treeHeight, 2, x, y+1)
        case -1:
            numTrees += numVisibleTree(treeGrid, treeHeight, -1, x-1, y)
        case -2:
            numTrees += numVisibleTree(treeGrid, treeHeight, -2, x, y-1)
        case 1:
            numTrees += numVisibleTree(treeGrid, treeHeight, 1, x+1, y)
        case 2:
            numTrees += numVisibleTree(treeGrid, treeHeight, 2, x, y+1)
    return numTrees