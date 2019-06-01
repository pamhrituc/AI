from random import *
from math import *
from numpy import *
class Neuron:
    def __init__(self, inputNo):
        self.inputNo = inputNo
        #random.seed(1)
        self.weights = [(random.random() * 2 - 1) for k in range(self.inputNo)]
        self.output = 0

    def activate(self, info):
        net = 0.0
        for i in range(self.inputNo):
            net += info[i] * self.weights[i]
        self.output = net
        #self.output = 1 / (1.0 + exp(-net)) #for sigmoidal activation

def readFromFile(filename):
    f = open(filename, 'r')
    input = []
    output = []
    for line in f:
        aux = []
        aux.append(float(line.split(",")[0]))
        aux.append(float(line.split(",")[1]))
        aux.append(float(line.split(",")[2]))
        aux.append(float(line.split(",")[3]))
        aux.append(float(line.split(",")[4]))
        aux.append(float(line.split(",")[5]))
        result = line.split(",")[6].split("\n")[0]
        if result == "Hernia":
            output.append([1, 0, 0])
        if result == "Spondylolisthesis":
            output.append([0, 1, 0])
        if result == "Normal":
            output.append([0, 0, 1])
        input.append(aux)
    return input, output

def scaleValues(arr):
    mi = min(arr)
    ma = max(arr)
    for i in range(0, len(arr)):
        arr[i] = (arr[i] - mi) / (ma - mi)
    return arr

def classify(o1, o2, o3):
    ma = max(o1, o2, o3)
    if ma == o1:
        return "Hernia"
    if ma == o2:
        return "Spondylolisthesis"
    return "Normal"
