def filterNumbers(strNum):
    #   Returns true if string contains number
    try:
        int(strNum)
        return True
    except ValueError:
        return False


def getFileContent(fileName, returnNumber, individualChars, firstSplit="", secondSplit=""):
    #   Converts file into lists of strings or integers
    #   IndividualChars can only be combined with returnNumber or firstSplit, not both and not secondSplit (lazy patch)
    #   Load file
    inputFile = open(fileName, "r")
    content = inputFile.read()
    inputFile.close()

    #   Replace characters if splits is list
    if not isinstance(firstSplit, str):
        for letter in firstSplit:
            content = content.replace(letter, firstSplit[0])
        firstSplit = firstSplit[0]
    if not isinstance(secondSplit, str):
        for letter in secondSplit:
            content = content.replace(letter, secondSplit[0])
        secondSplit = secondSplit[0]

    #   If "individualChars" split the string into chars
    if individualChars:
        ret = list(content)
        if firstSplit != "":
            content = list(filter(None, content.split(firstSplit)))
            ret = []
            for row in content:
                ret.append(list(row))
            return ret
        if returnNumber:
            ret = list(map(int, list(filter(filterNumbers, ret))))
        return ret

    #   Split the string by "firstSplit" if defined
    if firstSplit != "":
        if returnNumber and secondSplit == "":
            content = list(map(int, list(filter(filterNumbers, content.split(firstSplit)))))
        else:
            content = list(filter(None, content.split(firstSplit)))

    #   Split each string by "secondSplit" if defined
    if secondSplit != "":
        ret = []
        for row in content:
            if returnNumber:
                ret.append(list(map(int, list(filter(filterNumbers, row.split(secondSplit))))))
            else:
                ret.append(list(filter(None, row.split(secondSplit))))
    else:
        ret = content
    return ret


class RoundList:
    def __init__(self, newObj):
        self.obj = newObj
        self.prev = self
        self.nxt = self

    def delete(self):
        self.nxt.prev = self.prev
        self.prev.nxt = self.nxt

    def add(self, newObj):
        newListObj = RoundList(newObj)
        newListObj.prev = self
        newListObj.nxt = self.nxt
        self.nxt.prev = newListObj
        self.nxt = newListObj


class IntCodeComputer05:
    #   Interprets program
    def __init__(self, mem):
        self.mem = mem
        self.p = 0
        self.readMode = [0, 0, 0]
        self.input = 1
        self.output = 0
        self.newOutput = False
        self.END = 99
        self.NONE = 0
        self.ADD = 1
        self.MULTIPLY = 2
        self.INPUT = 3
        self.OUTPUT = 4
        self.JUMP_IF_TRUE = 5
        self.JUMP_IF_FALSE = 6
        self.LESS_THAN = 7
        self.EQUALS = 8

    def translateOPCode(self):
        #   Sets readMode and returns opCode
        if self.p >= len(self.mem):
            self.readMode = [0, 0, 0]
            return 0
        mem = self.mem[self.p]
        ret = mem % 100
        mem = mem // 100
        self.readMode[0] = mem % 10
        mem = mem // 10
        self.readMode[1] = mem % 10
        mem = mem // 10
        self.readMode[2] = mem % 10
        return ret

    def getParameter(self, i, mode):
        #   Gets memory slot mem[i], or value mem[i] depending on mode
        if self.readMode[mode] == 0:
            return self.mem[self.mem[i]]
        else:
            return self.mem[i]

    def executeCode(self):
        self.newOutput = False
        if self.p >= len(self.mem):
            print("ERROR: Read from outside memory")
            return 0
        opCode = self.translateOPCode()
        if opCode == self.END:
            return 0
        if opCode == self.ADD:
            self.mem[self.mem[self.p+3]] = self.getParameter(self.p+1, 0) + self.getParameter(self.p+2, 1)
            self.p += 4
        if opCode == self.MULTIPLY:
            self.mem[self.mem[self.p+3]] = self.getParameter(self.p+1, 0) * self.getParameter(self.p+2, 1)
            self.p += 4
        if opCode == self.INPUT:
            self.mem[self.mem[self.p+1]] = self.input
            self.p += 2
        if opCode == self.OUTPUT:
            self.output = self.getParameter(self.p+1, 0)
            self.p += 2
            self.newOutput = True
        if opCode == self.JUMP_IF_TRUE:
            if self.getParameter(self.p+1, 0) != 0:
                self.p = self.getParameter(self.p+2, 1)
            else:
                self.p += 3
        if opCode == self.JUMP_IF_FALSE:
            if self.getParameter(self.p + 1, 0) == 0:
                self.p = self.getParameter(self.p + 2, 1)
            else:
                self.p += 3
        if opCode == self.LESS_THAN:
            if self.getParameter(self.p + 1, 0) < self.getParameter(self.p + 2, 1):
                self.mem[self.mem[self.p + 3]] = 1
            else:
                self.mem[self.mem[self.p + 3]] = 0
            self.p += 4
        if opCode == self.EQUALS:
            if self.getParameter(self.p + 1, 0) == self.getParameter(self.p + 2, 1):
                self.mem[self.mem[self.p + 3]] = 1
            else:
                self.mem[self.mem[self.p + 3]] = 0
            self.p += 4
        if opCode == self.NONE:
            self.p += 1
        return 1
