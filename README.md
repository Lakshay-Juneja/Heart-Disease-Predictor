# ❤️ Heart Disease Prediction

## 📌 Overview
This project predicts the likelihood of heart disease using machine learning techniques based on various health parameters such as age, cholesterol levels, and blood pressure.

### 🔍 Live Demo
Run the **interactive web app** built with **Streamlit** to predict heart disease risk! 🚀
```bash
streamlit run app/modelRun.py
```

## 📊 Dataset
- The dataset is sourced from the [UCI Machine Learning Repository]([https://archive.ics.uci.edu/ml/datasets/heart+Disease](https://archive.ics.uci.edu/ml/datasets/heart+Disease)).
- A version is also available on [Kaggle]([https://www.kaggle.com/datasets/sumaiyatasmeem/heart-disease-classification-dataset](https://www.kaggle.com/datasets/sumaiyatasmeem/heart-disease-classification-dataset)).

## 🎯 Model Performance
✅ **Achieved Accuracy**: **88.5%**

## 🏥 Clinical Features Used

| Feature | Description |
|---------|-------------|
| **age** | Age in years |
| **sex** | Gender (1 = Male; 0 = Female) |
| **cp** | Chest pain type (0-3) |
| **trestbps** | Resting blood pressure (mm Hg) |
| **chol** | Serum cholesterol (mg/dl) |
| **fbs** | Fasting blood sugar > 120 mg/dl (1 = True; 0 = False) |
| **restecg** | Resting electrocardiographic results (0-2) |
| **thalach** | Maximum heart rate achieved |
| **exang** | Exercise-induced angina (1 = Yes; 0 = No) |
| **oldpeak** | ST depression induced by exercise |
| **slope** | Slope of peak exercise ST segment (0-2) |
| **ca** | Number of major vessels (0-3) |
| **thal** | Thallium stress test result (1,3,6,7) |
| **target** | Presence of heart disease (1 = Yes; 0 = No) |

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Lakshay-Juneja/Heart-Disease-Predictor.git
cd Heart-Disease-Predictor
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Prediction Model
To execute the Python script for predictions:
```bash
jupyter notebook model.ipynb
```

### 4️⃣ Run the Web App
```bash
streamlit run app/modelRun.py
```

## 🧠 Machine Learning Models Used
- Logistic Regression
- Random Forest Classifier
- Support Vector Machine (SVM)

## 📌 Usage Guide
💡 **Step 1**: Enter the patient’s clinical details in the interactive UI.
💡 **Step 2**: Click **Predict** to analyze the heart disease risk.
💡 **Step 3**: Get a **probability score** and risk level (Low, Moderate, or High).

🔴 **High Risk** → Consult a doctor immediately.
🟠 **Moderate Risk** → Consider preventive measures.
🟢 **Low Risk** → Maintain a healthy lifestyle.

## ⚠️ Disclaimer
This tool is is a project and **not a substitute for professional medical advice.** Always consult a doctor for an accurate diagnosis.

📩 Have suggestions or want to contribute? Reach out or create a pull request! 🎉

---
💻 Developed by [Lakshay Juneja](https://github.com/Lakshay-Juneja)

