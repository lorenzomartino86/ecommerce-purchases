import unittest
import numpy as np
import pandas as pd

class GroupByTest(unittest.TestCase):

    def setUp(self):
        data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
                'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
                'Sales':[200,120,340,124,243,350]}
        self.data_frame = pd.DataFrame(data)

    def test_group_by_company_and_sum(self):
        byComp = self.data_frame.groupby('Company')
        data_frame = byComp.mean()
        total_rows = len(data_frame.index)
        self.assertEqual(3, total_rows)
        self.assertEqual(296.5, data_frame.loc['FB']['Sales'])
        self.assertEqual(232.0, data_frame.loc['MSFT']['Sales'])
