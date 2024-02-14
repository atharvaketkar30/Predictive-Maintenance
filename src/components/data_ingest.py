import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
from dataclasses import dataclass

#Paths to saving the data
@dataclass
class DataIngestionCinfig:
    train_data_path: str= os.path.join('artifacts', 'train.csv')
    test_data_path: str= os.path.join('artifacts', 'test.csv')
    raw_data_path: str= os.path.join('artifacts', 'data.csv')

#Data ingestion class
class DataIngestion():
    def __init__(self):
        self.ingestion_config = DataIngestionCinfig()

    def get_data(self, file_name):
        logging.info('Reading data from raw data path')
        try:
            #Reading data from the csv file
            df = pd.read_csv(file_name)
            logging.info('Data read successfully')


            #Saving the data
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info('Data saved successfully')


            return (
                self.ingestion_config.raw_data_path
                )
        except Exception as e:
            raise CustomException(error_ms=e, detail=sys)
        

if __name__ == '__main__':
    data_ingestion = DataIngestion()
    data_ingestion.get_data('sensor.csv')