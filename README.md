# 🌾 Crop Yield Prediction

This project leverages **Machine Learning** to predict crop yield based on environmental, climatic, and agricultural factors. The goal is to assist farmers and stakeholders in optimizing planning, resource management, and decision-making.

---

## 📋 Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Dataset](#dataset)
4. [Preprocessing](#preprocessing)
5. [Models Used](#models-used)
6. [Installation](#installation)
7. [Usage](#usage)
8. [Results](#results)
9. [Contributing](#contributing)
10. [License](#license)

---

## 📌 Introduction
Agriculture productivity relies on numerous factors such as crop type, rainfall, fertilizer use, and more. This project builds machine learning models to predict crop yield accurately, aiding farmers and planners in selecting optimal crops and resource allocation.

---

## 🎯 Features
- Predict crop yield with 96.54% accuracy using **Random Forest**.
- Use of **multiple regression models**: Linear Regression, Decision Tree, KNN, SVR, and Random Forest.
- Insights into which crops perform best under specific conditions.
- Visualizations of feature importance and prediction results.

---

## 📂 Dataset
The dataset includes the following fields:
- **Crop**: Crop type (e.g., Maize, Jute, etc.)
- **Year**: Crop year
- **Season**: Kharif, Rabi, or Whole Year
- **State**: The state in India where the crop is grown
- **Area**: Area under cultivation (in hectares)
- **Production**: Production in tons
- **Annual Rainfall**: Rainfall during the crop cycle
- **Fertilizer Use**: Fertilizers applied (in kilograms)
- **Pesticide Use**: Pesticides applied (in kilograms)
- **Yield**: Crop yield (Production per unit area)

---

## 🔧 Preprocessing
1. **Data Cleaning**: Handle missing values, outliers, and data inconsistencies.
2. **Feature Scaling**: Applied Min-Max scaling for certain features to normalize them.
3. **Encoding**: Converted categorical variables like `Season` and `State` into numerical values using **Label Encoding**.
4. **Train-Test Split**: The dataset is split into **80% training** and **20% testing** sets.

---

## 🔍 Models Used
We implemented and evaluated the following machine learning models:
1. **Linear Regression**  
2. **Decision Tree Regressor**  
3. **K-Nearest Neighbors (KNN)**  
4. **Random Forest Regressor**  
5. **Support Vector Regressor (SVR)**  

**Best Model:**  
- **Random Forest Regressor** achieved an accuracy of **96.54%**, making it the most effective for this task.

---

## 📥 Download Pre-trained Model and Preprocessor
- [Download model.pkl](https://drive.google.com/file/d/1hBtaT5sL7VosVMmizXbL55rT-EbFZ8bp/view?usp=sharing)
- [Download preprocessor.pkl](https://drive.google.com/file/d/1hFQIOW7Gh4lcxfUnXGgsfAlSPC-QxkXq/view?usp=sharing)

Place these files in the `/models` folder before running the project.


## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/crop-yield-prediction.git
   cd crop-yield-prediction

2. Install the required dependencies: 
      pip install -r requirements.txt