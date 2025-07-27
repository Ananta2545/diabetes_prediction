
# 🩺 Diabetes Predictor

A simple and interactive machine learning web app built using **Gradio** that predicts whether a person is likely to have diabetes based on health metrics.

Live Demo: https://huggingface.co/spaces/Ananta2545/Diabetes-predictor

---

## 📊 About the Project

This ML-powered diabetes prediction app uses a Random Forest Classifier trained on the **Pima Indians Diabetes Dataset**. It applies **SMOTE (Synthetic Minority Over-sampling Technique)** to balance the data and improve prediction performance on imbalanced classes.

The app takes user input for 8 key features (e.g. glucose, BMI, insulin, etc.) and outputs whether the person is likely diabetic or not.

---

## 🚀 Features

- ✅ Built using **Gradio 5.x** for an intuitive UI
- ✅ Balanced training data using **SMOTE**
- ✅ Deployed on **Hugging Face Spaces**
- ✅ Trained on Pima Indians Diabetes Dataset
- ✅ Fast and lightweight deployment
- ✅ Accuracy displayed on the interface

---

## 🧪 Model Info

- **Model**: Random Forest Classifier
- **Training Split**: 80/20 (Train/Test)
- **Oversampling**: SMOTE
- **Accuracy**: Displayed dynamically after model training

---

## 📈 Input Features

| Feature                      | Description                          |
|-----------------------------|--------------------------------------|
| Pregnancies                 | Number of times pregnant             |
| Glucose                     | Plasma glucose concentration         |
| Blood Pressure              | Diastolic blood pressure (mm Hg)     |
| Skin Thickness              | Triceps skin fold thickness (mm)     |
| Insulin                     | 2-Hour serum insulin (mu U/ml)       |
| BMI                         | Body mass index (weight in kg/m²)    |
| Diabetes Pedigree Function  | Function score based on family history |
| Age                         | Age in years                         |

---

## 🖥️ Interface Preview

<!-- Add screenshots here later -->

<img width="1366" height="682" alt="image" src="https://github.com/user-attachments/assets/6bf70cbe-cb69-4bad-b99a-9f13bad42224" />

<img width="1366" height="675" alt="image" src="https://github.com/user-attachments/assets/c3d74d84-b5ae-42b1-9ed7-ac075bc88db6" />

---

## 📦 Installation & Local Usage

You can also run this app locally:

```bash
git clone https://huggingface.co/spaces/Ananta2545/Diabetes-predictor
cd Diabetes-predictor
pip install -r requirements.txt
python app.py
```

## Project Structure
```
├── app.py               # Main Gradio application
├── diabetes.csv         # Dataset used for training
├── requirements.txt     # Python dependencies
├── README.md            # You're reading it
```

## Example inputs
Not Diabetic (Expected Output: "The person is likely Not Diabetic")
```
Pregnancies: 2
Glucose: 99
Blood Pressure: 64
Skin Thickness: 20
Insulin: 79
BMI: 24.0
Diabetes Pedigree Function: 0.3
Age: 29
```
--

Diabetic (Expected Output: "The person is likely Diabetic")
```
Pregnancies: 8
Glucose: 180
Blood Pressure: 90
Skin Thickness: 40
Insulin: 150
BMI: 35.0
Diabetes Pedigree Function: 1.2
Age: 45
```
Built with ❤️ by Ananta Chatterjee
Thanks for visiting.
