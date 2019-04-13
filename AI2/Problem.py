from Individ import *
class Problem:
    def __init__(self):
        self.__boardSize = 0

    def loadData(self, fileName):
        f = open(fileName, 'r')
        n = int(f.readline())
        self.__boardSize = n * n
        return n

    def getBoardSize(self):
        return self.__boardSize
