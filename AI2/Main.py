from random import *
from Individ import *
from Population import *
from Algorithm import *
from App import *
'''
p1 = Individ([1, 5, 6, 3, 2, 4, 7, 8])
p2 = Individ([3, 1, 5, 7, 2, 4, 6, 8])
p1, p2 = p1.crossover(p2)
print(p1)
print(p2)
p1.mutate()
print(p1)
''
p3 = Individ([0] * 8)
print(p3.generate())
''
pop = Population(p3)
for i in pop.getPopulation():
    print(i)

p1 = Individ([0] * 64)
print(p1.generate())
print(p1.fitness())

pop = Population(Individ([0] * 9))
print("before")
for i in pop.getPopulation():
    print(i)
alg = Algorithm(pop)
alg.readParameters("param.in")
alg.run()
print("after")
for i in pop.getPopulation():
    print(i)
'''
main()
'''
p1 = Individ([1, 11] * 32)
#print(p1.generate())
print(p1.fitness())
'''
