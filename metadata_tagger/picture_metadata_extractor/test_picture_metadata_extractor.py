"""
The tests for the picture metadata extractor
"""

import unittest

from metadata_tagger.picture_metadata_extractor import picture_metadata_extractor

path = "metadata_tagger/picture_metadata_extractor/resources/test"

class DatasetTests(unittest.TestCase):
    """
    Picture dimension extractor tests for multiple file formats.
    """

    def test_bmp(self):
        """
        Test .bmp dimension extraction
        """
        self.assertEqual(
            picture_metadata_extractor.get_dimensions(f"{path}/test.bmp")["width"], "444")
        self.assertEqual(
            picture_metadata_extractor.get_dimensions(f"{path}/test.bmp")["height"], "450")

    def test_gif(self):
        """
        Test .gif dimension extraction
        """
        self.assertEqual(
            picture_metadata_extractor.get_dimensions(f"{path}/test.gif")["width"], "444")
        self.assertEqual(
            picture_metadata_extractor.get_dimensions(f"{path}/test.gif")["height"], "450")

    def test_jp2(self):
        """
        Test .jp2 dimension extraction
        """
        self.assertEqual(
            picture_metadata_extractor.get_dimensions(f"{path}/test.jp2")["width"], "444")
        self.assertEqual(
            picture_metadata_extractor.get_dimensions(f"{path}/test.jp2")["height"], "450")

    def test_jpg(self):
        """
        Test .jpg dimension extraction
        """
        self.assertEqual(
            picture_metadata_extractor.get_dimensions(f"{path}/test.jpg")["width"], "444")
        self.assertEqual(
            picture_metadata_extractor.get_dimensions(f"{path}/test.jpg")["height"], "450")

    def test_png(self):
        """
        Test .png dimension extraction
        """
        self.assertEqual(
            picture_metadata_extractor.get_dimensions(f"{path}/test.png")["width"], "444")
        self.assertEqual(
            picture_metadata_extractor.get_dimensions(f"{path}/test.png")["height"], "450")

    def test_webp(self):
        """
        Test .webp dimension extraction
        """
        self.assertEqual(
            picture_metadata_extractor.get_dimensions(f"{path}/test.webp")["width"], "444")
        self.assertEqual(
            picture_metadata_extractor.get_dimensions(f"{path}/test.webp")["height"], "450")

    def test_wrong_extension_png(self):
        """
        Test dimension extraction for an image with the wrong extension
        """
        self.assertEqual(
            picture_metadata_extractor.get_dimensions(f"{path}/wrong_extension_png.jpg")["width"], "444")
        self.assertEqual(
            picture_metadata_extractor.get_dimensions(f"{path}/wrong_extension_png.jpg")["height"], "450")


if __name__ == '__main__':
    unittest.main()
