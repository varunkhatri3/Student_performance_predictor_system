from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import os
import pickle
import sys

# --- Self-Contained Prediction Logic (Built for simplified folder structure) ---

class CustomData:
    def __init__(self, study_hours, attendance, previous_score, assignment_marks):
        self.study_hours = study_hours
        self.attendance = attendance
        self.previous_score = previous_score
        self.assignment_marks = assignment_marks

    def get_as_dataframe(self):
        try:
            input_dict = {
                "study_hours": [self.study_hours],
                "attendance": [self.attendance],
                "previous_score": [self.previous_score],
                "assignment_marks": [self.assignment_marks],
            }
            return pd.DataFrame(input_dict)
        except Exception as e:
            print(f"Error creating dataframe: {e}")
            return None

class Predictor:
    def __init__(self):
        self.model_path = os.path.join("artifacts", "model.pkl")
        self.preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

    def predict(self, features):
        try:
            with open(self.model_path, 'rb') as f:
                model = pickle.load(f)
            with open(self.preprocessor_path, 'rb') as f:
                preprocessor = pickle.load(f)

            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        except Exception as e:
            print(f"Error during prediction: {e}")
            return None

# --- Flask App ---

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction_text = ""
    result_class = ""
    
    if request.method == "POST":
        try:
            # Create data object
            data = CustomData(
                study_hours=float(request.form["study_hours"]),
                attendance=float(request.form["attendance"]),
                previous_score=float(request.form["previous_score"]),
                assignment_marks=float(request.form["assignment_marks"])
            )
            
            df = data.get_as_dataframe()
            predictor = Predictor()
            results = predictor.predict(df)
            
            if results is not None:
                prediction = results[0]
                prediction_text = "Will Pass 🎉" if prediction == 1 else "Will Fail ❌"
                result_class = "pass" if prediction == 1 else "fail"
            else:
                prediction_text = "Model Error"
                result_class = "error"
                
        except Exception as e:
            prediction_text = f"Error: {e}"
            result_class = "error"

    return render_template("index.html", prediction=prediction_text, result_class=result_class)

if __name__ == "__main__":
    # Encoding fix for Windows console emojis
    try:
        if sys.stdout.encoding != 'utf-8':
            import codecs
            sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
            sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
    except Exception:
        pass

    print("\n" + "="*60)
    print("🚀 FLASK WEB APP STARTING (Standard Edition)")
    print("="*60)
    print("📍 URL: http://localhost:5000")
    print("="*60 + "\n")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
