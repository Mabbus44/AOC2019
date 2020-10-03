from MabbusLib import getFileContent
from MabbusLib import IntCodeComputer05


def part1():
    fileInput = getFileContent("Day 7 Input.txt", True, False, ",")
    amp = [0, 1, 2, 3, 4]
    maxOutput = 0
    for phase0 in range(5):
        for phase1 in range(5):
            if phase1 == phase0:
                continue
            for phase2 in range(5):
                if phase2 == phase1 or phase2 == phase0:
                    continue
                for phase3 in range(5):
                    if phase3 == phase2 or phase3 == phase1 or phase3 == phase0:
                        continue
                    for phase4 in range(5):
                        if phase4 == phase3 or phase4 == phase2 or phase4 == phase1 or phase4 == phase0:
                            continue
                        phase = [phase0, phase1, phase2, phase3, phase4]
                        ampInput = 0
                        for i in range(5):
                            amp[i] = IntCodeComputer05(fileInput.copy())
                            amp[i].input = phase[i]
                            while amp[i].executeCode():
                                amp[i].input = ampInput
                                None
                            ampInput = amp[i].output
                        if ampInput > maxOutput:
                            maxOutput = ampInput
    print("Part 1: {}".format(maxOutput))


def part2():
    fileInput = getFileContent("Day 7 Input.txt", True, False, ",")
    amp = [5, 6, 7, 8, 9]
    maxOutput = 0
    for phase0 in range(5):
        for phase1 in range(5):
            if phase1 == phase0:
                continue
            for phase2 in range(5):
                if phase2 == phase1 or phase2 == phase0:
                    continue
                for phase3 in range(5):
                    if phase3 == phase2 or phase3 == phase1 or phase3 == phase0:
                        continue
                    for phase4 in range(5):
                        if phase4 == phase3 or phase4 == phase2 or phase4 == phase1 or phase4 == phase0:
                            continue
                        #   Startup
                        phase = [phase0+5, phase1+5, phase2+5, phase3+5, phase4+5]
                        for i in range(5):
                            amp[i] = IntCodeComputer05(fileInput.copy())
                            amp[i].input = phase[i]
                            amp[i].executeCode()
                        amp[0].input = 0
                        #   Run until the first amp halted
                        done = False
                        ampID = 0
                        while not done:
                            while amp[ampID].executeCode() and amp[ampID].newOutput is False:
                                None
                            if amp[ampID].newOutput:
                                ampInput = amp[ampID].output
                                ampID += 1
                                if ampID > 4:
                                    ampID = 0
                                amp[ampID].input = ampInput
                            else:
                                done = True
                        if amp[4].output > maxOutput:
                            maxOutput = ampInput
    print("Part 2: {}".format(maxOutput))


part2()
