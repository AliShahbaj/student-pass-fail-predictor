# app.py
from flask import Flask, request, render_template
import pickle
import pandas as pd

# Load trained model
with open("student_pass_fail_model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        hours = float(request.form["hours"])
        test_data = pd.DataFrame({"study_hours": [hours]})
        prediction = model.predict(test_data)[0]

        result = "Pass ✅" if prediction == 1 else "Fail ❌"
        return f"Prediction: Student will {result} (Study hours: {hours})"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
