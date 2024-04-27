import streamlit as st
from functions import *

with open('./main.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

display_fisk_logo()

display_sponsored_research('Office of Sponsored Researches')
