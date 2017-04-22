import unittest
import pandas as pd
import os

class InputOutTest(unittest.TestCase):

    def setUp(self):
        self.file_location = os.path.join(os.path.dirname(__file__), 'EcommercePurchases.csv')

    def test_read_csv(self):
        data_frame = pd.read_csv(self.file_location)
