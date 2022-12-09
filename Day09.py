def Part1(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        Input = [line.rstrip("\n").split() for line in f]
    return tailTravel(2, Input)

def Part2(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        Input = [line.rstrip("\n").split() for line in f]
    return tailTravel(10, Input)

def tailTravel(numKnots: int, Input : list[list[str]]):
    visitedSet = {"0 0"}
    knots = [[0,0] for x in range(numKnots)]
    for instruction in Input:
        for i in range(1, int(instruction[1])+1):
            head = knots[0]
            match instruction[0]:
                case "U":
                    head[1] += 1
                case "D":
                    head[1] -= 1
                case "L":
                    head[0] -= 1
                case "R":
                    head[0] += 1
            for k in range(1, len(knots)):
                prevKnot = knots[k-1]
                currKnot = knots[k]
                if(abs(prevKnot[0]-currKnot[0])+abs(prevKnot[1]-currKnot[1])>=3):
                    currKnot[0] += 1 if prevKnot[0]-currKnot[0] > 0 else -1
                    currKnot[1] += 1 if prevKnot[1]-currKnot[1] > 0 else -1
                elif(abs(prevKnot[0]-currKnot[0])==2):
                    currKnot[0] += 1 if prevKnot[0]-currKnot[0] > 0 else -1
                elif(abs(prevKnot[1]-currKnot[1])==2):
                    currKnot[1] += 1 if prevKnot[1]-currKnot[1] > 0 else -1
                if k == len(knots)-1:
                    visitedSet.add(str(currKnot[0])+" "+str(currKnot[1]))
    return len(visitedSet)