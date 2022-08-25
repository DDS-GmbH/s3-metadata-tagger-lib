"""
The tests for the dataset metadata extractor
"""

import unittest

from pdf_metadata_extractor import pdf_metadata_extractor


class DatasetTests(unittest.TestCase):
    """
    Simple pdf metadata extractor tests
    """

    def test_pdf(self):
        """
        Check whether the number of pages in a pdf is determined correctly
        """
        self.assertEqual(
            pdf_metadata_extractor.get_pages("pdf_metadata_extractor/resources/test/test.pdf")["pages"], "1")


if __name__ == '__main__':
    unittest.main()
