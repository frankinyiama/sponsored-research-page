import streamlit as st
from functions import *

with open('./main.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

display_fisk_logo()

display_sponsored_research('Post Awards')

department = st.selectbox(
  'Department',
  ['Life and Physical Sciences','Math and Computer Science','ARts and Language ','Behavioral Sciences','Library'],
)

primary_investigator = department = st.selectbox(
  'Department',
  ['Sajid Hussain','Dr.Lei Qian','Dr.Ning Zang','Dr Fridous KAuser']
)

