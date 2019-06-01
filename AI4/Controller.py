from Model import *
class Controller:
    def __init__(self, m):
        self.__model = m

    def triangular(self, x, array):
        a = array[0]
        b = array[1]
        c = array[2]
        try:
            val1 = (x - a) / (b - a)
        except:
            val1 = float('inf')
        try:
            val2 = (c - x) / (c - b)
        except:
            val2 = float('inf')
        result = max(0, min(val1, 1, val2))
        return result

    def trapezoidal(self, x, array):
        a = array[0]
        b = array[1]
        c = array[2]
        d = array[3]
        try:
            val1 = (x - a) / (b - a)
        except:
            val1 = float('inf')
        try:
            val2 = (d - x) / (d - c)
        except:
            val2 = float('inf')
        result = max(0, min(val1, 1, val2))
        return result

    def getModel(self):
        return self.__model
