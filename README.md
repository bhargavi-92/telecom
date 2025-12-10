# 📞 Telecom Churn Prediction App

## 🚀 Overview
This project is a deployed web application built using **Streamlit** and **Python** that predicts whether a customer is likely to churn (cancel their service) based on their account and service attributes.

The underlying model is a [**Logistic Regression / Random Forest Classifier**] trained on historical telecom data.

**Key Features:**
* **Customer Churn Prediction:** Input various customer features to receive an instant prediction.
* **Data Preprocessing:** Handles missing values and scales/encodes categorical and numerical features automatically using a pre-saved `ColumnTransformer` pipeline.
* **Deployed:** Accessible via [Deployment Platform Link Here, e.g., Streamlit Cloud or Hugging Face Spaces].

## ⚙️ Project Structure


The core files in this repository are:

* `streamlit_app.py`: The main Python script containing the Streamlit UI, model loading functions, and prediction logic.
* `requirements.txt`: Lists all necessary Python libraries (e.g., `streamlit`, `pandas`, `scikit-learn`, `cloudpickle`).
* `model.bin`: The saved, serialized Machine Learning model.
* `preprocessor.bin`: The saved data preprocessing object (`ColumnTransformer` or Pipeline).

## 📋 How to Use the App

### 1. 🌐 Access the Deployed App
The easiest way to use the application is to visit the deployed link:

> **[Insert Your Deployment URL Here]**

### 2. 💻 Run Locally (For Developers)

To run this application on your local machine:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/bhargavi-92/telecom.git](https://github.com/bhargavi-92/telecom.git)
    cd telecom
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Streamlit App:**
    ```bash
    streamlit run streamlit_app.py
    ```

## 📊 Data & Model Details

### Input Features (Examples)
The model uses various features, including:
* `tenure`: Number of months the customer has been with the company.
* `MonthlyCharges`: The customer's current monthly bill.
* `Contract`: The type of contract (e.g., Month-to-month, One year).
* `InternetService`, `OnlineSecurity`, `TechSupport`, etc.

### Model Performance
* **Algorithm:** [e.g., Random Forest Classifier]
* **Accuracy:** [e.g., 81.5%]
* **F1-Score:** [e.g., 0.75]

## 🔗 Technologies Used

* **Python**
* **Streamlit** (for the web application)
* **scikit-learn** (for modeling and preprocessing)
* **Pandas** (for data handling)
* **Cloudpickle** (for serialization of model objects)

## ✉️ Contact

* **Author:** Bhargavi [Your Full Name or Username]
* **GitHub:** [Link to your GitHub profile]
