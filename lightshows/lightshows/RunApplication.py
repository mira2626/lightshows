from lightshows.DataSourceImpl import DataSourceImpl
from lightshows.Grid import Grid
from lightshows.LigtsCalculatorImpl import LightsCalculatorImpl
from lightshows.ReadInstructionsImpl import ReadInstructionsImpl


class RunApplication():
# @todo handle versioning (with tags?)
# @todo handle packaging and distribution

    def main(self):

        listOfInstructions = ReadInstructionsImpl().getListOfInstructions(DataSourceImpl())
        LightsCalculatorImpl.calculateLights(LightsCalculatorImpl,listOfInstructions)

        print(sum(sum(Grid.getGrid(Grid))))


if __name__ == '__main__':
        RunApplication().main()