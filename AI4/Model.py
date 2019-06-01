class Model:
    def __init__(self):
        self.__temp, self.__cap = readInput("input2.in")
        self.__cold, self.__cool, self.__moderate, self.__hot, self.__veryhot = readTemp("temperature.in")
        self.__small, self.__medium, self.__high = readCap("capacity.in")

    def getTemp(self):
        return self.__temp

    def getCap(self):
        return self.__cap

    def getCold(self):
        return self.__cold

    def getCool(self):
        return self.__cool

    def getModerate(self):
        return self.__moderate

    def getHot(self):
        return self.__hot

    def getVeryHot(self):
        return self.__veryhot

    def getSmall(self):
        return self.__small

    def getMedium(self):
        return self.__medium

    def getHigh(self):
        return self.__high

def readInput(filename):
    f = open(filename, 'r')
    t = int(f.readline().split("=")[1])
    c = int(f.readline().split("=")[1])
    return t, c

def readTemp(filename):
    f = open(filename, 'r')
    cold = []
    cool = []
    moderate = []
    hot = []
    veryhot = []
    for l in f:
        if l == "cold\n":
            cold.append(int(f.readline().split("=")[1]))
            cold.append(int(f.readline().split("=")[1]))
            cold.append(int(f.readline().split("=")[1]))
            cold.append(int(f.readline().split("=")[1]))
        if l == "cool\n":
            cool.append(int(f.readline().split("=")[1]))
            cool.append(int(f.readline().split("=")[1]))
            cool.append(int(f.readline().split("=")[1]))
        if l == "moderate\n":
            moderate.append(int(f.readline().split("=")[1]))
            moderate.append(int(f.readline().split("=")[1]))
            moderate.append(int(f.readline().split("=")[1]))
        if l == "hot\n":
            hot.append(int(f.readline().split("=")[1]))
            hot.append(int(f.readline().split("=")[1]))
            hot.append(int(f.readline().split("=")[1]))
        if l == "veryhot\n":
            veryhot.append(int(f.readline().split("=")[1]))
            veryhot.append(int(f.readline().split("=")[1]))
            veryhot.append(int(f.readline().split("=")[1]))
            veryhot.append(int(f.readline().split("=")[1]))
    return cold, cool, moderate, hot, veryhot

def readCap(filename):
    f = open(filename, 'r')
    small = []
    medium = []
    high = []
    for l in f:
        if l == "small\n":
            small.append(int(f.readline().split("=")[1]))
            small.append(int(f.readline().split("=")[1]))
            small.append(int(f.readline().split("=")[1]))
        if l == "medium\n":
            medium.append(int(f.readline().split("=")[1]))
            medium.append(int(f.readline().split("=")[1]))
            medium.append(int(f.readline().split("=")[1]))
        if l == "high\n":
            high.append(int(f.readline().split("=")[1]))
            high.append(int(f.readline().split("=")[1]))
            high.append(int(f.readline().split("=")[1]))
    return small, medium, high
