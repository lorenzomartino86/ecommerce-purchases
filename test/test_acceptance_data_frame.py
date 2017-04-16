import unittest
from unittest.mock import Mock
from src.adapter.file_purchases_repository import FilePurchasesRepository
from src.domain.ecommerce_purchases import EcommercePurchases

class DataFrameTest(unittest.TestCase):

    def setUp(self):
        self.repository = FilePurchasesRepository("./EcommercePurchases.csv")
        self.purchases = EcommercePurchases()

    def test_data_frame_generation(self):
        self.purchases.create_data_frame(self.repository)
        data_frame = self.purchases.get_data_frame()
        dimensions = data_frame.shape
        total_rows = len(data_frame.index)
        self.assertEqual(10000, total_rows)
        self.assertEqual((10000, 14), dimensions)

    def test_get_first_five_rows(self):
        self.purchases.create_data_frame(self.repository)
        data_frame = self.purchases.get_data_frame(5)
        self.assertEqual(5, len(data_frame.index))

    def test_get_first_row(self):
        self.purchases.create_data_frame(self.repository)

        # DataFrame is a collection of Series
        data_frame = self.purchases.get_data_frame(1)
        self.assertEqual(1, len(data_frame.index))

        # get value of Series 'AM or PM' at index 0, and so on..
        am_or_pm = data_frame.loc[0, 'AM or PM']
        credit_card = data_frame.loc[0, 'Credit Card']
        company = data_frame.loc[0, 'Company']
        price = data_frame.loc[0, 'Purchase Price']

        self.assertEqual("PM", am_or_pm)
        self.assertEqual(6011929061123406, credit_card)
        self.assertEqual("Martinez-Herman", company)
        self.assertEqual(98.14, price)

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

        # get value of Series 'AM or PM' at index, and so on..
        am_or_pm = data_frame.loc[index, 'AM or PM']
        credit_card = data_frame.loc[index, 'Credit Card']
        company = data_frame.loc[index, 'Company']
        price = data_frame.loc[index, 'Purchase Price']

        self.assertEqual("AM", am_or_pm)
        self.assertEqual(4139972901927273, credit_card)
        self.assertEqual("Greene Inc", company)
        self.assertEqual(67.59, price)





if __name__ == '__main__':
    unittest.main()
