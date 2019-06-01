from Controller import *
from Model import *

class View:
    def __init__(self, ctrl):
        self.__ctrl = ctrl

    def printRunResults(self, temp, cap, tempClass, capClass, smallClass, mediumClass, highClass):
        result = ""
        result += "Temperature " + str(temp) + "\n"
        result += "Capacity " + str(cap) + "\n"

        result += "The value of the temperature in the cold part " + str(tempClass[0]) + "\n"
        result += "The value of the temperature in the cool part " + str(tempClass[1]) + "\n"
        result += "The value of the temperature in the moderate part " + str(tempClass[2]) + "\n"
        result += "The value of the temperature in the hot part " + str(tempClass[3]) + "\n"
        result += "The value of the temperature in the very hot part " + str(tempClass[4]) + "\n"

        result += "The value of the capacity in the small part " + str(capClass[0]) + "\n"
        result += "The value of the capacity in the medium part " + str(capClass[1]) + "\n"
        result += "The value of the capacity in the high part " + str(capClass[2]) + "\n"

        result += "cold and small " + str(smallClass[0]) + "\n"
        result += "cool and small " + str(smallClass[1]) + "\n"
        result += "moderate and small " + str(smallClass[2]) + "\n"
        result += "hot and small " + str(smallClass[3]) + "\n"
        result += "veryhot and small " + str(smallClass[4]) + "\n"
        result += "moderate and medium " + str(smallClass[5]) + "\n"
        result += "hot and medium " + str(smallClass[6]) + "\n"
        result += "veryhot and medium " + str(smallClass[7]) + "\n"
        result += "moderate and high " + str(smallClass[8]) + "\n"
        result += "hot and high " + str(smallClass[9]) + "\n"
        result += "veryhot and high " + str(smallClass[10]) + "\n"

        result += "cold and medium " + str(mediumClass[0]) + "\n"
        result += "cool and medium " + str(mediumClass[1]) + "\n"

        result += "cold and high " + str(highClass[0]) + "\n"
        result += "cool and high " + str(highClass[1]) + "\n"
        return result

    def run(self):
        ctrl = self.__ctrl
        model = ctrl.getModel()
        temp = model.getTemp()
        cap = model.getCap()
        cold = model.getCold() #trapezoid
        cool = model.getCool()
        moderate = model.getModerate()
        hot = model.getHot()
        veryhot = model.getVeryHot() #trapezoid
        small = model.getSmall()
        medium = model.getMedium()
        high = model.getHigh()

        tempClass = []
        tempClass.append(ctrl.trapezoidal(temp, cold))
        tempClass.append(ctrl.triangular(temp, cool))
        tempClass.append(ctrl.triangular(temp, moderate))
        tempClass.append(ctrl.triangular(temp, hot))
        tempClass.append(ctrl.trapezoidal(temp, veryhot))

        capClass = []
        capClass.append(ctrl.triangular(cap, small))
        capClass.append(ctrl.triangular(cap, medium))
        capClass.append(ctrl.triangular(cap, high))


        smallClass = []
        smallClass.append(min(tempClass[0], capClass[0])) #cold and small
        smallClass.append(min(tempClass[1], capClass[0])) #cool and small
        smallClass.append(min(tempClass[2], capClass[0])) #moderate and small
        smallClass.append(min(tempClass[3], capClass[0])) #hot and small
        smallClass.append(min(tempClass[4], capClass[0])) #veryhot and small
        smallClass.append(min(tempClass[2], capClass[1])) #moderate and medium
        smallClass.append(min(tempClass[3], capClass[1])) #hot and medium
        smallClass.append(min(tempClass[4], capClass[1])) #veryhot and medium
        smallClass.append(min(tempClass[2], capClass[2])) #moderate and high
        smallClass.append(min(tempClass[3], capClass[2])) #hot and high
        smallClass.append(min(tempClass[4], capClass[2])) #veryhot and high
        smallClassValue = max(smallClass)

        mediumClass = []
        mediumClass.append(min(tempClass[0], capClass[1])) #cold and medium
        mediumClass.append(min(tempClass[1], capClass[1])) #cool and medium
        mediumClassValue = max(mediumClass)

        highClass = []
        highClass.append(min(tempClass[0], capClass[2])) #cold and high
        highClass.append(min(tempClass[1], capClass[2])) #cool and high
        highClassValue = max(highClass)

        string = self.printRunResults(temp, cap, tempClass, capClass, smallClass, mediumClass, highClass)
        string += "Value for small class " + str(smallClassValue) + "\n"
        string += "Value for medium class " + str(mediumClassValue) + "\n"
        string += "Value for high class " + str(highClassValue) + "\n"

        p = (5 * smallClassValue + 10 * mediumClassValue + 15 * highClassValue) / (smallClassValue + mediumClassValue + highClassValue)
        string += "P = " + str(p) + "\n"
        print(string)
        self.writeToFile("output.out", string)

    def writeToFile(self, filename, string):
        f = open(filename, 'w')
        f.write(string)
        f.close
