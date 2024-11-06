import os
import sys
from Xray.exception import XRayException


class S30peration():
    def sync_folder_to_s3(self, folder: str, bucket_name: str, bucket_folder_name: str) -> None:
        try:
            command: str = (
                f"Aws s3 sync {folder} s3://{bucket_name} / {bucket_folder_name}"
            )
            os.system(command = command)
        except Exception as e:
            raise XRayException(e, sys)
    
    def sync_folder_to_s3(self, folder: str, bucket_name: str, bucket_folder_name: str)->None:
        try:
            command: str = (
                f"Aws s3 sync s3://{bucket_name}/{bucket_folder_name}/{folder}"
            )
            os.system(command=command)
        except Exception as e:
            raise XRayException(e, sys)
     