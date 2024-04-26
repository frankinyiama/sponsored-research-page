import streamlit as st
from functions import *

with open('./main.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

left_co, cent_co, last_co = st.columns(3)
with cent_co:
    st.image('fisk_logo_transparent.jpeg')

display_sponsored_research('General')
# display_sub_title('General')

# st.set_page_config(page_title="General") 