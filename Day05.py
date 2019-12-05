from MabbusLib import getFileContent

END = 99
ADD = 1
MULTIPLY = 2
INPUT = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8


class IntCodeComputer:
    #   Interprets program
    def __init__(self, mem):
        self.mem = mem
        self.p = 0
        self.readMode = [0, 0, 0]
        self.input = 1
        self.output = 0
        self.newOutput = False

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
        if opCode == END:
            return 0
        if opCode == ADD:
            self.mem[self.mem[self.p+3]] = self.getParameter(self.p+1, 0) + self.getParameter(self.p+2, 1)
            self.p += 4
        if opCode == MULTIPLY:
            self.mem[self.mem[self.p+3]] = self.getParameter(self.p+1, 0) * self.getParameter(self.p+2, 1)
            self.p += 4
        if opCode == INPUT:
            self.mem[self.mem[self.p+1]] = self.input
            self.p += 2
        if opCode == OUTPUT:
            self.output = self.getParameter(self.p+1, 0)
            self.p += 2
            self.newOutput = True
        if opCode == JUMP_IF_TRUE:
            if self.getParameter(self.p+1, 0) != 0:
                self.p = self.getParameter(self.p+2, 1)
            else:
                self.p += 3
        if opCode == JUMP_IF_FALSE:
            if self.getParameter(self.p + 1, 0) == 0:
                self.p = self.getParameter(self.p + 2, 1)
            else:
                self.p += 3
        if opCode == LESS_THAN:
            if self.getParameter(self.p + 1, 0) < self.getParameter(self.p + 2, 1):
                self.mem[self.mem[self.p + 3]] = 1
            else:
                self.mem[self.mem[self.p + 3]] = 0
            self.p += 4
        if opCode == EQUALS:
            if self.getParameter(self.p + 1, 0) == self.getParameter(self.p + 2, 1):
                self.mem[self.mem[self.p + 3]] = 1
            else:
                self.mem[self.mem[self.p + 3]] = 0
            self.p += 4
        return 1


def part1():
    fileInput = getFileContent("Day 5 Input.txt", True, False, ",")
    comp = IntCodeComputer(fileInput)
    while comp.executeCode():
        None
    print("Part 1: {}".format(comp.output))


def part2():
    fileInput = getFileContent("Day 5 Input.txt", True, False, ",")
    comp = IntCodeComputer(fileInput)
    comp.input = 5
    while comp.executeCode():
        None
    print("Part 2: {}".format(comp.output))


part2()
