import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        study_hours: float,
        attendance: float,
        previous_score: float,
        assignment_marks: float):

        self.study_hours = study_hours
        self.attendance = attendance
        self.previous_score = previous_score
        self.assignment_marks = assignment_marks

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "study_hours": [self.study_hours],
                "attendance": [self.attendance],
                "previous_score": [self.previous_score],
                "assignment_marks": [self.assignment_marks],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
