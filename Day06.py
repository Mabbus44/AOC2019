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

    def parentList(self, inputList):
        #   Returns a list of all parents and grand parents
        if self.parent:
            inputList.append(self.parent)
            return self.parent.parentList(inputList)
        else:
            return inputList


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
    startBody = next(b for b in bodies.bodies if b.name == "YOU")
    endBody = next(b for b in bodies.bodies if b.name == "SAN")
    startBodyParents = startBody.parentList([])
    endBodyParents = endBody.parentList([])
    firstHalf = 0
    for p in startBodyParents:
        if p in endBodyParents:
            break
        firstHalf += 1
    secondHalf = 0
    for p in endBodyParents:
        if p in startBodyParents:
            break
        secondHalf += 1
    print("Part 2: {}".format(firstHalf + secondHalf))


part2()
