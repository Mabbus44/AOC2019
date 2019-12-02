from MabbusLib import getFileContent


def part1():
    mem = getFileContent("Day 2 Input.txt", True, False, ",")
    i = 0
    mem[1] = 12
    mem[2] = 2
    while mem[i] != 99:
        if mem[i] == 1:
            mem[mem[i+3]] = mem[mem[i+1]] + mem[mem[i+2]]
            i += 4
        elif mem[i] == 2:
            mem[mem[i+3]] = mem[mem[i+1]] * mem[mem[i+2]]
            i += 4
    print("Part 1: {}".format(mem[0]))


def part2():
    fileInput = getFileContent("Day 2 Input.txt", True, False, ",")
    goal = 19690720
    done = False
    for noun in range(100):
        for verb in range(100):
            mem = list(fileInput)
            i = 0
            mem[1] = noun
            mem[2] = verb
            while mem[i] != 99:
                if mem[i] == 1:
                    mem[mem[i+3]] = mem[mem[i+1]] + mem[mem[i+2]]
                    i += 4
                elif mem[i] == 2:
                    mem[mem[i+3]] = mem[mem[i+1]] * mem[mem[i+2]]
                    i += 4
            if mem[0] == goal:
                print("Part 2: {}".format(100 * noun + verb))
                done = True
                break
        if done:
            break


part2()
