from MabbusLib import getFileContent
from MabbusLib import IntCodeComputer05

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
BLACK = 0
WHITE = 1


class Mesh:
    def __init__(self):
        self.xMin = 0
        self.xMax = 0
        self.yMin = 0
        self.yMax = 0
        self.mesh = [[0]]
        self.visited = [[0]]

    def expandMesh(self, x, y):
        if x < self.xMin:
            for newX in range(self.xMin-x):
                for row in range(len(self.mesh)):
                    self.mesh[row].insert(0, 0)
                    self.visited[row].insert(0, 0)
            self.xMin = x
        if x > self.xMax:
            for newX in range(x-self.xMax):
                for row in range(len(self.mesh)):
                    self.mesh[row].append(0)
                    self.visited[row].append(0)
            self.xMax = x
        if y < self.yMin:
            for newRow in range(self.yMin-y):
                self.mesh.insert(0, [0]*(self.xMax-self.xMin+1))
                self.visited.insert(0, [0] * (self.xMax - self.xMin+1))
            self.yMin = y
        if y > self.yMax:
            for newRow in range(y-self.yMax):
                self.mesh.append([0]*(self.xMax-self.xMin+1))
                self.visited.append([0]*(self.xMax-self.xMin+1))
            self.yMax = y

    def getPoint(self, x, y):
        self.expandMesh(x, y)
        return self.mesh[y - self.yMin][x - self.xMin]

    def setPoint(self, x, y, val):
        if val != BLACK and val != WHITE:
            print("Error in mesh.setPoint. Invalid value for val {}".format(val))
        self.expandMesh(x, y)
        self.mesh[y - self.yMin][x - self.xMin] = val
        self.visited[y - self.yMin][x - self.xMin] = 1

    def output(self):
        for row in range(len(self.mesh)):
            for col in range(len(self.mesh[0])):
                if self.mesh[row][col] == BLACK:
                    print(".", end="")
                else:
                    print("#", end="")
            print("")


class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = UP
        self.mesh = Mesh()

    def turn(self, turnDir):
        if turnDir == 0:
            self.dir -= 1
            if self.dir < UP:
                self.dir = LEFT
        elif turnDir == 1:
            self.dir += 1
            if self.dir > LEFT:
                self.dir = UP
        else:
            print("Error in Robot.turn. Invalid turnDir {}".format(turnDir))

    def move(self):
        if self.dir == UP:
            self.y -= 1
        if self.dir == DOWN:
            self.y += 1
        if self.dir == LEFT:
            self.x -= 1
        if self.dir == RIGHT:
            self.x += 1

    def paint(self, color):
        self.mesh.setPoint(self.x, self.y, color)

    def getColor(self):
        return self.mesh.getPoint(self.x, self.y)

    def countVisited(self):
        count = 0
        for row in range(len(self.mesh.visited)):
            for col in range(len(self.mesh.visited[0])):
                if self.mesh.visited[row][col] == 1:
                    count += 1
        return count


def part1():
    fileInput = getFileContent("Day 11 Input.txt", True, False, ",")
    comp = IntCodeComputer05(fileInput)
    robot = Robot()
    comp.input = robot.getColor()
    paint = True
    while comp.executeCode():
        if comp.newOutput:
            if paint:
                robot.paint(comp.output)
                comp.input = robot.getColor()
                paint = False
            else:
                robot.turn(comp.output)
                robot.move()
                comp.input = robot.getColor()
                paint = True
    print("Part 1: {}".format(robot.countVisited()))


def part2():
    fileInput = getFileContent("Day 11 Input.txt", True, False, ",")
    comp = IntCodeComputer05(fileInput)
    robot = Robot()
    robot.mesh.mesh[0][0] = WHITE
    comp.input = robot.getColor()
    paint = True
    while comp.executeCode():
        if comp.newOutput:
            if paint:
                robot.paint(comp.output)
                comp.input = robot.getColor()
                paint = False
            else:
                robot.turn(comp.output)
                robot.move()
                comp.input = robot.getColor()
                paint = True
    print("Part 2:")
    robot.mesh.output()


part1()
part2()
