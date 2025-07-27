import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE
import gradio as gr

# Load dataset
df = pd.read_csv("diabetes.csv")
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Balance the dataset using SMOTE
sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X, y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Test accuracy
test_accuracy = accuracy_score(y_test, model.predict(X_test)) * 100

# Prediction function
def predict_diabetes(pregnancies, glucose, bp, skin, insulin, bmi, dpf, age):
    input_data = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)[0]
    result = "⚠️ The person is likely **Diabetic**" if prediction == 1 else "✅ The person is likely **Not Diabetic**"
    accuracy_msg = f"✅ **Model Accuracy on Test Set:** {test_accuracy:.2f}%"
    return result, accuracy_msg

# Gradio UI using Blocks (streamlit-style layout)
with gr.Blocks(title="Diabetes Predictor") as demo:
    gr.Markdown("## 🩺 Diabetes Prediction App")
    gr.Markdown("Enter patient information on the left to predict diabetes and view model accuracy.")

    with gr.Row():
        with gr.Column(scale=1):
            pregnancies = gr.Slider(0, 17, value=3, label="Pregnancies")
            glucose = gr.Slider(0, 200, value=120, label="Glucose (mg/dL)")
            bp = gr.Slider(0, 122, value=70, label="Blood Pressure (mm Hg)")
            skin = gr.Slider(0, 100, value=20, label="Skin Thickness (mm)")
            insulin = gr.Slider(0, 846, value=79, label="Insulin (µU/mL)")
            bmi = gr.Slider(0.0, 67.0, value=28.0, label="BMI (kg/m²)")
            dpf = gr.Slider(0.0, 2.4, value=0.5, label="Diabetes Pedigree Function")
            age = gr.Slider(21, 88, value=33, label="Age (years)")
            submit_btn = gr.Button("🔍 Predict")

        with gr.Column(scale=1):
            prediction_output = gr.Textbox(label="🧾 Prediction Result", lines=2)
            accuracy_output = gr.Textbox(label="📈 Model Accuracy")

    # On button click
    submit_btn.click(
        predict_diabetes,
        inputs=[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age],
        outputs=[prediction_output, accuracy_output]
    )

demo.launch()
