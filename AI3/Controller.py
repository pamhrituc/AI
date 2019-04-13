from random import randint, random
from Particle import *
def population(count, l, vmin, vmax):
    return [ Particle(l, vmin, vmax) for x in range(count) ]

def selectNeighbours(population, nSize):
    neighbours = []
    if nSize > len(population):
        nSize = len(population)
    elif nSize == len(population):
        localNeighbour = []
        for i in range(0, nSize):
            for j in range(1, nSize + 1):
                localNeighbour.append(j)
            shuffle (localNeighbour)
            neighbours.append(localNeighbour.copy())
        return neighbours


    for i in range(0, len(population)):
        localNeighbour = []
        for j in range(nSize):
            x = randint(0, len(population) - 1)
            while x in localNeighbour:
                x = randint(0, len(population) - 1)
            localNeighbour.append(x)
        neighbours.append(localNeighbour.copy())
    return neighbours

def iteration(population, neighbours, c1, c2, w):
    bestNeighbours = []
    for i in range(len(population)):
        bestNeighbours.append(neighbours[i][0])
        for j in range(1, len(neighbours[i])):
            if population[bestNeighbours[i]].fit > population[neighbours[i][j]].fit:
                bestNeighbours[i] = neighbours[i][j]

    for i in range(0, len(population)):
        for j in range(len(population[0].velocity)):
            newVelocity = w * population[i].velocity[j]
            newVelocity += c1 * random() * (population[bestNeighbours[i]].position[j] - population[i].position[j])
            newVelocity += c2 * random() * (population[i].bestPosition[j] - population[i].position[j])
            population[i].velocity[j] = newVelocity

    for i in range(0, len(population)):
        newPosition = []
        for j in range(len(population[0].velocity)):
            newPosition.append(population[i].position[j] + population[i].velocity[j])
        population[i].position = newPosition
    return population
