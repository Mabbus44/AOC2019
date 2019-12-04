class Password:
    def __init__(self, size):
        self.size = size
        self.digits = [0]*size
        self.overflow = False

    def setPassword(self, password):
        for i in range(self.size-1, -1, -1):
            self.digits[i] = password//(10**i)
            password -= self.digits[i]*10**i

    def returnInt(self):
        ret = 0
        for i in range(self.size):
            ret += self.digits[i]*10**i
        return ret

    def print(self):
        print(self.returnInt())

    def increaseDigit(self, i):
        self.digits[i] += 1
        if self.digits[i] > 9:
            self.digits[i] = 0
            if i >= self.size:
                self.overflow = True
            else:
                self.increaseDigit(i+1)
                self.digits[i] = self.digits[i+1]

    def makeValid(self):
        for i in range(self.size-2, -1, -1):
            if self.digits[i] < self.digits[i+1]:
                self.digits[i] = self.digits[i+1]

    def hasDoubleDigit(self):
        for i in range(self.size-2, -1, -1):
            if self.digits[i] == self.digits[i+1]:
                return True
        return False

    def hasDoubleDigitExclusive(self):
        inARow = 1
        hasDouble = False
        for i in range(self.size-2, -1, -1):
            if self.digits[i] == self.digits[i+1]:
                inARow += 1
            else:
                if inARow == 2:
                    hasDouble = True
                inARow = 1
        if inARow == 2:
            hasDouble = True
        if hasDouble:
            return True
        return False


def part1():
    digitCount = 6
    startVal = 359282
    endVal = 820401
    p = Password(digitCount)
    p.setPassword(startVal)
    p.makeValid()
    count = 0
    while p.returnInt() <= endVal:
        if p.hasDoubleDigit():
            count += 1
        p.increaseDigit(0)
    print("Part 1: {} passwords".format(count))


def part2():
    digitCount = 6
    startVal = 359282
    endVal = 820401
    p = Password(digitCount)
    p.setPassword(startVal)
    p.makeValid()
    count = 0
    while p.returnInt() <= endVal:
        if p.hasDoubleDigitExclusive():
            count += 1
        p.increaseDigit(0)
    print("Part 2: {} passwords".format(count))


part2()
