# train_model.py
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Step 1: Create a small dataset (study_hours vs pass/fail)
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "result":      [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]  # 0 = fail, 1 = pass
}
df = pd.DataFrame(data)

# Step 2: Train logistic regression model
X = df[["study_hours"]]   # features
y = df["result"]          # target

model = LogisticRegression()
model.fit(X, y)

# Step 3: Test prediction
test_data = pd.DataFrame({"study_hours": [4.5]})
print("Prediction for 4.5 study hours:", model.predict(test_data))

# Step 4: Save model
with open("student_pass_fail_model.pkl", "wb") as f:
    pickle.dump(model, f)
