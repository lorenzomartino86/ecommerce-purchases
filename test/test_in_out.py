import unittest
import pandas as pd
import os

class InputOutTest(unittest.TestCase):

    def setUp(self):
        self.file_location = os.path.join(os.path.dirname(__file__), 'EcommercePurchases.csv')
        self.loaded_csv = os.path.join(os.path.dirname(__file__), 'test_load')
        self.url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'

    def test_read_csv(self):
        data_frame = pd.read_csv(self.file_location)
        dimensions = data_frame.shape
        total_rows = len(data_frame.index)
        self.assertEqual(10000, total_rows)
        self.assertEqual((10000, 14), dimensions)

    def test_load_csv(self):
        data_frame = pd.read_csv(self.file_location)
        data_frame.to_csv(self.loaded_csv, index=False)
        data_frame_loaded = pd.read_csv(self.loaded_csv)
        dimensions = data_frame_loaded.shape
        total_rows = len(data_frame_loaded.index)
        self.assertEqual(10000, total_rows)
        self.assertEqual((10000, 14), dimensions)
        os.remove(self.loaded_csv)

    def test_get_html(self):
        data_frame = pd.read_html(self.url)
        print (data_frame)
