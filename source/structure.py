import streamlit as st
from streamlit_option_menu import option_menu

from source.pages.home import Startseite
from source.pages.bubblesort import Bubblesort

def main():
    
    st.set_page_config(page_title="Softwaretechnik-Mock", page_icon=":desktop_computer:", layout="wide")


    # Use local CSS
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
                
    # removes streamlit specific headers
    local_css("source/style/style.css")  


    with st.sidebar:
        selected = option_menu(
            menu_title = None,
            options = ["Home", "Bubblesort"],
            icons = ["house", "bar-chart"]  # insert bootstrap icon names here
        )


    if selected == "Home":
        start_screen = Startseite()
        start_screen.show()
    if selected == "Bubblesort":
        bubble_screen = Bubblesort()
        bubble_screen.show()

