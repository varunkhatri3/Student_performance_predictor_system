# Student Performance Prediction System
## AI/ML Internship Project

### About This Project
This is my first AI/ML project! It predicts whether a student will pass or fail based on their study habits and performance. I built this during my internship to learn about Machine Learning.

---

## What Does It Do?

The system takes 4 inputs about a student:
- Study hours per day
- Attendance percentage
- Previous exam score
- Assignment marks

Then it predicts: **Will Pass** or **Will Fail**

---

## Technologies I Used

- **Python** - Programming language
- **Pandas** - For working with data
- **Scikit-learn** - Machine learning library
- **Flask** - For the web application

---

## Project Structure

```
student_performance_project/
│
├── data/                   # The dataset
│   └── students_data.csv
│
├── src/                    # My code files
│   ├── components/         # Different parts of the pipeline
│   ├── pipeline/           # Training and prediction code
│   ├── logger.py          # Logging
│   └── utils.py           # Helper functions
│
├── artifacts/             # Saved models
│   ├── model.pkl          # Trained model
│   └── preprocessor.pkl   # Data processing
│
├── templates/             # HTML files for web app
├── static/                # CSS files
│
├── app.py                 # Web application
└── README.md              # This file!
```

---

## How to Run This Project

### Step 1: Install Required Libraries
```bash
pip install -r requirements.txt
```

### Step 2: Train the Model
```bash
python -m src.pipeline.train_pipeline
```

### Step 3: Run the Application
```bash
python app.py
```
Then open your browser and go to: `http://localhost:5000`

---

## The Dataset

My dataset contains information about 1,100 students with these features:

| Feature | What It Means |
|---------|--------------|
| study_hours | How many hours they study per day |
| attendance | Their attendance percentage |
| previous_score | Score from previous exam |
| assignment_marks | Marks in assignments |
| result | Pass or Fail (what we predict) |

---

## How It Works

1. **Data Collection**: I used a dataset with student information
2. **Data Preprocessing**: Clean the data and prepare it for training
3. **Model Training**: Train different ML models and pick the best one
4. **Prediction**: Use the trained model to predict new students

The system automatically picks the best performing model (Random Forest)!

---

## What I Learned

✅ How to build a complete ML pipeline  
✅ Data preprocessing and feature scaling  
✅ Training and comparing multiple ML models  
✅ Creating a web application with Flask  

---

## Results

The model works great! It achieved an **accuracy of ~90%**. You can see detailed results in the logs folder.

---

## Screenshots

**Web Application:**
![Web App](link-to-screenshot-if-any)

---

## About Me

This project was created as part of my AI/ML internship program. It's my first machine learning project and I learned a lot while building it!

**Program**: Artificial Intelligence Internship  
**Organization**: SKILL ORBIT  

---

## Troubleshooting

**Problem**: Model files not found  
**Solution**: Run the training pipeline first: `python -m src.pipeline.train_pipeline`

**Problem**: Web app not starting  
**Solution**: Make sure Flask is installed: `pip install flask`

---

## Thanks!
Thank you for checking out my first ML project! I hope it helps other beginners learning AI/ML.
