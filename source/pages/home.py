import streamlit as st
from streamlit_lottie import st_lottie
import json

from source.assets.animation_paths import animation_developer

class Startseite():

    def __init__(self):
        pass
    
    def show(self):
        def load_lottiefile(filepath: str):
            with open(filepath, "r") as f:
                return json.load(f)
        
        # ---- LOAD ASSETS ----
        lottie_wood = load_lottiefile(animation_developer)

        # ---- HEADER SECTION ----
        with st.container():
            st.markdown("<h1 style='text-align: center;'>Softwaretechnik-Mock</h1>", unsafe_allow_html=True)
            st.write("##")

            first_column, second_column = st.columns(2)
            with first_column:
                st.write(
                    """<p style='font-size: 20px;'>
                    Mit diesem Framework kann man relativ leicht Webseiten in Python entwickeln.""",
                    unsafe_allow_html=True 
                )
                st.write(
                    """<p style='font-size: 20px;'>
                    Es existieren zahlreiche Tutorials auf YouTube. Wie z.B. dieses hier für eine einfache Seite:""",
                    unsafe_allow_html=True
                )
                st.write(
                    "[Klick mich >](https://www.youtube.com/watch?v=VqgUkExPvLY)"
                )
                st.write(
                    """<p style='font-size: 20px;'>
                    Oder dieses für den Login:""",
                    unsafe_allow_html=True
                )
                st.write(
                    "[Ich bin klickbar >](https://www.youtube.com/watch?v=eCbH2nPL9sU)"
                )
                st.write(
                    """<p style='font-size: 20px;'>
                    Solche Animationen kann man sich als JSON von dieser Website herunterladen:""",
                    unsafe_allow_html=True 
                )
                st.write(
                    "[LottieFiles >](https://app.lottiefiles.com/)"
                )
                st.write(
                    """<p style='font-size: 20px;'>
                    Und dann einfach in die eigene Webseite einbinden.""",
                    unsafe_allow_html=True 
                )

            with second_column:
                st_lottie(
                    lottie_wood
                )
                

       