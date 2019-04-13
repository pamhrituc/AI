from Individ import *
class Population:
    def __init__(self, indiv):
        self.__noIndiv = 10
        self.__v = []
        i = 0
        while i < self.__noIndiv:
            indiv.generate()
            #print(indiv)
            self.__v.append(deepcopy(indiv))
            i += 1

    def getPopulation(self):
        return self.__v

    def getSize(self):
        return self.__noIndiv

    def getIndiv(self, n):
        return self.__v[n]

    def setIndiv(self, n, val):
        self.__v[n] = val
