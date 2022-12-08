def Part1(inputName):
    textFile = open("Inputs\\" + inputName + "Input.txt", "r")
    RawInput = textFile.readlines()
    RawInput.append("\n")
    Sum = 0
    maxCalories = 0
    for line in RawInput:
        if len(line.replace("\n", "")) == 0:
            maxCalories = max(maxCalories,Sum)
            Sum = 0
        else:
            Sum += int(line.replace("\n", ""))
    return maxCalories

def Part2(inputName):
    textFile = open("Inputs\\" + inputName + "Input.txt", "r")
    RawInput = textFile.readlines()
    RawInput.append("\n")
    Sum = 0
    maxCalories = [0,0,0]
    for line in RawInput:
        if len(line.replace("\n", "")) == 0:
            for i in range(0, len(maxCalories)):
                if Sum == max(maxCalories[i],Sum):
                    maxCalories.insert(i,Sum)
                    maxCalories.pop()
                    break
            Sum = 0
        else:
            Sum += int(line.replace("\n", ""))
    return sum(maxCalories)