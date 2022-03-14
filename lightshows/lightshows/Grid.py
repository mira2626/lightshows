import numpy as np


class Grid:

    rows = 1000 # y
    cols = 1000 # x
    #todo read them from confiq file

    gridValues = np.zeros((rows,cols))


    def updateGrid(self):
        #@todo
        return self.gridValues

    def getGrid(self):
        return self.gridValues

    def getValueWithCoords(self, x, y):
        return self.gridValues[x, y]

    def setValueWithCoords(self, value, x, y):
        self.gridValues[x, y] = value