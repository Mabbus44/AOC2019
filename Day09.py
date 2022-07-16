from MabbusLib import getFileContent
from MabbusLib import IntCodeComputer05


def part1():
    fileInput = getFileContent("Day 9 Input.txt", True, False, ",")
    comp = IntCodeComputer05(fileInput)
    comp.input = 1
    while comp.executeCode():
        None
    print("Part 1: {}".format(comp.output))


def part2():
    fileInput = getFileContent("Day 9 Input.txt", True, False, ",")
    comp = IntCodeComputer05(fileInput)
    comp.input = 2
    while comp.executeCode():
        None
    print("Part 2: {}".format(comp.output))


part1()
part2()
