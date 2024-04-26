import streamlit as st
from st_pages import Page, show_pages
from functions import *

with open('./main.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

display_fisk_logo()

display_title("Welcome to the Sponsored Researches Page")

show_pages(
   [
       Page("main.py", "Home"),
       Page("pages/2-general.py", "General"),
       Page("pages/3-directory.py", "Directory"),
       Page("pages/4-proposals.py", "Pre-Awards/Proposals"),
       Page("pages/5-post-awards.py", "Post-Awards"),
       Page("pages/6-donors.py", "Donors"),
       Page("pages/7-overview.py", "Overview"),
       Page("pages/8-office.py", "Office of Research"),
       Page("pages/9-contact.py", "Contact"),
   ]
)