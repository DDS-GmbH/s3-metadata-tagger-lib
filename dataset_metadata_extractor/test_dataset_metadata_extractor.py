"""
The tests for the dataset metadata extractor
"""

import unittest

from dataset_metadata_extractor import dataset_metadata_extractor


class DatasetTests(unittest.TestCase):
    """
    Simple dataset metadata extractor tests
    """

    def test_csv(self):
        """
        Check whether the encoding of a csv file is determined correctly
        """
        self.assertEqual(
            dataset_metadata_extractor.get_encoding("dataset_metadata_extractor/resources/test/test.csv")["encoding"], "ascii")

    def test_xlsx(self):
        """
        Check whether the encoding of a .xlsx file is determined correctly
        """
        self.assertEqual(
            dataset_metadata_extractor.get_encoding("dataset_metadata_extractor/resources/test/test.xlsx")["encoding"], "UTF-8")


if __name__ == '__main__':
    unittest.main()
