
import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer 
from compose import ColumnTransformer
import cloudpickle
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.esemble import RandomFrosetClassifier

@st.cache_resource
def load_preprocessor():
    with open("preprocessor.bin", 'rb') as f:
        preprocessor = cloudpickle.load(f)
    print("Successfully loaded preprocessor")
    return preprocessor

@st.cache_resource
def load_model():
    with open("model.bin", 'rb') as f:
        model = cloudpickle.load(f)
    print("Loaded model Successfully")
    return model 


preprocessor = load_preprocessor()
model = load_model()



def clearn_data(x):
    try:
        x = x.copy()
        if x['SeniorCitizen'].dtype != 'O':
            x['SeniorCitizen'] = x['SeniorCitizen'].astype('str')
            print('Converted SeniorCitizen data type to string')
        else:
            print('SeniorCitizen data type is already string')

        if x['TotalCharge'].dtype == 'O':
            x['TotalCharge'] = x['TotalCharge'].replace(' ', None).astype('float')
            print('Converted TotalCharge data type to float')
        else:
            print('TotalCharge data type is not string.Hence not converting it')

        if 'customerID' in x.cloumns:
            x.drop(columns=['customerID'], inplace=True)
            print('Dropped customerID column')
       else:
            print('customerID columns not found. Hence, not deleting it')

       print("Data Clearing Successful")
       return None

def preprocess_inference_data(x_test, y_test, preprocessor):
    try:
        x_test = x_test.copy()
        if y_test is not None:
            y_test = y_test.copy()

        (categorical_mode_imputer_ct,
         one_hot_encoder_ct,
         numeric_median_imputer_ct,
         minmax_scaler, label_encoder) = preprocessor

        # Categorical missing value imputation
        categorical_mode_imputer_ct.set_output(transform='pandas')
        x_test = categorical_mode_imputer_ct.transform(x_test)
      
        # Onehot encoder
        one_hot_encoder_ct.set_output(transform='pandas')
        x_test = one_hot_encoder_ct.transform(x_test)

        # numeric missing value imputation
        numeric_median_imputer_ct.set_output(transform='pandas')
        x_test = numeric_median_imputer_ct.transform(x_test)

        # minmax scaler
        x_test = pd.DataFrame(minmax_scaler.transform(x_test), columns=minmax_scaler.get_feature_names_out())

        # Label encoder
        if y_test is not None:
           y_test = label_encoder.transform(y_test)

        print('Successfully Preprocessed Data')
        return x_test, y_test, label_encoder           
    except Exception as e:
        print(f"Failed To Preprocess Data: {e}')
        return 
