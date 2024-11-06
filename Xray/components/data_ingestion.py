import sys

from Xray.cloud_storage.s3_operation import S30peration
#from Xray.constant.training_pipeline import *
from Xray.entity.artifact_entity import DataIngestionArtifact
from Xray.entity.config_entity import DataIngestionConfig
from Xray.exception import XRayException
from Xray.logger import logging

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
        self.s3 = S30peration()
    def get_data_from_s3(self):
        try:
            logging.info("Entered the get_data_from_s3 method of Data...")
            self.s3.sync_folder_to_s3(
                folder=self.data_ingestion_config.data_path,
                bucket_name=self.data_ingestion_config.bucket_name,
                bucket_folder_name=self.data_ingestion_config.S3_data_folder,
            )
            logging.info("Exited the get_data_from_s3 method of Data ingestion")
            
        except Exception as e:
            raise XRayException(e, sys)
        
    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise XRayException(e, sys)
        