from Model import *
from Controller import *
from View import *
#print(readTemp("temperature.in"))

model = Model()
ctrl = Controller(model)
view = View(ctrl)
view.run()
