from pickle import FALSE
import streamlit as st
from streamlit_option_menu import option_menu
import json
from pathlib import Path
from PIL import Image
from streamlit_lottie import st_lottie
import requests  # pip install requests

st.markdown(
    """
<style>
body {
    background-color: blue;
}
</style>
""",
    unsafe_allow_html=True,
)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def show():
    with st.sidebar:

        st.markdown(
            """
                    # Crop Predicition
                    """,
            unsafe_allow_html=False,
        )

        selected = option_menu(
            menu_title=None,  # required
            # options = ["Text", "IMDb movie reviews", "Image", "Audio", "Video", "Twitter Data", "Web Scraping"], #required
            # icons = ["card-text", "film", "image", "mic", "camera-video", "twitter", "globe"], #optional
            options=[
                "Home",
                "Text",
                "Predict",
                "About",
                "Contact",
                "Help",
            ],  # required
            icons=[
                "house",
                "card-text",
                "lightbulb",
                "info",
                "phone",
                "exclamation-circle",
            ],  # optional
            # menu_icon="cast", #optional
            default_index=0,  # optional
            styles={
                "container": {
                    "padding": "0!important",
                    "background-color": "#D6F5E1",
                },
                "sidebar": {"background-color": "greenyellow"},
                "icon": {"color": "black", "font-size": "25px"},
                "nav-link": {
                    "font-size": "20px",
                    "text-align": "left",
                    "margin": "0px",
                    # "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": " #278768"},
            },
        )
        lottie_hello = load_lottieurl(
            "https://lottie.host/c07b6c29-b864-4778-818e-31343fdfe521/XHvQsxmUDG.json"
        )
        st_lottie(lottie_hello, key="helloooo")
        # lottie_chn = load_lottieurl("https://lottie.host/ce8a7374-11e5-4616-b122-f335165a6397/NoseKTHg8j.json")
        # st_lottie(lottie_chn,key="chn")
        return selected
