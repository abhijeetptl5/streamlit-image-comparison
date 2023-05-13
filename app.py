import streamlit as st

from streamlit_image_comparison import exif_transpose
from streamlit_image_comparison import read_image_as_pil
from streamlit_image_comparison import pillow_to_base64
from streamlit_image_comparison import local_file_to_base64
from streamlit_image_comparison import local_file_to_base64
from streamlit_image_comparison import pillow_local_file_to_base64
from streamlit_image_comparison import image_comparison

import glob
import random

images = glob.glob('/home/abhijeetpatil/modern_pathology/samples/*.jpeg')

IMAGE_TO_URL = {
    "sample_image_1": "https://user-images.githubusercontent.com/34196005/143309873-c0c1f31c-c42e-4a36-834e-da0a2336bb19.jpg",
    "sample_image_2": "https://user-images.githubusercontent.com/34196005/143309867-42841f5a-9181-4d22-b570-65f90f2da231.jpg",
}


st.set_page_config(
    page_title="Histopathology Quality Control",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="auto",
)

st.markdown(
    """
    <h2 style='text-align: center'>
    Histopathology Quality Control
    </h2>
    """,
    unsafe_allow_html=True,
)

with st.form(key="Streamlit Image Comparison"):
    col1, col2 = st.columns([3, 1])
    with col1:
        # img1_url = st.text_input("Image one URL:", value=IMAGE_TO_URL["sample_image_1"])
        img1_url = random.choice(images)
        img2_url = img1_url.replace('.jpeg', '_mask.png')

    #col1, col2 = st.columns([3, 1])
    #with col1:
        # img2_url = st.text_input("Image two URL:", value=IMAGE_TO_URL["sample_image_2"])
        # img2_url = img1_url.replace('.jpeg', '_mask.png')

    # col1, col2 = st.columns([1, 1])
    # with col1:
    #     starting_position = st.slider(
    #         "Starting position of the slider:", min_value=0, max_value=100, value=50
    #     )
    # with col2:
    #     width = st.slider(
    #         "Component width:", min_value=400, max_value=1000, value=700, step=100
    #     )

    # col1, col2, col3, col4 = st.columns([1, 3, 3, 3])
    # with col2:
    #     show_labels = st.checkbox("Show labels", value=True)
    # with col3:
    #     make_responsive = st.checkbox("Make responsive", value=True)
    # with col4:
    #     in_memory = st.checkbox("In memory", value=True)

    # centered submit button
    col1, col2, col3 = st.columns([6, 4, 6])
    with col2:
        submit = st.form_submit_button("Update Render 🔥")

static_component = image_comparison(
    img1=img1_url,
    img2=img2_url,
    label1='',
    label2='',
    width=700,
    starting_position=50,
    show_labels=True,
    make_responsive=True,
    in_memory=True,
)
