from random import randint, random
from operator import add
from math import *
class Particle:
    def __init__(self, l, vmin, vmax):
        '''
        l: no of components
        vmin: the minimum possible value
        vamx: the maximum possible value
        '''
        self.__position = [(random() * (vmax - vmin) + vmin) for x in range(0, l)]
        self.evaluate()
        self.velocity = [0 for i in range(0, l)]

        self.__bestPosition = self.__position.copy()
        self.__bestFitness = self.__fit

    def fitness(self, position):
        n = len(position)
        f = 0
        for i in range(0, n - 1):
            y = pow(position[i], 2) + pow(position[i + 1], 2)
            z = cos(2 * pi * position[i]) + cos(2 * pi * position[i + 1])
            f += (-20) * pow(e, (-0.2) * sqrt(0.5 * y)) - pow(e, 0.5 * z) + e + 20
        return f

    def evaluate(self):
        self.__fit = self.fitness(self.__position)

    @property
    def position(self):
        """ getter for pozition """
        return self.__position

    @property
    def fit(self):
        """ getter for fitness """
        return self.__fit

    @property
    def bestPosition(self):
        """ getter for best pozition """
        return self.__bestPosition

    @property
    def bestFitness(self):
        """getter for best fitness """
        return self.__bestFitness

    @position.setter
    def position(self, newPosition):
        self.__position = newPosition.copy()
        # automatic evaluation of particle's fitness
        self.evaluate()
        # automatic update of particle's memory
        if (self.__fit < self.__bestFitness):
            self.__bestPosition = self.__position
            self.__bestFitness  = self.__fit
