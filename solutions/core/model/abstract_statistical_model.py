from abc import ABCMeta, abstractmethod

class AbstractStatisticalModel(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.stats_model = self.setup_model()

    @abstractmethod
    def setup_model(self):
        """
        Return a stats model.
        """
        pass

    def training(self, training_df):
        self.stats_model.fit(training_df)

    def predict(self, predict_df):
        return self.stats_model.predict(predict_df)
