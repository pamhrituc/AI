import math
class State:
    def __init__(self, matrix):
        self.__matrix = matrix
        if self.__matrix == []:
            self.__dim = 0
        else:
            self.__dim = len(matrix[1])

    def getMatrix(self):
        return self.__matrix

    def setMatrix(self, m):
        self.__matrix = m

    def getDim(self):
        return self.__dim

    def setElem(self, i, j, x):
        self.__matrix[i][j] = x

    def __str__(self):
        s = ""
        for i in self.__matrix:
            for j in i:
                s += str(j)
                s += " "
            s += "\n"
        return s

    def checkBox(self, k, l):
        nList = []
        n = self.__dim
        sq = int(math.sqrt(n))
        for i in range(1, n + 1):
            nList.append(i)
        for i in range(0 + k, sq + k):
            for j in range(0 + l, sq + l):
                #print(self.__matrix[i][j])
                if self.__matrix[i][j] not in nList:
                    return False
                else:
                    nList.remove(self.__matrix[i][j])
        return True

    def isSolution(self):
        n = self.__dim
        sq = int(math.sqrt(n))
        for line in self.__matrix:
            lSet = list(set(line))
            orLine = sorted(line)
            #print(orLine)
            if lSet != orLine:
                return False
        for j in range(0, n):
            for i in range(0, n - 1):
                if self.__matrix[i][j] == self.__matrix[i + 1][j]:
                    return False
        for k in range(0, n, sq):
            for l in range(0, n, sq):
                if self.checkBox(k, l) == False:
                    return False
        return True

    def readFromFile(self, fileName):
        mtx = []
        f = open(fileName, 'r')
        n = int(f.readline())
        for x in f:
            li = []
            for i in x:
                if i != ' ' and i != '\n':
                    li.append(int(i))
            mtx.append(li)
        self.__matrix = mtx
        self.__dim = n

    def expand(self, state):
        n = self.__dim
        for i in range(0, n):
            for j in range(0, n):
                #print("Cond " + str(state.getMatrix()[i][j] != self.__matrix[i][j]))
                #print(state.getMatrix()[i][j])
                #print(self.__matrix[i][j])
                x = state.getMatrix()[i][j]
                if (state.getMatrix()[i][j] != self.__matrix[i][j]) and state.getMatrix()[i][j] < n:
                    state.setElem(i, j, x + 1)
                    return state
                if int(state.getMatrix()[i][j]) == 0:
                    state.setElem(i, j, x + 1)
                    return state

    def checkBoxZ(self, k, l):
        nList = []
        n = self.__dim
        sq = int(math.sqrt(n))
        for i in range(1, n + 1):
            nList.append(i)
        for i in range(0 + k, sq + k):
            for j in range(0 + l, sq + l):
                if self.__matrix[i][j] != 0:
                    if self.__matrix[i][j] not in nList:
                        return False
                    else:
                        nList.remove(self.__matrix[i][j])
        return True

    def isValid(self):
        n = self.__dim
        sq = int(math.sqrt(n))
        for i in range(0, n):
            for j in range(0, n):
                for k in range(j + 1, n):
                    if (self.__matrix[i][j] == self.__matrix[i][k]) and self.__matrix[i][j] != 0:
                        return False
        for j in range(0, n):
            for i in range(0, n):
                for k in range(i + 1, n):
                    if self.__matrix[i][j] == self.__matrix[k][j] and int(self.__matrix[i][j]) != 0:
                        return False
        for k in range(0, n, sq):
            for l in range(0, n, sq):
                if self.checkBoxZ(k, l) == False:
                    return False
        return True

    def difference(self, state):
        mtx = self.__matrix
        n = self.__dim
        for i in range(0, n):
            for j in range(0, n):
                if state.getMatrix()[i][j] != mtx[i][j]:
                    return state.getMatrix()[i][j]

    def freq(self, x):
        '''
        returns the frequency of an element
        '''
        k = 0 #the frequency
        mtx = self.__matrix
        for i in mtx:
            for j in i:
                if j == x:
                    k += 1
        return k

    def heuristic(self):
        nList = []
        n = self.__dim
        sq = int(math.sqrt(n))
        for i in range(1, n + 1):
            nList.append(i)
        freqList = {} #frequecy dictionary, w/ the numbers 0..n as keys & their respective
        for i in nList:
            j = self.freq(i)
            freqList[i] = j
        h = min(freqList.values())
        for key in freqList:
            if freqList[key] == h:
                return key
