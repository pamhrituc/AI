from numpy import *
def constant(x):
    return x

def constantPrime(x):
    return 1
    
def step():
    return

def linear(a, b, x):
    return a * x + b

def linearPrime(a, b, x):
    return a * x

def sigmoid(s):
    return 1/(1 + exp(-s))

def sigmoidPrime(s):
    return s * (1 - s)

def gaussian():
    return

def ReLU():
    return max(0, linear())
