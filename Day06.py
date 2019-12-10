from MabbusLib import getFileContent


class Body:
    #   Body
    def __init__(self, name):
        #   Body has a name, and reference to its parents and children
        self.parent = 0
        self.children = []
        self.name = name

    def orbitCount(self):
        #   Returns the number of bodies orbited
        if self.parent:
            return self.parent.orbitCount() + 1
        return 0

    def expandRoutes(self, inputRoute):
        #   Returns a list of all possible continuations of inputRout that do not repeat a body
        newBody = 0
        parentCount = 0
        if self.parent:
            parentCount = 1
        ret = []
        for cIndex in range(len(self.children)+parentCount):
            validRoute = False
            if cIndex == len(self.children):
                newBody = self.parent
            else:
                newBody = self.children[cIndex]
            for i in inputRoute:
                if i == newBody:
                    validRoute = False
            if validRoute:
                newRoute = list(inputRoute)
                newRoute.append(newBody)
                ret.append(newRoute)
        return ret


class BodyList:
    #   A list of body with some methods
    def __init__(self):
        self.bodies = []

    def addBody(self, name, parentName="none"):
        #   Adds a new body to the list (if not present), and adds the parent, child references
        #   Check if name and parent is new to the list, and if they are, add them to the list
        newName = True
        newParent = True
        if parentName == "none":
            newParent = False
        for b in self.bodies:
            if b.name == name:
                newName = False
            if b.name == parentName:
                newParent = False
        if newName:
            self.bodies.append(Body(name))
        if newParent:
            self.bodies.append(Body(parentName))
        #   Get the body references for the name and the parent
        mainBody = 0
        parentBody = 0
        for b in self.bodies:
            if b.name == name:
                mainBody = b
            if b.name == parentName:
                parentBody = b
        #   Set the parent and child references
        mainBody.parent = parentBody
        if parentBody:
            parentBody.children.append(mainBody)

    def indexByName(self, name):
        #   Returns index of object with name
        for i in range(len(self.bodies)):
            if self.bodies[i] == name:
                return i
        return -1


def part1():
    fileInput = getFileContent("Day 6 Input.txt", False, False, "\n", ")")
    bodies = BodyList()
    for row in fileInput:
        bodies.addBody(row[1], row[0])
    orbitSum = 0
    for b in bodies.bodies:
        orbitSum += b.orbitCount()
    print("Part 1: {} orbits".format(orbitSum))


def part2():
    fileInput = getFileContent("Day 6 Input.txt", False, False, "\n", ")")
    bodies = BodyList()
    for row in fileInput:
        bodies.addBody(row[1], row[0])
    startBody = bodies.bodies[bodies.indexByName("YOU")].parent
    endBody = bodies.bodies[bodies.indexByName("SAN")].parent
    routes = startBody.expandRoutes([])
    routeLen = 1
    newRoutes = []
    for r in routes:
        tNewRoutes = r[routeLen-1].expandRoutes(r)
        for r2 in tNewRoutes:
            newRoutes.append(r2)
    print("Part 2: {} orbits".format(orbitSum))


part2()
