from abc import ABC, abstractmethod


class LightsCalculator(ABC):

    @abstractmethod
    def calculateLights(self):
        pass