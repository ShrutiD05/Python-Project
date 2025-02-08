import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import base64

st.header("Vehicle Parking Management System (VPMS)")
st.info("Welcome to our project")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.text("")
    st.text("")

with col2:
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    want_to_contribute = st.button("Explore our project")
    if want_to_contribute:
        switch_page("home")

with col3:
    st.text("")

hide = """
    <style>

        # footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        .css-1cypcdb {display: none;}
        }

    </style>
"""
st.markdown(hide, unsafe_allow_html=True)


@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


# img = get_img_as_base64("https://images.unsplash.com/photo-1542281286-9e0a16bb7366")

bg_img = """
<style>
.egzxvld5{

background-image: url("https://cdn.shopify.com/s/files/1/0048/1086/6803/articles/PCOS_2048x.jpg?v=1604611044");
background-repeat: no-repeat;
background-size: cover;

}


</style>
"""

st.markdown(bg_img, unsafe_allow_html=True)


# Define the image URL or path
background_image_url = "https://images.pexels.com/photos/1756957/pexels-photo-1756957.jpeg"

# Inject CSS to set the background image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url({background_image_url});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)