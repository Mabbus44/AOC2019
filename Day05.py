from MabbusLib import getFileContent
from MabbusLib import IntCodeComputer05


def part1():
    fileInput = getFileContent("Day 5 Input.txt", True, False, ",")
    comp = IntCodeComputer05(fileInput)
    while comp.executeCode():
        None
    print("Part 1: {}".format(comp.output))


def part2():
    fileInput = getFileContent("Day 5 Input.txt", True, False, ",")
    comp = IntCodeComputer05(fileInput)
    comp.input = 5
    while comp.executeCode():
        None
    print("Part 2: {}".format(comp.output))


part1()
part2()
