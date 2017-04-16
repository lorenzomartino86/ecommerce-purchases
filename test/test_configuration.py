import unittest
from pathlib import Path

class ConditionalSelectionTest(unittest.TestCase):

    def test_existence_of_file(self):
        self.assertEqual(True, Path("./EcommercePurchases.csv").is_file())