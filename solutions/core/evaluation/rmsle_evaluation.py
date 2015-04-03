from __future__ import division
import math

class RootMeanSquaredLogarithmError(object):

    @staticmethod
    def evaluate(predict_list, actual_list):
        n = len(predict_list)
        sle = sum(map(lambda index: RootMeanSquaredLogarithmError.calculate_rmsle(predict_list[index], actual_list[index]), xrange(n))) 
        rmsle = math.sqrt(1/n * sle)

        return rmsle

    @staticmethod
    def calculate_rmsle(predicted_value, actual_value):
        return (math.log(predicted_value + 1) - math.log(actual_value + 1))**2
