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
            # Get form data
            study_hours = float(request.form["study_hours"])
            attendance = float(request.form["attendance"])
            previous_score = float(request.form["previous_score"])
            assignment_marks = float(request.form["assignment_marks"])
            
            # Create data object
            data = CustomData(
                study_hours=study_hours,
                attendance=attendance,
                previous_score=previous_score,
                assignment_marks=assignment_marks
            )
            
            # Convert to dataframe
            pred_df = data.get_data_as_data_frame()
            
            # Make prediction
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            
            # Get result
            prediction = results[0]
            
            # Set display text
            if prediction == 1:
                prediction_text = "Will Pass 🎉"
                result_class = "pass"
            else:
                prediction_text = "Will Fail ❌"
                result_class = "fail"
                
        except Exception as e:
            prediction_text = f"Error: {e}"
            result_class = "error"

    return render_template("index.html", prediction=prediction_text, result_class=result_class)

if __name__ == "__main__":
    import sys
    # This helps display emojis in some Windows terminals
    try:
        if sys.stdout.encoding != 'utf-8':
            sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

    print("\n" + "="*60)
    print("🚀 FLASK WEB APP STARTING")
    print("="*60)
    print("📍 Main App: http://localhost:5000")
    print("="*60 + "\n")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
