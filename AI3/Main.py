from Controller import *
from Particle import *
from matplotlib import pyplot as plt
from statistics import *

def readFromFile(fileName):
    f = open(fileName, 'r')
    noParticles = int(f.readline())
    dimParticle = int(f.readline())
    vmin = int(f.readline())
    vmax = int(f.readline())
    w = float(f.readline())
    c1 = int(f.readline())
    c2 = float(f.readline())
    sizeOfNeighbourhood = int(f.readline())
    return noParticles, dimParticle, vmin, vmax, w, c1, c2, sizeOfNeighbourhood

def readIt(fileName):
    f = open(fileName, 'r')
    noIteration = int(f.readline())
    return noIteration

def run():
    noIteration = readIt("it.in")
    noParticles, dimParticle, vmin, vmax, w, c1, c2, sizeOfNeighbourhood = readFromFile("data.in")
    P = population(noParticles, dimParticle, vmin, vmax)

    neighbourhoods = selectNeighbours(P, sizeOfNeighbourhood)

    for i in range(0, noIteration):
        P = iteration(P, neighbourhoods, c1, c2, w/(i+1))

    best = 0
    for i in range(1, len(P)):
        if (P[i].fit < P[best].fit):
            best = i

    fitnessOptim = P[best].fit
    individualOptim = P[best].position
    print('The detected minimum point is (%3.2f %3.2f) \n with function\'s value %3.2f' % (individualOptim[0], individualOptim[1], fitnessOptim))

    return fitnessOptim


def main():
    runNo = readIt("run.in")
    sample = []
    for i in range(0, runNo):
        f = run()
        sample.append(f)
    plt.plot(sample)
    plt.show()
    sd = stdev(sample)
    m = mean(sample)
    print("Standard deviation %3.2f" % sd)
    print("Mean %3.2f" % m)

main()
