import streamlit as st
import pandas as pd
import pickle

# Load your trained model
# Replace 'model.pkl' with the actual filename of your trained model
with open('RandomForest_model_1.pkl', 'rb') as file:
    model = pickle.load(file)

# Title and description
st.title("Crop Yield Prediction")
st.write("Predict the crop yield per hectare based on input parameters.")

# Dropdown for State and Crop (use sample values, replace as needed)
states = ['andhra pradesh', 'karnataka', 'maharashtra', 'punjab']  # Add actual states
crops = ['cotton', 'wheat', 'rice', 'maize']  # Add actual crops

state = st.selectbox("Select State", states)
crop = st.selectbox("Select Crop", crops)
crop_type = st.selectbox("Select Crop Type", ['kharif', 'rabi', 'zaid'])

# Input fields for other features
nitrogen = st.number_input("Nitrogen (N)", min_value=0)
phosphorus = st.number_input("Phosphorus (P)", min_value=0)
potassium = st.number_input("Potassium (K)", min_value=0)
pH = st.number_input("pH Level", min_value=0.0, step=0.1)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0)
temperature = st.number_input("Temperature (°C)", min_value=0.0)
area = st.number_input("Area in Hectares", min_value=0.0)

# Prediction button
if st.button("Predict Yield"):
    # Create a DataFrame with input data
    input_data = pd.DataFrame({
        'N': [nitrogen],
        'P': [phosphorus],
        'K': [potassium],
        'pH': [pH],
        'rainfall': [rainfall],
        'temperature': [temperature],
        'Area_in_hectares': [area]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display prediction
    st.write(f"Predicted Yield (tons per hectare): {prediction:.2f}")
