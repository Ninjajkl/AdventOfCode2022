def Part1(inputName):
    textFile = open("Inputs\\" + inputName + "Input.txt", "r")
    RawInput = textFile.readlines()
    List = []
    for line in RawInput:
        List.append(line.replace("\n", ""))
    count = 0
    for line in List:
        group = line.split(",")
        p1 = group[0].split("-")
        p2 = group[1].split("-")
        if((int(p1[0]) <= int(p2[0]) and int(p1[1]) >= int(p2[1])) or (int(p1[0]) >= int(p2[0]) and int(p1[1]) <= int(p2[1]))):
            count += 1
    return count

def Part2(inputName):
    textFile = open("Inputs\\" + inputName + "Input.txt", "r")
    RawInput = textFile.readlines()
    List = []
    for line in RawInput:
        List.append(line.replace("\n", ""))
    count = 0
    for line in List:
        group = line.split(",")
        p1 = group[0].split("-")
        p2 = group[1].split("-")
        if((int(p1[1]) >= int(p2[0]) and int(p1[0]) <= int(p2[1])) or(int(p2[1]) >= int(p1[0]) and int(p2[0]) <= int(p1[1]))):
            count += 1
    return count