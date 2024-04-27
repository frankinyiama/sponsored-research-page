import streamlit as st
from functions import *

with open('./main.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

display_fisk_logo()

display_sponsored_research('Proposals')

st.text_area(
    'Multipurpose, Radiation- and Temperature Resistant Semiconductor (Burger Arnold)',
    "This research focuses on developing a multipurpose semiconductor material that is highly resistant to radiation and temperature variations. The semiconductor material is designed to maintain its functionality and stability in harsh environments, making it suitable for a wide range of applications, including aerospace, nuclear, and automotive industries. The study explores the material's properties and its potential uses in various electronic devices subjected to extreme conditions."
)

st.text_area(
    'RIA: Designing Synthetic Polyglycidol-based Polymeric Networks (Beezer, Dain)',
    'This research investigates the design of synthetic polyglycidol-based polymeric networks. The study explores the synthesis and characterization of these networks, focusing on their potential applications in various fields such as drug delivery, tissue engineering, and coatings. The research aims to understand the structure-property relationships of these polymeric networks, enabling the development of new materials with tailored properties for specific application'
  )