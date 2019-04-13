from matplotlib import pyplot as plt
from Algorithm import *
from Individ import *
from Population import *
from Problem import *

def printMainMenu():
    s = ""
    s += "\t1. EA & Plot\n"
    s += "\t2. Statistics\n"
    s += "\t0. exit\n"
    s += "your choice: "
    print(s)

def main():
    while True:
        prob = Problem() #create problem
        size = prob.loadData("data01.in") #load data of problem, return board size
        x = Individ([0] * size)
        pop = Population(x)
        alg = Algorithm(pop)
        alg.readParameters("param.in")
        printMainMenu()
        x = input()
        if x == "1":
            bestX, sample = alg.run()
            print(bestX)
            print(bestX.fitness())
            plt.plot(sample)
            # function to show the plot
            plt.show()
        if x == "2":
            alg.run()
            sd, m = alg.statistics()
            print("Standard deviation " + str(sd))
            print("Mean " + str(m))
        if x == "0":
            return
