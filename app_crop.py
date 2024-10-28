from flask import Flask, render_template, request
import pandas as pd
import pickle

# Load the trained Random Forest model
with open('RandomForest_model_1.pkl', 'rb') as rf_file:
    rf_model = pickle.load(rf_file)

# Initialize Flask app
app = Flask(__name__)

# Route for home page
@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    
    if request.method == "POST":
        # Get form data
        N = float(request.form.get("N", 0))
        P = float(request.form.get("P", 0))
        K = float(request.form.get("K", 0))
        pH = float(request.form.get("pH", 0))
        rainfall = float(request.form.get("rainfall", 0))
        temperature = float(request.form.get("temperature", 0))
        area = float(request.form.get("area", 0))
        
        # Create DataFrame from input data
        input_data = pd.DataFrame({
            'N': [N],
            'P': [P],
            'K': [K],
            'pH': [pH],
            'rainfall': [rainfall],
            'temperature': [temperature],
            'Area_in_hectares': [area]
        })
        
        # Make prediction
        prediction = rf_model.predict(input_data)[0]

    return render_template("index.html", prediction=prediction)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
