from abc import ABC, abstractmethod

class DataSource(ABC):

 @abstractmethod
 def getSourceData(self):
  pass
