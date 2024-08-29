import pandas as pd
import streamlit as st 
from joblib import load

rf = load('RFmodel.joblib')
df_cars = pd.read_csv('cleaned_cars_data2.csv')



def predict(data):
    data = pd.DataFrame(data, index=[0])
    pred = rf.predict(data)
    return f'The predicted price of the Car is {round(pred[0], 3)} Lakhs'


st.sidebar.image('Cardekho_img.jpg')
st.sidebar.header("Give Specifications :")

bt = st.sidebar.selectbox(
    "Select body Type:",
    options=df_cars['bt'].unique(),
)

km = st.sidebar.number_input(
    "Enter total kilometers driven:",
    step=1,
    placeholder="Type a whole number..",
    min_value= 0
)

transmission = st.sidebar.selectbox(
    "select transmission:",
    options=['Manual', 'Automatic']
)

ownerNo = st.sidebar.number_input(
    "Enter number of owner:",
    step=1,
    placeholder="Type a whole number..",
    min_value= 0
)

oem =  st.sidebar.selectbox(
    "select the Brand:",
    options=df_cars['oem'].unique()
)

model = st.sidebar.selectbox(
    "select the model:",
    options=df_cars['model'].unique()
)

modelYear = st.sidebar.number_input(
    "Enter model Year:",
    step=1,
    placeholder="Type a Whole number XXXX..",
    min_value= 1900
)

Insurance = st.sidebar.selectbox(
    "select insurance type:",
    options=df_cars['Insurance Validity'].unique()
)

fuelType = st.sidebar.selectbox(
    "select fuel type:",
    options=df_cars['Fuel Type'].unique()
) 

Seats = st.sidebar.selectbox(
    "slect the number of seats:",
    options=df_cars['Seats'].unique()
)

Safety_count = st.sidebar.number_input(
    "Enter number of safety features:",
    step=1,
    placeholder="Type a Whole number..",
    min_value=0
)

feature_count = st.sidebar.number_input(
    "Enter number of top features:",
    step=1,
    placeholder="Type a Whole number..",
    min_value=0
)

Color = st.sidebar.selectbox(
    'select the car color:',
    options=df_cars['Color'].unique()
)

cylinders = st.sidebar.selectbox(
    'Select the number of cylinders:',
    options=df_cars['No of Cylinder'].unique()
)

TurboCharger = st.sidebar.selectbox(
    "Turbo charger:",
    options=df_cars['Turbo Charger'].unique()
)

SuperCharger = st.sidebar.selectbox(
    "super charger:",
    options=df_cars['Super Charger'].unique()
)

City = st.sidebar.selectbox(
    "select the City:",
    options=df_cars['City'].unique()
)

power = st.sidebar.number_input(
    "Enter the Power:",
    placeholder="Enter Max power..",
    min_value=0.0
)



input_dict = {
    'bt' : bt,
    'km' : km,
    'transmission' : transmission,
    'ownerNo' : ownerNo,
    'oem' : oem,
    'model' : model,
    'modelYear' : modelYear,
    'Insurance Validity' : Insurance,
    'Fuel Type' : fuelType,
    'Seats' : Seats,
    'Safety_count' : Safety_count,
    'top_features_count' : feature_count,
    'Color' : Color,
    'No of Cylinder': float(cylinders),
    'Turbo Charger' : TurboCharger,
    'Super Charger' : SuperCharger,
    'City' : City,
    'Power': power 
}

st.header('Car Price Prediction:')

if st.sidebar.button("Predict Price", type='primary'):
    res = predict(input_dict)
    st.success(res)



