from random import randint, random
from copy import deepcopy
from math import sin, cos
def readFromFile(filename):
    f = open(filename, 'r')
    input = []
    output = []
    f.readline()
    for line in f:
        input_aux = []
        output_aux = []
        input_aux.append(int(line.split(",")[0])) #subject#
        output_aux.append(input_aux[0])
        input_aux.append(int(line.split(",")[1])) #age
        input_aux.append(int(line.split(",")[2])) #sex
        input_aux.append(float(line.split(",")[3])) #test_time
        output_aux.append(float(line.split(",")[4])) #motor_UPDRS
        output_aux.append(float(line.split(",")[5])) #total_UPDRS
        input_aux.append(float(line.split(",")[6])) #Jitter(%)
        input_aux.append(float(line.split(",")[7])) #Jitter(Abs)
        input_aux.append(float(line.split(",")[8])) #Jitter:RAP
        input_aux.append(float(line.split(",")[9])) #Jitter:PPQ5
        input_aux.append(float(line.split(",")[10])) #Jitter:DDP
        input_aux.append(float(line.split(",")[11])) #Shimmer
        input_aux.append(float(line.split(",")[12])) #Shimmer(dB)
        input_aux.append(float(line.split(",")[13])) #Shimmer:APQ3
        input_aux.append(float(line.split(",")[14])) #Shimmer:APQ5
        input_aux.append(float(line.split(",")[15])) #Shimmer:APQ11
        input_aux.append(float(line.split(",")[16])) #Shimmer:DDA
        input_aux.append(float(line.split(",")[17])) #NHR
        input_aux.append(float(line.split(",")[18])) #HNR
        input_aux.append(float(line.split(",")[19])) #RPDE
        input_aux.append(float(line.split(",")[20])) #DFA
        input_aux.append(float(line.split(",")[21])) #PPE
        input.append(input_aux)
        output.append(output_aux)
    return input, output

def scaleValues(arr):
    mi = min(arr[1:])
    ma = max(arr[1:])
    for i in range(1, len(arr)):
        arr[i] = (arr[i] - mi) / (ma - mi)
    return arr

def scaleOutput(arr):
    for i in range(1, len(arr)):
        arr[i] /= 100
    return arr

DEPTH_MAX = 5
terminals, results = readFromFile("data.csv")
for t in terminals:
    t = scaleValues(t)
    
for r in results:
    r = scaleOutput(r)
    
noTerminals = 18
functions = ['+','-','*', 'sin', 'cos']
noFunctions = 5

class Chromosome:
    def __init__(self, d = DEPTH_MAX):
        self.mDepth = d
        self.repres = [0 for i in range(2 ** (self.mDepth + 1) - 1)]
        self.fitness = 0
        self.size = 0

    def growExpression(self, pos = 0, depth = 0):
        """
        initialise randomly an expression
        """
        if (pos == 0) or (depth < self.mDepth):
            if random() < 0.3:
                self.repres[pos] = randint(1, noTerminals)
                self.size = pos + 1
                return pos + 1
            else:
                self.repres[pos] = -randint(1, noFunctions)
                finalFirstChild = self.growExpression(pos + 1, depth + 1)
                finalSecondChild = self.growExpression(finalFirstChild, depth + 1)
                return finalSecondChild
        else:
                #choose a terminal
            self.repres[pos] = randint(1, noTerminals)
            self.size = pos + 1
            return pos + 1

    def evalExpression(self, pos, crtData):
        """
        the expresion value for some specific terminals
        """
        if  self.repres[pos] > 0: # a terminal
            return crtData[self.repres[pos] - 1], pos    
        elif self.repres[pos] < 0:  #a function
            if functions[-self.repres[pos] - 1] == '+':
                auxFirst = self.evalExpression(pos + 1, crtData)
                auxSecond = self.evalExpression(auxFirst[1] + 1, crtData)
                return auxFirst[0] + auxSecond[0], auxSecond[1]
            elif functions[-1 - self.repres[pos]] == '-':
                auxFirst = self.evalExpression(pos + 1, crtData)
                auxSecond = self.evalExpression(auxFirst[1] + 1, crtData)
                return auxFirst[0] - auxSecond[0], auxSecond[1]
            elif functions[-1 - self.repres[pos]] == '*':
                auxFirst = self.evalExpression(pos + 1, crtData)
                auxSecond = self.evalExpression(auxFirst[1] + 1, crtData)
                return auxFirst[0] * auxSecond[0], auxSecond[1]
            elif functions[-1 - self.repres[pos]] == 'sin':
                auxFirst = self.evalExpression(pos + 1, crtData)
                auxSecond = self.evalExpression(auxFirst[1] + 1, crtData)
                return sin(auxFirst[0]), auxSecond[1]
            elif functions[-1 - self.repres[pos]] == 'cos':
                auxFirst = self.evalExpression(pos + 1, crtData)
                auxSecond = self.evalExpression(auxFirst[1] + 1, crtData)
                return cos(auxFirst[0]), auxSecond[1]

    def computeFitness(self, crtData, crtOut, noExamples):
        '''
        the fitness function
        '''
        err = 0.0
        for d in range(1, noExamples - 1):
            err += abs(crtOut[d][1] - self.evalExpression(0, crtData[d])[0])
        self.fitness = err

    def traverse(self, pos):
        '''
        returns the next index where it begins the next 
        branch in the tree from the same level
        '''
        if (self.repres[pos] > 0):	 #terminal
            return pos + 1
        else:
            return self.traverse(self.traverse(pos + 1))

