from lightshows.Grid import Grid
from lightshows.LightsCalculator import LightsCalculator

class LightsCalculatorImpl2(LightsCalculator):


    def calculateLights2(self, listOfInstructions):
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

                            prev = Grid.getValueWithCoords(grid, x, y)
                            Grid.setValueWithCoords(grid,prev + 1,x,y)

                    elif currentCommand.find(turnOff) != -1:

                            curr = Grid.getValueWithCoords(grid, x, y) - 1
                            Grid.setValueWithCoords(grid,max(0,curr),x,y)

                    elif currentCommand.find(toggle) != -1:
                        prev = Grid.getValueWithCoords(grid, x, y)
                        Grid.setValueWithCoords(grid,prev + 2, x, y)
