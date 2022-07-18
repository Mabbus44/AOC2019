from MabbusLib import getFileContent
from MabbusLib import Coord


def part12():
    asteroidsRaw = getFileContent("Day 10 Input.txt", False, True, "\n")
    asteroids = []
    for y in range(len(asteroidsRaw)):
        for x in range(len(asteroidsRaw[0])):
            if asteroidsRaw[y][x] == "#":
                asteroids.append(Coord(x, y))
    bestAsteroid = Coord()
    bestAsteroidCount = 0
    bestSeenAsteroids = []
    for a in asteroids:
        count = 0
        seenAsteroids = []
        for b in asteroids:
            fail = False
            aToBDir = a.dir(b)
            if aToBDir.x == 0 and aToBDir.y == 0:
                check = b
                fail = True
            else:
                check = a + aToBDir
            while check != b:
                if asteroidsRaw[check.y][check.x] == "#":
                    fail = True
                check = check + aToBDir
            if not fail:
                count += 1
                seenAsteroids.append(b)
        if count > bestAsteroidCount:
            bestAsteroid = a
            bestAsteroidCount = count
            bestSeenAsteroids = seenAsteroids
    print("Part 1: {}".format(bestAsteroidCount))
    for a in bestSeenAsteroids:
        a.calcAngle(bestAsteroid)
    bestSeenAsteroids.sort(key=lambda ast: ast.angle)
    i = 0
    deleteCount = 0
    while len(bestSeenAsteroids) > 0:
        aToBDir = bestAsteroid.dir(bestSeenAsteroids[i])
        check = bestSeenAsteroids[i] + aToBDir
        replaced = False
        deleteCount += 1
        if deleteCount == 200:
            print("Part 2: {}".format(bestSeenAsteroids[i].x * 100 + bestSeenAsteroids[i].y))
            break
        while replaced is False and 0 <= check.x < len(asteroidsRaw[0]) and 0 <= check.y < len(asteroidsRaw):
            if asteroidsRaw[check.y][check.x] == "#":
                replaced = True
                bestSeenAsteroids[i] = Coord(check.x, check.y)
                bestSeenAsteroids[i].calcAngle(bestAsteroid)
            check = check + aToBDir
        if replaced is False:
            del bestSeenAsteroids[i]
        else:
            i += 1
        if i >= len(bestSeenAsteroids):
            i = 0


part12()
