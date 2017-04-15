import unittest
from pathlib import Path

from src.adapter.file_purchases_repository import FilePurchasesRepository
from src.domain.ecommerce_purchases import EcommercePurchases

class DataFrameTest(unittest.TestCase):
    def setUp(self):
        self.path = Path("resources/EcommercePurchases.csv")

    def test_existence_of_file(self):
        self.assertEqual(True, self.path.is_file())

    def test_data_frame_generation(self):
        ecommerce = EcommercePurchases()

        repository = FilePurchasesRepository()
        ecommerce.createDataFrame(repository)


        self.assertEqual(True, self.path.is_file())


if __name__ == '__main__':
    unittest.main()
