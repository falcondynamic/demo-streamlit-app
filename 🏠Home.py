import streamlit as st
import pandas as pd
import requests

st.header("My Bike Price Prediction App")

length_fork_mm = st.sidebar.slider("Please provide the travel length of the fork in millimeters.", min_value=30, max_value=200)
battery_wh = st.sidebar.slider("What is the watt-hour capacity of your electric bike's battery?", min_value=248, max_value=850)
frame_material= st.sidebar.selectbox("What material was used for the frame of your bicycle (e.g., aluminum, carbon, steel)?", ('Aluminium', 'Carbon', 'Aluminium-Carbon', 'Diamant', 'Aluminium-Stahl'))
number_of_gears=st.sidebar.slider("Please specify the number of gears on your bicycle.",min_value=1, max_value=30)
#bremse_vorne=st.sidebar.selectbox("Which brand of braking system located at the front of your bicycle (e.g., MAGURA HS-11 , Shimano MT-200).", ('Shimano MT-200'))
#schaltwerk=st.sidebar.selectbox("Which rear derailleur is installed on your bicycle? (e.g., Shimano Deore, SRAM GX)", ('Shimano ', 'Shimano Deore))
category=st.sidebar.selectbox("To which category does your bicycle belong? (e.g., mountain bike, road bike, electric bike)", ('Trekking', 'City', 'MTB_Hardtail', 'MTB_Fully'))                                                                                                          
manufacturer=st.sidebar.selectbox("Who is the manufacturer of your bicycle?", (  'Kalkhoff',
                                                                                'CUBE',
                                                                                'Haibike',
                                                                                'Hercules',
                                                                                'Winora',
                                                                                'SCOTT',
                                                                                'corratec',
                                                                                'Diamant',
                                                                                'GHOST',
                                                                                'Specialized',
                                                                                'Cannondale',
                                                                                'Canyon'))

my_dict = {
    "length_fork_mm": length_fork_mm,
    "battery_wh": battery_wh,
    "frame_material": frame_material,
    'number_of_gears': number_of_gears,
    "category": category,
    "manufacturer": manufacturer    
}

df = pd.DataFrame.from_dict([my_dict])


st.header("The configuration of your e-bike is below!")
st.table(df)

st.subheader("Press predict if configuration is okay!!!")

if st.button("Predict"):
    response = requests.get(f"https://demo-fastapi-jzlx.onrender.com/prediction/{length_fork_mm}/{battery_wh}/{frame_material}/{number_of_gears}/{category}/{manufacturer}").json()
    st.success("The estimated price of your e-bike is {}{}. ".format(response["unit"],int(response["prediction"])))