import streamlit as st
from streamlit_lottie import st_lottie
from database import add_vehicle_to_db, get_vehicle_count, duplicate_vehicle_exists
from dotenv import load_dotenv
import requests
import time
import os

st.set_page_config(
    page_title="Vehicle Parking Management System",
    page_icon="🚗",
)

load_dotenv()

# Retrieve parking limit from environment variable (default to 5 if not set)
default_parking_limit = int(os.getenv("PARKING_LIMIT", 5))


st.sidebar.header("Settings")
use_default_limit = st.sidebar.checkbox("Use Default Parking Limit", value=True)
if use_default_limit:
    parking_limit = default_parking_limit
    st.sidebar.write(f"Current Parking Limit (Fixed): {parking_limit}")
else:
    parking_limit = st.sidebar.number_input("Set Parking Limit", min_value=1, max_value=100,
                                            value=default_parking_limit)
    st.sidebar.write(f"Current Parking Limit (Custom): {parking_limit}")


vehicle_types = {
    "🛵 Two-Wheeler": 50.0,
    "🚗 Four-Wheeler": 100.0
}

def add():

    st.header("➕ Entering Vehicle")
    vehicle_name = st.text_input("Vehicle Name")
    owner_name = st.text_input("Owner Name")
    contact_number = st.text_input("Contact Number")

    vehicle_type = st.selectbox("Vehicle Type", options=list(vehicle_types.keys()))

    charges = vehicle_types[vehicle_type]
    st.write(f"Charges for selected vehicle type ({vehicle_type}): Rs. {charges:.2f} /-")

    if st.button("Add Vehicle"):
        add = st.empty()
        with st.spinner('Please Wait !'):
            if vehicle_name and owner_name and contact_number:
                if duplicate_vehicle_exists(vehicle_name, owner_name):
                    st.error(f"A vehicle named '{vehicle_name}' for owner '{owner_name}' already exists!")
                elif get_vehicle_count() < parking_limit:
                    with add:
                        url1 = requests.get("https://lottie.host/a5390648-8bfa-424e-8c04-2ec2c09a4999/chqlPIgzd6.json")
                        if url1.status_code == 200:
                            url1_json = url1.json()
                        else:
                            print("Error in the URL")
                        st_lottie(url1_json, speed=1, width=300, height=300, key='add')
                        time.sleep(5)
                        add_vehicle_to_db(vehicle_name, owner_name, contact_number, vehicle_type, charges)
                        st.success(f"Vehicle '{vehicle_name}' added successfully!")
                        time.sleep(2)
                    add.empty()
                else:
                    st.error("Parking is full! Cannot add more vehicles.")
            else:
                st.error("Please fill all the fields.")

hide = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide, unsafe_allow_html=True)


if _name_ == "_main_":
    add()