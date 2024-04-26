import streamlit as st
from functions import *

with open('./main.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 874a0f5 (Adding css)
left_co, cent_co, last_co = st.columns(3)
with cent_co:
    st.image('fisk_logo_transparent.jpeg')

display_sponsored_research('General')
<<<<<<< HEAD
=======
st.set_page_config(page_title="General") 
>>>>>>> 8c63bfc (Adding css to the pages)
=======
# display_sub_title('General')

# st.set_page_config(page_title="General") 
>>>>>>> 874a0f5 (Adding css)
