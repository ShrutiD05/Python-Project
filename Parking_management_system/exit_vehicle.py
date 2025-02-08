import streamlit as st
from streamlit_lottie import st_lottie
from database import exit_vehicle_from_db, vehicle_exists
import requests
import time

st.set_page_config(
    page_title="Vehicle Parking Management System",
    page_icon="🚗",
)

def exit():
    st.header("🗑 Exiting Vehicle")
    remove_vehicle_name = st.text_input("Enter the Vehicle Name to Exit")

    if st.button("Exit Vehicle"):
        remove = st.empty()
        with st.spinner('Please Wait !'):
            if remove_vehicle_name:
                if vehicle_exists(remove_vehicle_name):
                    with remove:
                        url1 = requests.get("https://lottie.host/d30899bd-f2b7-4679-914b-8e00a4925981/tp0ZZoL5Jp.json")
                        if url1.status_code == 200:
                            url1_json = url1.json()
                        else:
                            print("Error in the URL")
                        st_lottie(url1_json, speed=1, width=300, height=300, key='add')
                        time.sleep(6)
                        exit_vehicle_from_db(remove_vehicle_name)
                        st.success(f"Vehicle '{remove_vehicle_name}' exited successfully!")
                        time.sleep(2)
                else:
                    st.error(f"Vehicle '{remove_vehicle_name}' does not exist!")
            else:
                st.error("Please enter a vehicle name.")

hide = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide, unsafe_allow_html=True)



if _name_ == "_main_":
    exit()