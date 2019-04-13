from statistics import *
from Problem import *
class Algorithm:
    def __init__(self, pop):
        self.__probMut = 0
        self.__probCross = 0
        self.__popSize = 0
        self.__genNo = 0
        self.__pop = pop
        self.__indivSize = pop.getSize()

    def readParameters(self, fileName):
        '''
        probability of mutation and crossover, population size and  number of generations)
        '''
        f = open(fileName, 'r')
        self.__probMut = int(f.readline()) #probability of mutation
        self.__probCross = int(f.readline()) #probability of crossover
        self.__popSize = int(f.readline()) #population size
        self.__genNo = int(f.readline()) #number of generations

    def iteration(self):
        pop = self.__pop
        n = self.__indivSize
        i1 = randint(0, pop.getSize() - 1)
        i2 = randint(0, pop.getSize() - 1)
        #print(str(i1) + " and " + str(i2))
        if i1 != i2:
            p1 = pop.getIndiv(i1)
            p2 = pop.getIndiv(i2)
            cP = randint(1, 100)
            #print(str(cP) + " and " + str(self.__probCross))
            if cP <= self.__probCross:
                c1, c2 = p1.crossover(p2)
                mP = randint(1, 100)
                if mP <= self.__probMut:
                    c1.mutate()
                mP = randint(1, 100)
                if mP <= self.__probMut:
                    c2.mutate()
                f1 = p1.fitness()
                f2 = p2.fitness()
                fc1 = c1.fitness()
                fc2 = c2.fitness()
                if f1 == min(f1, f2, fc1, fc2):
                    if f2 == min(f2, fc1, fc2):
                        pop.setIndiv(i2, c2)
                    pop.setIndiv(i1, c1)
                if f2 == min(f1, f2, fc1, fc2):
                    if f1 == min(f1, fc1, fc2):
                        pop.setIndiv(i1, c1)
                    pop.setIndiv(i2, c2)
        return pop

    def run(self):
        genNo = self.__genNo
        fitnessList = []
        for i in range(0, genNo):
            self.iteration()
        bestFitness = 0
        for x in self.__pop.getPopulation():
            f = x.fitness()
            fitnessList.append(f)
            if f > bestFitness:
                bestFitness = f
                bestX = x
        #print("bestX")
        return bestX, fitnessList

    def statistics(self):
        sample = []
        for i in range(0, 40):
            x, s = self.run()
            sample.append(x.fitness())
        sd = stdev(sample)
        m = mean(sample)
        #print("Standard deviation " + str(sd))
        #print("Mean " + str(m))
        return sd, m

    def getMutationProb(self):
        return self.__probMut

    def getCrossoverProb(self):
        return self.__probCross

    def getPopulationSize(self):
        return self.__popSize

    def getGenerationNo(self):
        return self.__genNo
