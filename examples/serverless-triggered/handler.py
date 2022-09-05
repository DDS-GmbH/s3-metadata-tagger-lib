import logging
import os
import urllib.parse

from typing import Dict, Callable, TypedDict

import boto3
from aws_lambda_typing import context as context_, events

from metadata_tagger.object_tagger import tag_file, S3ObjectPath, MetadataHandler
from metadata_tagger.extractors import pdf_metadata_extractor

if os.environ.get('LOCALSTACK_S3_ENDPOINT_URL'):
    s3_client = boto3.client(
        "s3", endpoint_url=os.environ.get('LOCALSTACK_S3_ENDPOINT_URL'))
else:
    s3_client = boto3.client("s3")


class TagFileRequest(TypedDict):
    key: str
    bucket: str


class HTTPRequest(TypedDict):
    body: str


def handle_pdf_creation(event: events.S3Event, context: context_.Context) -> None:
    handle_creation_event(event, context, pdf_metadata_extractor.get_pages)


def handle_creation_event(event: events.S3Event, context: context_.Context, tagging_function: Callable[[str], Dict[str, str]]):
    if len(event['Records']) == 0:
        raise Exception("Event did not contain a 'Records' entry")
    if 's3' in event['Records'][0] and 'key' in event['Records'][0]['s3']['object']:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(
            event['Records'][0]['s3']['object']['key'], encoding='utf-8')
        logging.info("Tagging %s in bucket %s", key, bucket)
        path = S3ObjectPath(key, bucket)
        metadata_handler = MetadataHandler(
            lambda fm: "pages" in fm, tagging_function)
        tag_file(path, metadata_handler)
    else:
        raise Exception(
            f"Request did not contain bucket or item key: {event['Records'][0]}")
