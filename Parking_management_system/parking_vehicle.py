import streamlit as st
from streamlit_lottie import st_lottie
from database import get_all_vehicles_from_db
import polars as pl
import requests
import time

st.set_page_config(
    page_title="Vehicle Parking Management System",
    page_icon="🚗",
)

def display():
    st.header("🚗 Parking Vehicles")
    st.text("")
    vehicles = get_all_vehicles_from_db()
    display = st.empty()
    with st.spinner('Please Wait !'):
        if vehicles:
            with display:
                url1 = requests.get("https://lottie.host/9f77d092-4412-4769-b01f-4bca9b341c69/1nvdDbQYQ6.json")
                if url1.status_code == 200:
                    url1_json = url1.json()
                else:
                    print("Error in the URL")
                st_lottie(url1_json, speed=1, width=300, height=300, key='add')
                time.sleep(6)
                columns = ["Vehicle Name", "Owner Name", "Contact Number", "Vehicle Type", "Charges"]
                df = pl.DataFrame(vehicles, columns, orient="row")
                st.table(df)
                time.sleep(2)

        else:
            st.write("##### No vehicles in parking")


hide = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide, unsafe_allow_html=True)


if _name_ == "_main_":
    display()