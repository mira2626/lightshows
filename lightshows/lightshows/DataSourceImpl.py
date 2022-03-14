import os

from lightshows.DataSource import DataSource


class DataSourceImpl(DataSource):

 def getSourceData(self):
  filename = os.path.abspath('../docs/coding_challenge_input.txt') #TODO READ IT FROM DOCS?
  return filename
