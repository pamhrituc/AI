from random import *
from copy import *
from math import *
from Population import *
class Individ:
    def __init__(self, x):
        self.__indiv = x #permutation represented as a list
        self.__size = len(self.__indiv)

    def setSize(self, n):
        self.__size = n

    def getIndivid(self):
        return self.__indiv

    def get(self, n):
        return self.__indiv[n]

    def set(self, n, x):
        self.__indiv[n] = x

    def __str__(self):
        return str(self.__indiv)

    def crossover(self, indiv2):
        '''
        Function that performs the crossover between two individuals
        '''
        i1 = 0
        i2 = 0
        n = self.__size
        indiv1 = Individ(self.__indiv)
        aux1 = [0] * n
        aux2 = [0] * n
        i = randint(1, n - 1)
        j = randint(i + 1, n)
        for k in range(i, j):
            aux1[k] = indiv1.get(k)
            aux2[k] = indiv2.get(k)
        for k in range(0, n):
            if i1 == i:
                i1 = j
            if i2 == i:
                i2 = j
            if indiv2.get(k) not in aux1 and aux1[i1] == 0:
                aux1[i1] = indiv2.get(k)
                i1 += 1
            if indiv1.get(k) not in aux2 and aux2[i2] == 0:
                aux2[i2] = indiv1.get(k)
                i2 += 1
        return Individ(aux1), Individ(aux2)

    def mutate(self):
        '''
        Function that mutates one individ
        '''
        n = self.__size
        r1 = randint(0, n - 1)
        r2 = randint(0, n - 1)
        indiv = self.__indiv
        indiv[r1], indiv[r2] = indiv[r2], indiv[r1]
        return Individ(indiv)

    def fitness(self):
        '''
        Function that returns the fitness level
        '''
        m = self.__size
        #print(m)
        n = int(sqrt(m))
        #print(n)
        indiv = self.__indiv
        k = 0
        for i in range(0, m - 1):
            if abs(indiv[i] - indiv[i + 1]) == n + 2:
                k += 1
            if abs(indiv[i] - indiv[i + 1]) == n - 2:
                k += 1
            if abs(indiv[i] - indiv[i + 1]) == 2 * n + 1:
                k += 1
            if abs(indiv[i] - indiv[i + 1]) == 2 * n - 1:
                k += 1
        return k

    def generate(self):
        '''
        Function that generates a random individ
        '''
        n = self.__size
        for i in range(1, n + 1):
            self.__indiv[i - 1] = i
        shuffle (self.__indiv)
        return self.__indiv
