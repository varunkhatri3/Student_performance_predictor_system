from flask import Flask, render_template, request
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction_text = ""
    result_class = ""
    
    if request.method == "POST":
        try:
            # Get Form Data
            data = CustomData(
                study_hours=float(request.form["study_hours"]),
                attendance=float(request.form["attendance"]),
                previous_score=float(request.form["previous_score"]),
                assignment_marks=float(request.form["assignment_marks"])
            )
            
            # Prepare Data
            pred_df = data.get_data_as_data_frame()
            
            # Prediction Logic
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            
            prediction = results[0]
            prediction_text = "PASSED 🎉" if prediction == 1 else "FAILED ❌"
            result_class = "pass" if prediction == 1 else "fail"
                
        except Exception as e:
            prediction_text = f"Error: {e}"
            result_class = "error"

    return render_template("index.html", prediction=prediction_text, result_class=result_class)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
