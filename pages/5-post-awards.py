import streamlit as st

with open('./main.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.set_page_config(page_title="Post Awards")