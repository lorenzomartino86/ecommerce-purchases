import unittest
from unittest.mock import Mock
from pathlib import Path
from src.adapter.file_purchases_repository import FilePurchasesRepository
from src.domain.ecommerce_purchases import EcommercePurchases

class DataFrameTest(unittest.TestCase):

    def setUp(self):
        purchases_csv = "./EcommercePurchases.csv"
        self.path = Path(purchases_csv)
        self.repository = FilePurchasesRepository(purchases_csv)
        self.purchases = EcommercePurchases()

    def test_existence_of_file(self):
        self.assertEqual(True, self.path.is_file())

    def test_data_frame_generation(self):
        self.purchases.create_data_frame(self.repository)
        data_frame = self.purchases.get_data_frame()
        total_rows = len(data_frame.index)
        self.assertEqual(10000, total_rows)

    def test_get_first_five_rows(self):
        self.purchases.create_data_frame(self.repository)
        data_frame = self.purchases.get_data_frame(5)
        self.assertEqual(5, len(data_frame.index))

    def test_removing_first_five_rows(self):
        self.purchases.create_data_frame(self.repository)
        data_frame = self.purchases.get_data_frame(-5)
        self.assertEqual(9995, len(data_frame.index))

if __name__ == '__main__':
    unittest.main()
