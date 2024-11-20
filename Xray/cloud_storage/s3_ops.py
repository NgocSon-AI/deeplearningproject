from io import StringIO
import sys
from typing import List, Union
from Xray.exception import XRayException
import boto3
from botocore.exceptions import ClientError
from mypy_boto3_s3.service_resource import Bucket
from Xray.logger import logging

class S3Operation:
    def __init__(self):
        self.s3_client = boto3.client("s3")
        self.s3_resource = boto3.resource("s3")

    def upload_file(self, from_filename: str, to_filename: str, bucket_name: str, remove: bool = True) -> None:
        logging.info("Entered the upload_file method of s3Operation class")
        try:
            logging.info(
                f"Uploading {from_filename} file to {to_filename} file in {bucket_name}"
            )
        except Exception as e:
            raise XRayException(e, sys)