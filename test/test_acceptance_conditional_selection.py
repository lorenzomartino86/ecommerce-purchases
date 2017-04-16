import unittest

from src.adapter.file_purchases_repository import FilePurchasesRepository
from src.domain.ecommerce_purchases import EcommercePurchases


class ConditionalSelectionTest(unittest.TestCase):

    def setUp(self):
        self.repository = FilePurchasesRepository("./EcommercePurchases.csv")
        self.purchases = EcommercePurchases()


    def test_price_greater_than_one_hundred(self):
        self.purchases.create_data_frame(self.repository)
        data_frame = self.purchases.get_by_price_greater_than(99)
        self.assertEqual(98, len(data_frame.index))