import streamlit as st

st.set_page_config(
    page_title="Vehicle Parking Management System",
    page_icon="🚗",
)

def info():
    st.header("🅰 About this project")
    st.text("")

    st.write("""
    
    *Features:*

    - *Entering (Add) Vehicle:*
        - *Functionality:* Allows users to add a new vehicle to the parking system.
        - *Inputs:*
            - Vehicle Name: The name or identifier of the vehicle.
            - Owner Name: The name of the person who owns the vehicle.
            - Contact Number: The contact number of the vehicle owner.
            - Vehicle Type: Type of vehicle (e.g., Two-Wheeler, Four-Wheeler) with associated icons.
            - Charges: Parking charges based on the vehicle type.
        - *Validation:* Checks if the number of vehicles is below the parking limit before adding a new vehicle.
        
    - *Exiting (Remove) Vehicle:*
        - *Functionality:* Allows users to remove a vehicle from the parking system.
        - *Inputs:*
            - Vehicle Name: The name or identifier of the vehicle to be removed.
        - *Validation:* Ensures that the vehicle name is provided before attempting to remove.

    - *Parking (Display) Vehicles:*
        - *Functionality:* Displays a list of all vehicles currently parked.
        - *Output:* Shows details such as Vehicle Name, Owner Name, Contact Number, Vehicle Type, and Charges in a table format.

    - *Parking Limit Management:*
        - *Fixed Limit:* A default parking limit value can be set and managed via an .env file, allowing the system to have a predetermined limit on the number of vehicles.
        - *Custom Limit:* Users can choose to set a custom parking limit dynamically via the Streamlit sidebar.

    *Technical Stack:*

    - *Frontend:*
        - *Streamlit:* A Python library used to build the web-based interface for interacting with the vehicle management system. Provides interactive components such as text inputs, select boxes, and tables.

    - *Backend:*
        - *MySQL:* A relational database management system used to store vehicle data, including vehicle name, owner details, vehicle type, and charges. The backend connects to the MySQL database to perform CRUD (Create, Read, Update, Delete) operations.

    - *Environment Management:*
        - *.env File:* Used to store configuration values such as the parking limit. The values from the .env file are loaded into the application using the python-dotenv package.

    *Database Schema:*

    - *Table:* vehicles
        - vehicle_name: The name or identifier of the vehicle (VARCHAR).
        - owner_name: The name of the vehicle owner (VARCHAR).
        - contact_number: The contact number of the vehicle owner (VARCHAR).
        - vehicle_type: The type of vehicle (e.g., Two-Wheeler, Four-Wheeler) (VARCHAR).
        - charges: The parking charges associated with the vehicle type (DECIMAL).

    *Implementation Details:*

    - *.env File Management:*
        The .env file contains environment-specific variables like the parking limit. This file is loaded at runtime to configure the parking limit, providing flexibility to adjust settings without modifying the code.

    - *Streamlit Sidebar:*
        The sidebar in the Streamlit application allows users to set the parking limit either to a fixed value from the .env file or to a custom value.

    - *Data Handling:*
        The application connects to the MySQL database to manage vehicle records. It ensures that the number of vehicles does not exceed the set parking limit and provides an interface for users to add, remove, and view vehicles.
    """)


hide = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide, unsafe_allow_html=True)

if _name_ == "_main_":
    info()