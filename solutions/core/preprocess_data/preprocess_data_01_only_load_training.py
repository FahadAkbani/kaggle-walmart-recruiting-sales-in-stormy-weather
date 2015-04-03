from solutions.core.preprocess_data.abstract_preprocess_data import AbstractPreprocessData
from solutions.configuration.constant import Constant

class PreprocessData01OnlyLoadTraining(AbstractPreprocessData):

    def preprocess(self):
        self.training_df = self.train_raw_data
        self.test_df = self.train_raw_data
        return self.training_df, self.test_df
