from MabbusLib import getFileContent


def part1():
    fileInput = getFileContent("Day 1 Input.txt", True, False, "\n")
    fuelSum = 0
    for f in fileInput:
        fuelSum += int(f/3)-2
    print("Part 1: {}".format(fuelSum))


def part2():
    fileInput = getFileContent("Day 1 Input.txt", True, False, "\n")
    fuelSum = 0
    for f in fileInput:
        addFuel = f
        while addFuel > 0:
            addFuel = int(addFuel/3)-2
            if addFuel > 0:
                fuelSum += addFuel
    print("Part 2: {}".format(fuelSum))


part2()
