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

    def test_existence_of_file(self):
        self.assertEqual(True, self.path.is_file())

    def test_data_frame_generation(self):
        ecommerce = EcommercePurchases()
        ecommerce.createDataFrame(self.repository)


if __name__ == '__main__':
    unittest.main()
