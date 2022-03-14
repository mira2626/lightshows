from lightshows.Grid import Grid
from lightshows.LightsCalculator import LightsCalculator


class LightsCalculatorImpl(LightsCalculator):

    def calculateLights(self, listOfInstructions):
        grid = Grid()
        turnOn = "turn on"
        turnOff = "turn off"
        toggle = "toggle"

        for i in listOfInstructions:
            currentCommand = i.command.lower()
            (startY,startX) = i.start.split(',')
            (finnishY,finnishX) = i.finnish.split(',') # @todo this logic could be moved to lower level

            for x in range(int(startX), int(finnishX)+1): # @todo handle bad input data & exceptions
                for y in range(int(startY), int(finnishY)+1):

                    if currentCommand.find(turnOn) != -1:

                        if Grid.getValueWithCoords(grid,x,y) == 0:
                            Grid.setValueWithCoords(grid,1,x,y)

                    elif currentCommand.find(turnOff) != -1:

                        if Grid.getValueWithCoords(grid,x,y) == 1:
                            Grid.setValueWithCoords(grid,0,x,y)

                    elif currentCommand.find(toggle) != -1:
                        if Grid.getValueWithCoords(grid, x, y) == 1:
                            Grid.setValueWithCoords(grid, 0, x, y)
                        elif Grid.getValueWithCoords(grid, x, y) == 0:
                            Grid.setValueWithCoords(grid, 1, x, y)

