def Part1(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        Input = [line.rstrip("\n") for line in f]
    orderCounter = 0
    InputList = []
    pairList = []
    for i in range(0, len(Input)):
        if i%3 != 2:
            pairList.append(createPacket(Input[i]))
        if i%3 == 2 or i == len(Input)-1:
            InputList.append(pairList)
            pairList = []
    for pair in enumerate(InputList, 1):
        orderCounter += pair[0] if CompareLists(pair[1][0], pair[1][1])==-1 else 0
    return(orderCounter)

def Part2(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        Input = [line.rstrip("\n") for line in f]
    packetList = []
    for i,line in enumerate(Input):
        if i%3 != 2:
            packetList.append(createPacket(line))
    packetList.append([[2]])
    packetList.append([[6]])
    for i in range(0, len(packetList)):
        for j in range(0, len(packetList)-1-i):
            if CompareLists(packetList[j],packetList[j+1]) != -1:
                temp = packetList[j]
                packetList[j] = packetList[j+1]
                packetList[j+1] = temp
    divider2 = 0
    divider6 = 0
    for i, packet in enumerate(packetList,1):
        if packet == [[2]]:
            divider2 = i
            if divider6 !=0:
                return divider2 * divider6
        if packet == [[6]]:
            divider6 = i
            if divider2 !=0:
                return divider2 * divider6

def createPacket(line : str):
    if len(line) == 0:
        return ""
    parentDir = {}
    intBuilder = ""
    for c in enumerate(line):
        if c[0] == 0:
            masterList = []
            parentList = masterList
            currList = masterList
            continue
        if c[0] == len(line)-1:
            if len(intBuilder) > 0:
                currList.append(int(intBuilder))
                intBuilder = ""
            continue
        if c[1] == "[":
            currList = []
            parentDir.update({id(currList) : parentList})
            parentList = currList
            continue
        if c[1] == "]":
            if len(intBuilder) > 0:
                currList.append(int(intBuilder))
                intBuilder = ""
            parentList = parentDir.get(id(currList))
            parentList.append(currList)
            currList = parentList
            continue
        if c[1] == ',':
            if len(intBuilder) > 0:
                currList.append(int(intBuilder))
                intBuilder = ""
            continue
        intBuilder += c[1]
    return masterList

def CompareInt(left : int, right : int):
    #print(left,right)
    if left == right:
        return 0
    if left < right:
        return -1
    if left > right:
        return 1

def CompareLists(left, right):
    #print(left,right)
    if(len(left)==0):
        if(len(right)==0):
            return 0
        return -1
    for i in range(0, len(left)):
        if len(right) <= i:
            return 1
        if type(left[i])==int:
            if type(right[i])==int:
                value = CompareInt(left[i],right[i])
                if value != 0: return value
            else:
                value = CompareLists([left[i]],right[i])
                if value != 0: return value
        elif type(left[i]) == list:
            if type(right[i])==int:
                value = CompareLists(left[i],[right[i]])
                if value != 0: return value
            else:
                value = CompareLists(left[i],right[i])
                if value != 0: return value
    if len(left) < len(right): return -1
    return 0