import unittest
import numpy as np
import pandas as pd

class OperationsTest(unittest.TestCase):

    def setUp(self):
        data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
                'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
                'Sales':[200,120,340,124,243,350]}
        self.data_frame = pd.DataFrame(data)

    def test_distinct_company(self):
        unique = self.data_frame['Company'].nunique()
        self.assertEqual(3, unique)

    def test_apply_times2(self):
        data_frame = self.data_frame['Sales'].apply(self.__times2)
        self.assertEqual(400, data_frame[0])
        self.assertEqual(248, data_frame[3])
        self.assertEqual(700, data_frame[5])

    def test_apply_len(self):
        data_frame = self.data_frame['Company'].apply(len)
        self.assertEqual(4, data_frame[0])
        self.assertEqual(4, data_frame[3])
        self.assertEqual(2, data_frame[5])

    def test_apply_lambda(self):
        data_frame = self.data_frame['Sales'].apply(lambda x: x*3)
        self.assertEqual(600, data_frame[0])
        self.assertEqual(372, data_frame[3])
        self.assertEqual(1050, data_frame[5])


    def test_pivot_table(self):
        data = {'A':['foo','foo','foo','bar','bar','bar'],
                'B':['one','one','two','two','one','one'],
                'C':['x','y','x','y','x','y'],
                'D':[1,3,2,5,4,1]}

        data_frame = pd.DataFrame(data)
        print(data_frame)

        pivot_table = data_frame.pivot_table(values='D', index=['A','B'], columns='C')
        print(pivot_table)







    def __times2(self, x):
        return x*2
