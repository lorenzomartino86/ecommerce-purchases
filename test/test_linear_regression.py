import unittest
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class LinearRegressionTest(unittest.TestCase):
    def test_train_test_split(self):
        X, y = np.arange(10).reshape((5,2)), range(5)
        print(X, y)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
        print(X_train, y_train)
        print(X_test, y_test)

        # Fit Training data
        regression = LinearRegression()
        regression.fit(X_train, y_train)

        # Predicting labels on the test set
        print(regression.predict(X_test))


if __name__ == '__main__':
    unittest.main()
