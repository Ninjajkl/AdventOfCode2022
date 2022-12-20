import types

def interpretInput(Input : list[str]):
    head = FileSystem(None, "dir", "/", 0)
    currDirectory = head
    for i in range(0, len(Input)):
        if Input[i][0] == "$":
            if Input[i].count("cd") > 0:
                if Input[i].count("..") > 0:
                    currDirectory = currDirectory.previousFile
                elif Input[i].count("/") > 0:
                    currDirectory = head
                else:
                    for child in currDirectory.childrenList:
                        if child.fileType == "dir" and child.name == Input[i][Input[i].index("cd")+3:]:
                            currDirectory = child
            else:
                i += 1
                while Input[i].count("$") == 0:
                    if Input[i].count("dir") > 0:
                        newDir = FileSystem(currDirectory, "dir", Input[i][Input[i].index(" ")+1:], 0)
                        currDirectory.childrenList.append(newDir)
                    else:
                        if Input[i].count(".") > 0:
                            newFile = FileSystem(currDirectory, Input[i][Input[i].index(".")+1:], Input[i][Input[i].index(" ")+1:Input[i].index(".")], int(Input[i][:Input[i].index(" ")]))
                        else:
                            newFile = FileSystem(currDirectory, "None", Input[i][Input[i].index(" ")+1:], int(Input[i][:Input[i].index(" ")]))
                        currDirectory.addValue(newFile.size)
                        currDirectory.childrenList.append(newFile)
                    i += 1
                    if(i == len(Input)):
                        return head
                i -= 1
    return head

def Part1(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        RawInput = [line.rstrip("\n") for line in f]
    root = interpretInput(RawInput)
    return root.findTotalSize(100000)

def Part2(inputName):
    with open("Inputs\\" + inputName + "Input.txt") as f:
        RawInput = [line.rstrip("\n") for line in f]
    root = interpretInput(RawInput)
    return root.findMinDir(30000000-(70000000 - root.size), root.size)

class FileSystem:
    previousFile = types.SimpleNamespace()
    childrenList = []
    fileType : str
    name : str
    size : int

    def __init__(self, prevFile, fileType, name, size):
        self.previousFile = prevFile
        self.fileType = fileType
        self.name = name
        self.size = size
        self.childrenList = []

    def addValue(self, value):
        self.size += value
        if self.name != "/":
            self.previousFile.addValue(value)

    def findTotalSize(self, limit):
        sum = 0
        for child in self.childrenList:
            if child.fileType == "dir" and child.size <= limit:
                sum += child.size
            sum += child.findTotalSize(limit)
        return sum

    def findMinDir(self, min, smallest):
        for child in self.childrenList:
            if child.fileType == "dir" and child.size >= min and child.size < smallest:
                smallest = child.size
            smallest = child.findMinDir(min, smallest)
        return smallest

    def printChildren(self):
        for child in self.childrenList:
            print(child)
            child.printChildren()
        return

    def __repr__(self) -> str:
        if self.previousFile == None:
            builder = "\nPrevious File: None"
        else:
            builder = "\nPrevious File: " + self.previousFile.name
        builder += ", Name: " + self.name
        builder += ", Children: "
        for child in self.childrenList:
            builder += child.name + " "
        builder += ", File Type: " + self.fileType + ", Size: " + str(self.size)
        return builder