import re
import numpy
from shapely.geometry import Polygon


def Part1(inputName):
    Input = convertInput(inputName)
    return findEmptyInRow(2000000, Input)

def Part2(inputName):
    Input = convertInput(inputName)
    return findEmptyInGrid(4000000, Input)
    
def convertInput(inputName : str):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        RawInput = [line.rstrip("\n").replace("=", " ").replace(",", "").replace(":","") for line in f]
        Input = []
        for line in RawInput:
            l = []
            for v in line.split():
                try: l.append(int(v))
                except ValueError: pass
            Input.append(l)
    return Input

def findEmptyInRow(row : int, input : list[list[int]]):
    rowSet = set()
    for line in input:
        manhat = abs(line[0]-line[2]) + abs(line[1]-line[3])
        for c in range(line[0]-(manhat-abs(row-line[1])), line[0]+(manhat-abs(row-line[1]))+1):
            rowSet.add(c)
    for line in input:
        if line[3]==row:rowSet.discard(line[2])
    return len(rowSet)

def findEmptyInGrid(maxValue : int, input : list[list[int]]):
    areaTaken = Polygon()
    for line in input:
        manhat = abs(line[0]-line[2]) + abs(line[1]-line[3])
        areaTaken = areaTaken.union(Polygon(((line[0],line[1]-manhat),(line[0]+manhat,line[1]),(line[0],line[1]+manhat),(line[0]-manhat,line[1]))))
    areaTaken = areaTaken.intersection(Polygon(((0,0),(maxValue,0),(maxValue,maxValue),(0,maxValue))))
    print(areaTaken.wkt)
    print("The empty spot is the point surrounded by the second list of tuples")
    print(3141837*4000000+3400528)