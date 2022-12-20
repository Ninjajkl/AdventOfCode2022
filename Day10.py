def Part1(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        Input = [line.rstrip("\n").split() for line in f]
    cycle = 0
    register = 1
    signalSum = 0
    for instr in Input:
        if instr[0] == "noop":
            cycle +=1
            if cycle%40 == 20:
                signalSum += register*cycle
        else:
            for i in range(0,2):
                cycle += 1
                if cycle%40 == 20:
                    signalSum += register*cycle
                if i == 1:
                    register += int(instr[1])
    return signalSum

def Part2(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        Input = [line.rstrip("\n").split() for line in f]
    cycle = 0
    register = 1
    CRT = ""
    for instr in Input:
        if instr[0] == "noop":
            cycle +=1
            CRT += "#" if len(CRT)%41 in range(register-1, register+2) else "."
            if cycle%40 == 0:
                CRT += "\n"
        else:
            for i in range(0,2):
                cycle += 1
                CRT += "#" if len(CRT)%41 in range(register-1, register+2) else "."
                if cycle%40 == 0:
                    CRT += "\n"
                if i == 1:
                    register += int(instr[1])
    return "\n"+CRT
