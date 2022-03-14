import os
import unittest

from lightshows import Grid
from lightshows.DataSource import DataSource
from lightshows.Grid import Grid
from lightshows.LigtsCalculatorImpl import LightsCalculatorImpl
from lightshows.ReadInstructionsImpl import ReadInstructionsImpl



class MockDataSource(DataSource):
    def getSourceData(self):
        return os.path.abspath('TestData.txt')


# @todo add unit tests for both parts

class MyTestCase(unittest.TestCase):


    def test_Integration(self):
        sd = MockDataSource()
        ins = ReadInstructionsImpl()
        listOfInstructions = ins.getListOfInstructions(sd)
        LightsCalculatorImpl.calculateLights(LightsCalculatorImpl,listOfInstructions)

        result = sum(sum(Grid.getGrid(Grid)))
        expected = 1003996

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
