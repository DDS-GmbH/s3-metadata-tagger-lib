"""
The package for retrieving the encoding xlsx and csv datasets.
"""

from zipfile import ZipFile
from typing import Dict
import logging
from chardet import UniversalDetector
from lxml import etree
import magic


def get_encoding(dataset_path: str) -> Dict[str, str]:
    """
    Returns a dictionary containing the encoding of the
    file found under the passed `dataset_path`.
    The file has to be either a text/csv, text/plain, or
    xlsx file.
    """
    encoding = ""
    mime_type = magic.from_file(dataset_path, mime=True)  # type: ignore
    if mime_type in ("text/csv", "text/plain"):
        logging.info("Getting csv encoding")
        encoding = _get_csv_encoding(dataset_path)
    elif mime_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        logging.info("Getting xlsx encoding")
        encoding = _get_xlsx_encoding(dataset_path)
    else:
        raise Exception(f"Not supported mime type {mime_type}")
    return {"encoding": encoding}


def _get_csv_encoding(dataset_path: str) -> str:
    detector = UniversalDetector()
    with open(dataset_path, 'rb') as dataset:
        for line in dataset.readlines():
            detector.feed(line)
            if detector.done:
                break
        result = detector.close()
        return result["encoding"]


def _get_xlsx_encoding(dataset_path: str) -> str:
    with ZipFile(dataset_path) as zip_file:
        try:
            with zip_file.open("docProps/core.xml") as props:
                element_tree = etree.ElementTree(
                    etree.fromstring(props.read()))
                encoding = "UTF-8"
                if element_tree.docinfo.encoding:
                    encoding = element_tree.docinfo.encoding
                return encoding
        except KeyError:
            return "UTF-8"
