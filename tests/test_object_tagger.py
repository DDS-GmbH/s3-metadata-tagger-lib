"""
Integration tests for the object tagger
"""

import logging
import unittest
from typing import Dict

import localstack_client.session as boto3

from metadata_tagger.object_tagger import S3ObjectPath, MetadataHandler, tag_file
from metadata_tagger.pdf_metadata_extractor import pdf_metadata_extractor

RESOURCE_PATH = "tests/resources"
FILE_NAME = "test.pdf"
BUCKET = "testbucket"
s3_client = boto3.client('s3')  # type: ignore


def check_if_already_tagged(file_metadata: Dict[str, str]) -> bool:
    """
    Check whether the file has already been tagged with the number of pages
    """
    return "pages" in file_metadata


class ObjectTaggerTest(unittest.TestCase):
    """
    Object tagger tests
    """

    def setUp(self) -> None:
        logging.basicConfig(level=logging.INFO)
        s3_client.create_bucket(Bucket=BUCKET)
        s3_client.upload_file(
            f"{RESOURCE_PATH}/{FILE_NAME}", BUCKET, FILE_NAME)

    def test_object_tagger(self):
        """
        Check whether a file is tagged correctly
        """
        object_path = S3ObjectPath(FILE_NAME, BUCKET)
        object_tagger = MetadataHandler(
            check_if_already_tagged, pdf_metadata_extractor.get_pages)
        tag_file(object_path, object_tagger)
        self.assertTrue("pages" in s3_client.head_object(
            Bucket=BUCKET, Key=FILE_NAME)["Metadata"])


if __name__ == '__main__':
    unittest.main()
