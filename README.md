# 💧 Smart Irrigation System

**AICTE Internship – Cycle 2 | July 2025**

---

## 📘 Project Description

This project, developed as part of the AICTE-Shell Edunet Internship (Cycle 2, July 2025), presents a **Smart Irrigation System** powered by **Artificial Intelligence (Machine Learning)**.

The system takes 20 soil sensor inputs (scaled from 0 to 1) and predicts the ON/OFF status of sprinklers for each corresponding parcel of land.  
It aims to optimize water usage in agriculture by automating irrigation decisions based on real-time soil conditions.

---

## 🛠️ Tech Stack

- **Language:** Python (3.12.8)  
- **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn, joblib, streamlit  
- **Tools:** Jupyter Notebook, VS Code, GitHub, Streamlit    

---

## 🔑 Key Features

- ✅ Data preprocessing and analysis  
- ✅ Predictive modeling using **Random Forest Classifier**  
- ✅ Interactive web app built with **Streamlit**  
- ✅ Real-time prediction of sprinkler states from sensor inputs  
- ✅ Visualization of irrigation data using **matplotlib** and **seaborn**  
- ✅ Model saving and loading with `joblib`  

---

## 📁 Files Included

- `Irrigation_System.ipynb`: Main notebook for model training and evaluation  
- `Farm_Irrigation_System.pkl`: Trained model file (used by the app)  
- `app.py`: Streamlit web application for real-time sprinkler prediction  

---

## 🚀 How to Run the App

1. Clone or download this repository.
2. Make sure you have Python 3.12+ installed.
3. Install the required packages:
   ```bash
   pip install streamlit scikit-learn pandas numpy matplotlib seaborn joblib
4. Run the app:
   ```bash
   streamlit run app.py
5. The app will open in your browser at `http://localhost:8501`

📌 Make sure the `Farm_Irrigation_System.pkl` file is in the same folder as `app.py`.

---
  

