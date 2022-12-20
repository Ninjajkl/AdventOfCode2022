import importlib
import importlib.util
from time import time_ns

while(True):
    #break
    #Day Selection
    dayNumber = str(input("Enter day to test in the format XX\n"))
    testLoader = importlib.util.find_spec("Day" + dayNumber)
    while testLoader is None:
        dayNumber = str(input("Enter day to test in the format XX\n"))
        testLoader = importlib.util.find_spec("Day" + dayNumber)
    day = importlib.import_module("Day" + dayNumber)
    0
    #Part Selection
    dayPart = int(input("Which part? Answer with a single number in the format X\n"))
    while not hasattr(day,'Part' + str(dayPart)):
        dayPart = int(input("Which part? Answer with a single number in the format X\n"))

    #Input Selection
    testType = str(input("If test, enter 'test'. Else, enter anything else\n"))
    if(testType == 'test'):
        inputType = "Test"
    else:
        inputType = "Day" + dayNumber

    #print output
    start = time_ns()
    print("Part "+ str(dayPart) +": " + str(getattr(day, "Part" + str(dayPart))(inputType)) + " in " + str((time_ns()-start)/1e6) + "ms")

    exitAnswer = str(input("Enter 'Y' to continue, otherwise enter anything else to exit\n"))
    if(exitAnswer != "Y"):
        break

def printAllDays(highestDay : int):
    for i in range(1,highestDay+1):
        print()
        dayNumber = str(i) if i >= 10 else "0" + str(i)
        day = importlib.import_module("Day" + dayNumber)
        print("Day" + dayNumber + ":")
        start = time_ns()
        print("Part 1: " + str(getattr(day, "Part1")("Day" + dayNumber)) + " in " + str((time_ns()-start)/1e6) + "ms")
        start = time_ns()
        print("Part 2: " + str(getattr(day, "Part2")("Day" + dayNumber)) + " in " + str((time_ns()-start)/1e6) + "ms")
#printAllDays(19)
