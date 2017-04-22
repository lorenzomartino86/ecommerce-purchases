import os
import unittest
from pathlib import Path

class ConditionalSelectionTest(unittest.TestCase):

    def setUp(self):
        self.file_location = os.path.join(os.path.dirname(__file__), 'EcommercePurchases.csv')

    def test_existence_of_file(self):
        self.assertEqual(True, Path(self.file_location).is_file())

if __name__ == '__main__':
    unittest.main()