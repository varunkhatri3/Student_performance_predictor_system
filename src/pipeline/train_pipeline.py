import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.exception import CustomException
from src.logger import logging

class TrainPipeline:
    def __init__(self):
        pass

    def run_pipeline(self):
        try:
            logging.info("Starting the training pipeline")
            
            # Step 1: Data Ingestion
            obj = DataIngestion()
            train_data_path, test_data_path = obj.initiate_data_ingestion()

            # Step 2: Data Transformation
            data_transformation = DataTransformation()
            train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)

            # Step 3: Model Trainer
            model_trainer = ModelTrainer()
            print(model_trainer.initiate_model_trainer(train_arr, test_arr))
            
            logging.info("Training pipeline completed successfully")
            
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    train_pipeline = TrainPipeline()
    train_pipeline.run_pipeline()
