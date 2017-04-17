import unittest
import numpy as np
import pandas as pd

class MissingDataTest(unittest.TestCase):

    def setUp(self):
        dictionary = {'A':[1,2,np.nan], 'B':[5,np.nan,np.nan], 'C':[1,2,3]}
        self.data_frame = pd.DataFrame(dictionary)

    def test_drop_rows_with_missing_values(self):
        data_frame = self.data_frame.dropna()
        total_rows = len(data_frame.index)
        self.assertEqual(1, total_rows)

    def test_fill_missing_values(self):
        data_frame = self.data_frame.fillna(value = 'FILL VALUE')
        total_rows = len(data_frame.index)

        last_row = data_frame.loc[2]
        self.assertEqual(3, total_rows)
        self.assertEqual('FILL VALUE', last_row['A'])
        self.assertEqual('FILL VALUE', last_row['B'])
        self.assertEqual(3, last_row['C'])

    def test_fill_missing_values_with_mean(self):
        data_frame = self.data_frame['A'].fillna(value=self.data_frame['A'].mean())
        total_rows = len(data_frame.index)
        self.assertEqual(3, total_rows)
        self.assertEqual(1, data_frame.loc[0])
        self.assertEqual(2, data_frame.loc[1])
        self.assertEqual(1.5, data_frame.loc[2])

