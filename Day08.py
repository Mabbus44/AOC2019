from MabbusLib import getFileContent


class Layer:
    def __init__(self, xSize, ySize, pixels):
        #   Initializes layer and places pixels into 2d array
        self.xSize = xSize
        self.ySize = ySize
        self.pixels = [[] for _ in range(ySize)]
        for y in range(ySize):
            for x in range(xSize):
                self.pixels[y].append(pixels[y*xSize+x])

    def print(self):
        #   Prints layer
        for y in range(self.ySize):
            for x in range(self.xSize):
                print(self.pixels[y][x], end='')
            print("")
        print("")

    def getDigitCount(self):
        #   Return array with count of each digit
        count = [0, 0, 0]
        for y in range(self.ySize):
            for x in range(self.xSize):
                if self.pixels[y][x] < 0 or self.pixels[y][x] > 2:
                    print("ERROR: {} found in picture".format(self.pixels[y][x]))
                else:
                    count[self.pixels[y][x]] += 1
        return count


class Picture:
    def __init__(self, xSize, ySize, pixels):
        #   Initializes picture and places pixels into layers
        self.xSize = xSize
        self.ySize = ySize
        self.layers = []
        self.finalPicture = Layer(xSize, ySize, [2]*(xSize*ySize))
        layerSize = xSize*ySize
        layerCount = len(pixels) // layerSize
        for layer in range(layerCount):
            self.layers.append(Layer(xSize, ySize, pixels[layer*layerSize:(layer+1)*layerSize]))

    def print(self):
        #   Prints all layers of picture
        for layer in range(len(self.layers)):
            print("Layer {}".format(layer))
            self.layers[layer].print()

    def combineLayers(self):
        #   Combines layers into finalPicture
        for layer in self.layers:
            for y in range(layer.ySize):
                for x in range(layer.xSize):
                    if self.finalPicture.pixels[y][x] == 2:
                        self.finalPicture.pixels[y][x] = layer.pixels[y][x]


def day1():
    fileInput = getFileContent("Day 8 Input.txt", True, True)
    p = Picture(25, 6, fileInput)
    lowestZeroCount = 999
    ans = 0
    for layer in p.layers:
        dCount = layer.getDigitCount()
        if dCount[0] < lowestZeroCount:
            lowestZeroCount = dCount[0]
            ans = dCount[1]*dCount[2]
    print("Part 1: {}".format(ans))


def day2():
    fileInput = getFileContent("Day 8 Input.txt", True, True)
    p = Picture(25, 6, fileInput)
    p.combineLayers()
    print("Part 2:")
    p.finalPicture.print()


day2()
