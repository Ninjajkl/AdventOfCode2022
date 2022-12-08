import importlib
import importlib.util

while(True):
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
    print(getattr(day, "Part" + str(dayPart))(inputType))

    exitAnswer = str(input("Enter 'Y' to continue, otherwise enter anything else to exit\n"))
    if(exitAnswer != "Y"):
        break