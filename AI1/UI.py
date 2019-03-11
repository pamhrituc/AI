from Controller import *

class UI:
    def __init__(self):
        self.__s = State([])
        #self.__s.readFromFile("ex3.txt")
        self.__ctrl = Controller(self.__s)

    def printMainMenu(self):
        s = ""
        s += "~Sudoku~\n"
        s += "\t1. bfs\n"
        s += "\t2. gbfs\n"
        s += "\t0. exit\n"
        s += "your choice: "
        print(s)

    def run(self):
        while True:
            self.__s.readFromFile("ex3.txt")
            self.printMainMenu()
            x = input()
            if x == "1":
                self.__ctrl.bfs(self.__s.getMatrix())
            if x == "2":
                self.__ctrl.gbfs(self.__s)
            if x == "0":
                return
