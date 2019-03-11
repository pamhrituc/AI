from State import *
from Controller import *
from UI import *
import copy

'''
s = State([])
s.readFromFile("ex1.txt")

ss = State([[3, 4, 1, 2], [0, 1, 4, 0], [1, 2, 0, 4], [0, 3, 2, 1]])
s = copy.deepcopy(ss)
print(ss.heuristic())

ctrl = Controller(s)
print(ctrl.gbfs(s))
'''

ui = UI()
ui.run()
