from Neuron import *
from Layer import *
from Function import *

input, output = readFromFile("data.txt")
layer0Weights = []
layer0 = Layer(15, 6) #15 neurons with 6 inputs each; connects input w/ hidden
for neuron in layer0.neurons:
    layer0Weights.append(neuron.weights)

layer1Weights = []
layer1 = Layer(3, 15) #3 neurons with 15 inputs each; connects hidden w/ output
for neuron in layer1.neurons:
    layer1Weights.append(neuron.weights)

for i in range(0, len(input)):
    for j in range(0, 10000):

        input[i] = scaleValues(input[i])
        l0 = input[i]

        layer0WeightsT = array(layer0Weights).T
        layer1WeightsT = array(layer1Weights).T

        #dot product in between input layer and weights
        d0 = dot(input[i], layer0WeightsT)
        l1 = sigmoid(d0)

        #the dot product between the result of the previous layer and the weights of the current layer
        d1 = dot(l1, layer1WeightsT)
        l2 = sigmoid(d1)

        l2_error = (output[i] - l2) #* (output[i] - l2)

        #backward propagation
        l2_delta = l2_error * sigmoidPrime(l2) #adjust weights for hidden-output

        l1_error = dot(l2_delta, layer1Weights)
        l1_delta = l1_error * sigmoidPrime(l1)

        '''
        if j % 1000 == 0:
            print("Actual output")
            print(l2_error)
            #print("L1")
            #print(l1_error)
            #print("sig " + str(l1))
            print ("Error: " + str(mean(abs(l2_error))))
        '''

        #update weights
        layer1Weights += dot(l2, l2_delta)
        layer0Weights += dot(l1, l1_delta)

    print("Study case " + str(i + 1) + ": " + classify(l2_error[0], l2_error[1], l2_error[2]))
