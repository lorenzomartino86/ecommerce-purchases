import unittest
from unittest.mock import Mock
from pathlib import Path
from src.adapter.file_purchases_repository import FilePurchasesRepository
from src.domain.ecommerce_purchases import EcommercePurchases

class DataFrameTest(unittest.TestCase):

    def setUp(self):
        self.purchases_csv = "./EcommercePurchases.csv"
        self.repository = FilePurchasesRepository(self.purchases_csv)
        self.purchases = EcommercePurchases()

    def test_existence_of_file(self):
        self.assertEqual(True, Path(self.purchases_csv).is_file())

    def test_data_frame_generation(self):
        self.purchases.create_data_frame(self.repository)
        data_frame = self.purchases.get_data_frame()
        total_rows = len(data_frame.index)
        self.assertEqual(10000, total_rows)

    def test_get_first_five_rows(self):
        self.purchases.create_data_frame(self.repository)
        data_frame = self.purchases.get_data_frame(5)
        self.assertEqual(5, len(data_frame.index))

    def test_get_first_row(self):
        self.purchases.create_data_frame(self.repository)
        data_frame = self.purchases.get_data_frame(1)
        self.assertEqual(1, len(data_frame.index))
        am_or_pm = data_frame['AM or PM'][0]
        credit_card = data_frame['Credit Card'][0]
        company = data_frame['Company'][0]
        purchase_price = data_frame['Purchase Price'][0]
        self.assertEqual("PM", am_or_pm)
        self.assertEqual(6011929061123406, credit_card)
        self.assertEqual("Martinez-Herman", company)
        self.assertEqual(98.14, purchase_price)

    def test_removing_first_five_rows(self):
        self.purchases.create_data_frame(self.repository)
        data_frame = self.purchases.get_data_frame(-5)
        self.assertEqual(9995, len(data_frame.index))

    def test_get_last_row(self):
        self.purchases.create_data_frame(self.repository)

        total_rows = len(self.purchases.get_data_frame().index)
        index = total_rows - 1
        data_frame = self.purchases.get_data_frame(-(index))
        self.assertEqual(1, len(data_frame.index))

        am_or_pm = data_frame['AM or PM'][index]
        credit_card = data_frame['Credit Card'][index]
        company = data_frame['Company'][index]
        purchase_price = data_frame['Purchase Price'][index]
        self.assertEqual("AM", am_or_pm)
        self.assertEqual(4139972901927273, credit_card)
        self.assertEqual("Greene Inc", company)
        self.assertEqual(67.59, purchase_price)

if __name__ == '__main__':
    unittest.main()
