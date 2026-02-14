# Student Performance Prediction System 🎓
## AI-Based Graduate Internship Project (AI/ML)

**🌐 Live Demo:** [https://student-performance-predictor-system.onrender.com](https://student-performance-predictor-system.onrender.com)

Welcome to my **Student Performance Prediction System**! This project was developed during my Artificial Intelligence internship to demonstrate an end-to-end Machine Learning pipeline. It predicts whether a student will **Pass** or **Fail** based on key academic metrics.

---

## 📂 Project Structure

This project is organized to be easy to explore and use. It follows a "Hybrid" model, providing both professional interactive notebooks and a production-ready web application.

```
student_performance_project/
│
├── artifacts/              # Main Saved Results
│   ├── model.pkl           # Trained Random Forest Model
│   └── preprocessor.pkl    # Data Preprocessing Object
│
├── data/                   # The Dataset
│   └── students_data.csv   # Unified dataset containing 1,100 student records
│
├── notebooks/              # Interactive AI Learning
│   └── Student_Performance_System.ipynb  # Core ML Pipeline (7 Modules)
│
├── static/                 # Web Styling
│   └── style.css           # Custom CSS for the web interface
│
├── templates/              # Web HTML
│   └── index.html          # Main web application frontend
│
├── app.py                  # Standalone Web Application (Flask)
├── requirements.txt        # All required Python libraries
├── MLPROJECT.pdf           # Core Project Reference & Submission Requirements
└── README.md               # You are here!
```

---

## 📊 Dataset & Evaluation

To ensure high-quality predictions, the model is trained on a substantial dataset designed for school-level performance analysis.

### 1. Dataset Breakdown
The dataset (**`data/students_data.csv`**) contains **1,100 total records** with the following technical features:

| Feature Name | Description | Data Type |
| :--- | :--- | :--- |
| **Study Hours** | Number of hours spent studying daily | Numerical |
| **Attendance** | Percentage of classes attended | Numerical |
| **Previous Score**| Marks obtained in the previous academic term | Numerical |
| **Assignment Marks**| Scores from recent assignments | Numerical |
| **Result (Target)** | Classification label: **Pass** (1) or **Fail** (0) | Categorical |

### 2. Train-Test Split Details
Following standard ML best practices, the data is split into two distinct sets:
- **Training Set (80%)**: **880 records** used to teach the model patterns between inputs and results.
- **Testing Set (20%)**: **220 records** held back to evaluate the model's performance on unseen data.
- **Random State**: Set to `42` for perfect reproducibility across all runs.

---

## ⚙️ How It Works (The 7 Modules)

Following the official **MLPROJECT.pdf** guidelines, the project is divided into 7 core modules, all fully implemented in the `Student_Performance_System.ipynb` notebook:

1.  **Data Collection**: Loading and preparing the 1,100 row CSV dataset.
2.  **Data Preprocessing**: Handling missing values, scaling features, and encoding labels (Pass=1, Fail=0).
3.  **Data Visualization**: Analyzing relationships like *Study Hours vs Score* and *Attendance vs Result*.
4.  **Model Selection**: Testing and comparing **Logistic Regression**, **Decision Trees**, and **Random Forest**.
5.  **Model Training**: Training on 80% of the data to learn classification patterns.
6.  **Model Testing**: Evaluating the model on 20% test data to verify performance.
7.  **Result & Conclusion**: Saving the optimized model (**94.09% accuracy**) for the web application.

---

## 🚀 Getting Started

### 1. Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 2. View the AI Pipeline
Open the **`notebooks/Student_Performance_System.ipynb`** file in Jupyter Notebook or VS Code to see the data analysis and training process.

### 3. Launch the Web App
Run the following command to start the predictor website:
```bash
python app.py
```

### 4. Open Live Version
If you don't want to run it locally, you can access the live version here:  
**[Launch Web App 🚀](https://student-performance-predictor-system.onrender.com)**

---

## ✨ Project Highlights
- **Realistic Dataset**: Features 1,100 synthetic student records with logical correlations.
- **Improved Accuracy**: Achieving an impressive **94.09% accuracy** using Logistic Regression.
- **Clean UI**: A mobile-friendly, professional web interface for real-time predictions.
- **Self-Contained**: The Flask app (`app.py`) is designed with no complex dependencies, making it portable and easy to run.

