from solutions.configuration.constant import Constant
from pandas import DataFrame, read_csv
from abc import ABCMeta, abstractmethod

class AbstractPreprocessData(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self._load_data()

    @abstractmethod
    def preprocess(self):
        """
        Preprocess data and RETURNS a self.training_df and self.test_df
        """
        pass

    def _load_data(self):
        self.train_raw_data = read_csv(Constant.Filesystem.TRAIN_FILE) 
        self.test_raw_data = read_csv(Constant.Filesystem.TEST_FILE)
        self.weather_raw_data = read_csv(Constant.Filesystem.WEATHER_FILE)
        self.key_raw_data = read_csv(Constant.Filesystem.STORE_STATION_ID_FILE)
