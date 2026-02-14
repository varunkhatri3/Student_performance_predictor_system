import os
import sys
from dataclasses import dataclass

from sklearn.ensemble import (
    AdaBoostClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier,
)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import seaborn as sns

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()


    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                "Random Forest": RandomForestClassifier(),
                "Decision Tree": DecisionTreeClassifier(),
                "Gradient Boosting": GradientBoostingClassifier(),
                "Logistic Regression": LogisticRegression(),
                "AdaBoost Classifier": AdaBoostClassifier(),
            }

            model_report = {}

            logging.info("="*60)
            logging.info("Training and Evaluating Multiple Models")
            logging.info("="*60)

            for i in range(len(list(models))):
                model_name = list(models.keys())[i]
                model = list(models.values())[i]
                
                logging.info(f"\n Training {model_name}...")
                model.fit(X_train,y_train)

                y_train_pred = model.predict(X_train)
                y_test_pred = model.predict(X_test)
                
                train_model_score = accuracy_score(y_train,y_train_pred)
                test_model_score = accuracy_score(y_test,y_test_pred)
                
                model_report[model_name] = test_model_score
                
                # Log detailed metrics
                logging.info(f"{model_name} - Training Accuracy: {train_model_score:.4f}")
                logging.info(f"{model_name} - Testing Accuracy: {test_model_score:.4f}")

            # Log model comparison
            logging.info("\n" + "="*60)
            logging.info("Model Performance Comparison")
            logging.info("="*60)
            for model_name, score in sorted(model_report.items(), key=lambda x: x[1], reverse=True):
                logging.info(f"{model_name:25s}: {score:.4f}")
            logging.info("="*60 + "\n")

            ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## To get best model name from dict
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset: {best_model_name}")
            logging.info(f"Best model accuracy: {best_model_score:.4f}")

            # Generate detailed classification report for best model
            predicted=best_model.predict(X_test)
            
            logging.info("\n" + "="*60)
            logging.info(f"Classification Report for {best_model_name}")
            logging.info("="*60)
            report = classification_report(y_test, predicted, target_names=['Fail', 'Pass'])
            logging.info("\n" + report)
            
            # Log confusion matrix
            cm = confusion_matrix(y_test, predicted)
            logging.info("\nConfusion Matrix:")
            logging.info(f"{'':10s} Predicted Fail  Predicted Pass")
            logging.info(f"Actual Fail    {cm[0][0]:8d}       {cm[0][1]:8d}")
            logging.info(f"Actual Pass    {cm[1][0]:8d}       {cm[1][1]:8d}")
            logging.info("="*60 + "\n")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            acc = accuracy_score(y_test, predicted)
            return acc

        except Exception as e:
            raise CustomException(e,sys)
