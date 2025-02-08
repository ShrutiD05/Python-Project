import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Vehicle Parking Management System",
    page_icon="🚗",
)
def home():

    st.header("Vehicle Parking Management System (VPMS)")
    image = Image.open('images/logo.jpeg')

    col1, col2, col3 = st.columns([3, 6, 3])

    with col1:
        st.write("")
        st.write("")
    with col2:
        st.write("")
        st.image(image, caption='Vehicle Parking Management System (VPMS)',width=300)
        st.write("")
    with col3:
        st.write("")

    st.text("Vehicle Management System is to streamline the management of vehicle parking. "
            "\nThe system allows users to add and remove vehicles from a parking lot, "
            "\nview a list of all parked vehicles, and manage parking limits. The system "
            "\nsupports different types of vehicles with associated charges and allows for "
            "\nboth fixed and custom parking limits.")


    hide = """
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            
        </style>
    """
    st.markdown(hide, unsafe_allow_html=True)

if _name_ == "_main_":
    home()