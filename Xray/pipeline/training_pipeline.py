import sys

from Xray.components.data_ingestion import DataIngestion
from Xray.entity.artifact_entity import DataIngestionArtifact
from Xray.entity.config_entity import DataIngestionConfig
from Xray.exception import XRayException
from Xray.logger import logging

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()

        def start_data_ingestion(self) -> DataIngestionArtifact:
            logging.info("Entered the start_data_ingestion method of Training ")
        try:
            logging.info("Getting the data")
            data_ingestion = DataIngestion(
                data_ingestion_config = self.data_ingestion_config()
            )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(
                "Excited the start_data_ingestion method"
            )
            return data_ingestion_artifact
        except Exception as e:
            raise XRayException(e, sys)
        

if __name__ == '__main__':
    train_pipeline = TrainPipeline()
    train_pipeline.start_data_ingestion()