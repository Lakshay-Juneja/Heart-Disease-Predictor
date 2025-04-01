import streamlit as st
import pandas as pd
import numpy as np
import pickle
from pathlib import Path
import os

# Set page config
st.set_page_config(page_title="Heart Disease Prediction", layout="wide")

# Load the trained model
@st.cache_resource
def loadModel():
    try:
        # Load the model 
        MODEL_PATH = os.path.join(os.path.dirname(__file__), 'heartModel.pkl')
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = loadModel()

# Function to make predictions
def predictHeartDisease(features):
    if model is None:
        st.error("Model not loaded properly. Cannot make predictions.")
        return None
    
    try:
        # Reshape the features and get probability
        featuresArray = np.array(features).reshape(1, -1)
        probability = model.predict_proba(featuresArray)[0][1]  # Probability of heart disease
        return probability
    except Exception as e:
        st.error(f"Prediction error: {e}")
        return None

# Function to get user input
def getUserInput():
    userInput = {}
    
    col1, col2 = st.columns(2)
    
    with col1:
        userInput['age'] = st.slider('Age (years)', 20, 100, 50)
        userInput['sex'] = st.selectbox('Gender', ('Female', 'Male'))
        userInput['cp'] = st.selectbox('Chest Pain Type', 
                         ['Typical angina', 'Atypical angina', 'Non-anginal pain', 'Asymptomatic'])
        userInput['trestbps'] = st.slider('Resting Blood Pressure (mm Hg)', 90, 200, 120)
        userInput['chol'] = st.slider('Serum Cholesterol (mg/dL)', 100, 600, 200)
        
    with col2:
        userInput['fbs'] = st.selectbox('Fasting Blood Sugar > 120 mg/dL', ('No', 'Yes'))
        userInput['restecg'] = st.selectbox('Resting Electrocardiogram', 
                              ['Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'])
        userInput['thalach'] = st.slider('Maximum Heart Rate Achieved', 70, 220, 150)
        userInput['exang'] = st.selectbox('Exercise Induced Angina', ('No', 'Yes'))
    
    userInput['oldpeak'] = st.slider('ST Depression Induced by Exercise', 0.0, 6.2, 1.0, step=0.1)
    userInput['slope'] = st.selectbox('Slope of Peak Exercise ST Segment', 
                        ['Upsloping', 'Flatsloping', 'Downsloping'])
    userInput['ca'] = st.slider('Number of Major Vessels (0-3)', 0, 3, 0)
    userInput['thal'] = st.selectbox('Thallium Stress Result', 
                       ['Normal', 'Fixed defect', 'Reversible defect'])
    
    return userInput

# Function to format input for display 
def formatInputForDisplay(userInput):
    displayData = {
        'Age (years)': userInput['age'],
        'Gender': userInput['sex'],
        'Chest Pain Type': userInput['cp'],
        'Resting BP (mm Hg)': userInput['trestbps'],
        'Serum Cholesterol (mg/dL)': userInput['chol'],
        'Fasting Blood Sugar > 120': userInput['fbs'],
        'Resting ECG': userInput['restecg'],
        'Max Heart Rate': userInput['thalach'],
        'Exercise Induced Angina': userInput['exang'],
        'ST Depression': userInput['oldpeak'],
        'ST Slope': userInput['slope'],
        'Major Vessels': userInput['ca'],
        'Thallium Result': userInput['thal']
    }
    return pd.DataFrame(displayData, index=["Value"])

# Main function
def main():
    st.title("❤️ Heart Disease Prediction")
    st.write("""
    This predicts the chances of a patient having heart disease based on clinical parameters.
    The model was trained on the Cleveland Heart Disease dataset with 88.5% accuracy.
    """)
    
    # Disclaimer note
    st.warning("""
    **Note:** This prediction is an estimate based on statistical patterns and may not be 100% accurate. 
    Always consult with a cardiologist for medical diagnosis.
    """)
    
    # Get user input
    userInput = getUserInput()
    
    # Convert inputs to model format
    inputData = {
        'age': userInput['age'],
        'sex': 1 if userInput['sex'] == 'Male' else 0,
        'cp': {'Typical angina': 0, 'Atypical angina': 1, 
               'Non-anginal pain': 2, 'Asymptomatic': 3}[userInput['cp']],
        'trestbps': userInput['trestbps'],
        'chol': userInput['chol'],
        'fbs': 1 if userInput['fbs'] == 'Yes' else 0,
        'restecg': {'Normal': 0, 'ST-T wave abnormality': 1, 
                    'Left ventricular hypertrophy': 2}[userInput['restecg']],
        'thalach': userInput['thalach'],
        'exang': 1 if userInput['exang'] == 'Yes' else 0,
        'oldpeak': userInput['oldpeak'],
        'slope': {'Upsloping': 0, 'Flatsloping': 1, 
                  'Downsloping': 2}[userInput['slope']],
        'ca': userInput['ca'],
        'thal': {'Normal': 1, 'Fixed defect': 6, 
                 'Reversible defect': 7}[userInput['thal']]
    }
    
    # Display user input 
    st.subheader('Patient Clinical Parameters')
    st.dataframe(formatInputForDisplay(userInput), use_container_width=True)
    
    # Make prediction when button is clicked
    if st.button('Predict Heart Disease Risk'):
        heart_disease_prob = predictHeartDisease(list(inputData.values()))
        
        if heart_disease_prob is not None:
            st.subheader('Prediction Result')
            st.metric("Chance of Heart Disease", f"{heart_disease_prob:.1%}")
            
            # Interpretation guide
            if heart_disease_prob >= 0.7: 
                st.error('High risk detected')
                st.warning('Please consult with a cardiologist for further evaluation.')
            elif heart_disease_prob >= 0.3: 
                st.warning('Moderate risk detected')
                st.info('Consider consulting a doctor for preventive care.')
            else:  
                st.success('Low risk detected')
                st.info('Maintain a healthy lifestyle with regular checkups.')
            
if __name__ == '__main__':
    main()
