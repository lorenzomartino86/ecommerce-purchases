import unittest
import pandas as pd
import os
from sqlalchemy import create_engine

class SqliteDataframeTest(unittest.TestCase):

    def setUp(self):
        self.file_location = os.path.join(os.path.dirname(__file__), 'EcommercePurchases.csv')
        self.engine = create_engine('sqlite:///:memory:')

    def test_load_csv_to_sqlite(self):
        data_frame = pd.read_csv(self.file_location)
        data_frame.to_sql('ecommerce_purchases_table', self.engine)
        data_frame_from_sqlite = pd.read_sql('ecommerce_purchases_table', con=self.engine)
        dimensions = data_frame_from_sqlite.shape
        total_rows = len(data_frame_from_sqlite.index)
        self.assertEqual(10000, total_rows)
        # 1 column added by sqllite that is 'index'
        self.assertEqual((10000, 15), dimensions)







