import os
import sys
from src.exception import CustomException
from src.logger import logger
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifact', 'train.csv')
    test_data_path: str=os.path.join('artifact', 'test.csv')
    raw_data_path: str=os.path.join('artifact', 'data.csv')


class DataIngestion:
    def __init__(self):
        self.ingesition_config = DataIngestionConfig()
    
    def intiate_data_ingestion(self):
        logger.info('Enterering Data Ingestion')
        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logger.info('Read the data set as data frame')

            os.makedirs(os.path.dirname(self.ingesition_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingesition_config.raw_data_path, index=False, header=True)    

            logger.info('Train test split initiated')
            train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

            train_data.to_csv(self.ingesition_config.train_data_path, index=False)
            test_data.to_csv(self.ingesition_config.test_data_path, index=False)
            logger.info('Train and Test data saved successfully')

            return(
                self.ingesition_config.train_data_path,
                self.ingesition_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)
            logger.error('Error in data ingestion')


if __name__ == '__main__':
    data_ingestion = DataIngestion()
    data_ingestion.intiate_data_ingestion()