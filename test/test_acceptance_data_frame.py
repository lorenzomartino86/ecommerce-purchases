import unittest
from unittest.mock import Mock
from src.adapter.file_purchases_repository import FilePurchasesRepository
from src.domain.ecommerce_purchases import EcommerceDataFrame

class DataFrameTest(unittest.TestCase):

    def setUp(self):
        repository = FilePurchasesRepository("./EcommercePurchases.csv")
        self.ecommerce = EcommerceDataFrame()
        self.ecommerce.create_data_frame(repository)

    def test_data_frame_generation(self):
        df = self.ecommerce.get_data_frame()
        dimensions = df.shape
        total_rows = len(df.index)
        self.assertEqual(10000, total_rows)
        self.assertEqual((10000, 14), dimensions)

    def test_get_first_five_rows(self):
        df = self.ecommerce.get_data_frame(5)
        self.assertEqual(5, len(df.index))

    def test_get_first_row(self):
        # DataFrame is a collection of Series
        df = self.ecommerce.get_data_frame(1)
        self.assertEqual(1, len(df.index))

        # get value of Series 'AM or PM' at index 0, and so on..
        am_or_pm = df.loc[0, 'AM or PM']
        credit_card = df.loc[0, 'Credit Card']
        company = df.loc[0, 'Company']
        price = df.loc[0, 'Purchase Price']

        self.assertEqual("PM", am_or_pm)
        self.assertEqual(6011929061123406, credit_card)
        self.assertEqual("Martinez-Herman", company)
        self.assertEqual(98.14, price)

    def test_removing_first_five_rows(self):
        df = self.ecommerce.get_data_frame(-5)
        self.assertEqual(9995, len(df.index))

    def test_get_last_row(self):
        total_rows = len(self.ecommerce.get_data_frame().index)
        index = total_rows - 1
        df = self.ecommerce.get_data_frame(-(index))
        self.assertEqual(1, len(df.index))

        # get value of Series 'AM or PM' at index, and so on..
        am_or_pm = df.loc[index, 'AM or PM']
        credit_card = df.loc[index, 'Credit Card']
        company = df.loc[index, 'Company']
        price = df.loc[index, 'Purchase Price']

        self.assertEqual("AM", am_or_pm)
        self.assertEqual(4139972901927273, credit_card)
        self.assertEqual("Greene Inc", company)
        self.assertEqual(67.59, price)





if __name__ == '__main__':
    unittest.main()
