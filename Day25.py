def SNAFUToDecimal(SNAFU : str):
    valueDict = {
        "2" : 2,
        "1" : 1,
        "0" : 0,
        "-" : -1,
        "=" : -2
    }
    intBuilder = 0
    for i in range(len(SNAFU)-1,-1,-1):
        intBuilder += pow(5,(len(SNAFU)-1)-i) * valueDict[SNAFU[i]]
    return intBuilder

def DecimalToSNAFU(decimal : str):
    vDict = {
        2 : "2",
        1 : "1",
        0 : "0",
        -1 : "-",
        -2 : "="
    }
    upperMax = [0]
    lowerMin = [0]
    currPlace = 0
    stringBuilder = ""
    for i in range(0,100):
        lowerMin.insert(0,pow(5,i)-upperMax[0])
        upperMax.insert(0,upperMax[0]+2*pow(5,i))
        if upperMax[0] >= decimal:
            firstPlace = 1 if decimal<(upperMax[0]+lowerMin[0])//2 else 2
            decimal -= firstPlace*pow(5,i)
            currPlace = i-1
            lowerMin.pop(0)
            upperMax.pop(0)
            stringBuilder += vDict[firstPlace]
            break
    for i in range(currPlace,-1,-1):
        nextPlace = 2 if decimal>(upperMax[0]+lowerMin[0])//2 else (1 if lowerMin[0]<decimal else (0 if -lowerMin[0] < decimal else (-1 if (-upperMax[0]-lowerMin[0])//2<decimal else -2)))
        decimal -= nextPlace*pow(5,i)
        lowerMin.pop(0)
        upperMax.pop(0)
        stringBuilder += vDict[nextPlace]
    return stringBuilder

def Part1(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        SNAFUSum = sum([SNAFUToDecimal(line.rstrip("\n")) for line in f])
    return DecimalToSNAFU(SNAFUSum)

def Part2(inputName):
    return DecimalToSNAFU(69)