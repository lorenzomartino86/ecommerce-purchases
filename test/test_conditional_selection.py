import os
import unittest
from src.adapter.file_purchases_repository import FilePurchasesRepository
from src.domain.ecommerce_purchases import EcommerceDataFrame

class ConditionalSelectionTest(unittest.TestCase):

    def setUp(self):
        file_location = os.path.join(os.path.dirname(__file__), 'EcommercePurchases.csv')
        repository = FilePurchasesRepository(file_location)
        self.ecommerce = EcommerceDataFrame()
        self.ecommerce.create_data_frame(repository)

    def test_price_greater_than_ninentynine(self):
        df = self.ecommerce.get_data_frame()
        df = df[df['Purchase Price'] > 99]
        length = len(df.index)
        self.assertEqual(98, length)

    def test_price_greater_than_ninentynine_and_language_fr(self):
        df = self.ecommerce.get_data_frame()
        df = df[(df['Purchase Price'] > 99) & (df['Language'] == 'fr')]
        length = len(df.index)
        self.assertEqual(15, length)

    def test_price_greater_than_sixty_for_psychiatric_nurses(self):
        df = self.ecommerce.get_data_frame()
        df = df[(df['Purchase Price'] > 60) & (df['Job'] == 'Psychiatric nurse')]
        length = len(df.index)
        self.assertEqual(7, length)

    def test_price_greater_than_sixty_or_with_psychiatric_nurses(self):
        df = self.ecommerce.get_data_frame()
        df = df[(df['Purchase Price'] > 60) | (df['Job'] == 'Psychiatric nurse')]
        length = len(df.index)
        self.assertEqual(4061, length)

if __name__ == '__main__':
    unittest.main()