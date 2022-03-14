from abc import ABC, abstractmethod


class ReadInstructions(ABC):

    @abstractmethod
    def getListOfInstructions(self):
        pass