def crossover(M, F):
    off = Chromosome()
    while True:
        startM = randint(0, M.size - 1)
        endM = M.traverse(startM)
        startF = randint(0, F.size - 1)
        endF = F.traverse(startF)
        if (len(off.repres) > endM + (endF - startF - 1) + (M.size - endM - 1)):
            break
    i = -1
    for i in range(startM):
        off.repres[i] = M.repres[i]
    for j in range(startF, endF):
        i = i + 1
        off.repres[i] = F.repres[j]
    for j in range(endM, M.size):
        i = i + 1
        off.repres[i] = M.repres[j]
    off.size = i + 1
    return off

def mutation(c):
    off = Chromosome()
    pos = randint(0, c.size)
    off.repres = c.repres[:]
    off.size = c.size
    if off.repres[pos] > 0:	#terminal
        off.repres[pos] = randint(1, noTerminals)
    else:	#function
        off.repres[pos] = -randint(1, noFunctions)
    return off

class Population:
    def __init__(self, size):
        self.size = size
        self.population = []
        for i in range(size):
            p = Chromosome()
            self.population.append(p)
            
    def iteration(self):
        i1 = 0
        i2 = 0
        while i1 == i2:
            i1 = randint(0, self.size - 1)
            i2 = randint(0, self.size - 1)
        
        p1 = self.population[i1]
        p2 = self.population[i2]
        
        p1.growExpression()
        p2.growExpression()
        
        cP = randint(1, 100)
        if cP <= 90:
            child = crossover(p1, p2)
            mP = randint(1, 100)
            if mP <= 10:
                child = mutation(child)
            
            p1.computeFitness(terminals, results, noTerminals)
            p2.computeFitness(terminals, results, noTerminals)
            child.computeFitness(terminals, results, noTerminals)
            mi = min(p1.fitness, p2.fitness, child.fitness)
            ma = max(p1.fitness, p2.fitness, child.fitness)
            if mi == p1.fitness:
                #print("p1")
                #print(p1.repres)
                #print(p1.fitness)
                if ma == p2.fitness:
                    self.population[i2] = deepcopy(child)
                return p1#.repres
            elif mi == p2.fitness:
                #print("p2")
                #print(p2.repres)
                #print(p2.fitness)
                if ma == p1.fitness:
                    self.population[i1] = deepcopy(child)
                return p2#.repres
            else:
                #print("child")
                #print(child.repres)
                #print(child.fitness)
                if ma == p2.fitness:
                    self.population[i2] = deepcopy(child)
                else:
                    self.population[i1] = deepcopy(child)
                return child#.repres
            
    def run(self):
        runNo = 0
        bestIndiv = []
        while runNo < 10000:
            #print("Run No #" + str(runNo))
            indiv = self.iteration()
            runNo += 1
            if indiv != None:
                bestIndiv.append(indiv.repres)
        return sorted(bestIndiv)
    
population = Population(50)
best = population.run()[0]
print(best)