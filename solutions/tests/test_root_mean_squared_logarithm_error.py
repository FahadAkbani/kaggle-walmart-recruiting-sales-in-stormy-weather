from solutions.core.evaluation.rmsle_evaluation import RootMeanSquaredLogarithmError as rmsle
import unittest
import random

class TestRootMeanSquaredLogarithmError(unittest.TestCase):

    def test_rmsle(self):

        random.seed(1000)
        N = 550000

        max_error = [0.005, 0.01, 0.1, 0.3, 0.5]
        results = [0.00, 0.01, 0.1, 0.26, 0.41]

        for experiment in xrange(len(results)):

            actual_list = map(lambda _: random.randint(1,N), xrange(N))
            predict_list = map(lambda _: actual_list[_] * (1+max_error[experiment]) , xrange(N))
            rsmle_value = rmsle.evaluate(predict_list, actual_list)
            self.assertEqual(round(rsmle_value, 2), round(results[experiment], 2))

            print 'exp: {0}, max_error: {1}, rsmle: {2}'.format((experiment+1), max_error[experiment], rsmle_value) 

if __name__ == '__main__':
    unittest.main()
        

