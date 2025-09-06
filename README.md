# 🎓 Student Pass/Fail Prediction (Logistic Regression + Flask)

A simple machine learning + Flask web app that predicts whether a student will **pass or fail** based on the number of study hours.  
This project demonstrates how to **train a logistic regression model** and then **deploy it with Flask** as a web app.

---

## 📂 Project Structure
```
student_pass_fail_prediction/
│── train_model.py              # Script to train and save the model
│── app.py                      # Flask web application
│── student_pass_fail_model.pkl # Saved ML model
│── templates/
│   └── index.html              # Frontend HTML form
│── README.md                   # Project documentation
```

---

## ⚙️ Installation & Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

1. Clone the repo:
   ```bash
   git clone https://github.com/AliShahbaj/student_pass_fail_prediction.git
   cd student_pass_fail_prediction
   ```

2. Install dependencies:
   ```bash
   uv sync
   uv add pandas scikit-learn flask
   ```

3. Train the model:
   ```bash
   uv run train_model.py
   ```

4. Run the Flask app:
   ```bash
   uv run app.py
   ```

---

## 🌐 Usage
1. Open the app in your browser:  
   👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

2. Enter study hours (e.g., `4.5`).

3. Get a prediction → **Pass ✅** or **Fail ❌**

---

## 📊 Example
For a student who studied **4.5 hours**, the model predicts:

```
Prediction: Student will Pass ✅ (Study hours: 4.5)
```

---

## 🔧 Tech Stack
- **Python** (pandas, scikit-learn, pickle)
- **Flask** (for serving the model as a web app)
- **HTML** (basic frontend form)
- **uv** (dependency & environment manager)

---

## 🚀 Future Improvements
- Add more features (attendance, assignments, previous scores)
- Use larger datasets instead of manual small data
- Improve frontend with CSS/Bootstrap
- Deploy on Render / Vercel / Heroku

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).
