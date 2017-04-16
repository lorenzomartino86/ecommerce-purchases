import unittest

from src.adapter.file_purchases_repository import FilePurchasesRepository
from src.domain.ecommerce_purchases import EcommerceDataFrame


class ConditionalSelectionTest(unittest.TestCase):

    def setUp(self):
        self.repository = FilePurchasesRepository("./EcommercePurchases.csv")
        self.ecommerce_data_frame = EcommerceDataFrame()


    def test_price_greater_than_one_ninentynine(self):
        self.ecommerce_data_frame.create_data_frame(self.repository)
        data_frame = self.ecommerce_data_frame.get_by_price_greater_than(99)
        length = len(data_frame.index)
        self.assertEqual(98, length)