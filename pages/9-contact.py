import streamlit as st
from functions import *

with open('./main.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

display_fisk_logo()

display_sponsored_research('Contacts')

col1, col2, col3 = st.columns([10, 2, 10]) 
col1.image("pictures/sajid-hussain-headshot.jpeg", width=255)
col1.write(
'''**Dr. Sajid Hussain, PhD** \n
**Director, Office of Sponsored Research and Programs** \n
Phone: 615-329-8624 \n
Office: Cravath Hall, Room 110B \n
Email: shussain@fisk.edu''')


col3.image("pictures/Arnold-Burger-headshot-fisk-research-page.jpg", width=180)
col3.write('''
**Arnold Burger, PhD** \n
**Sr. Vice Provost for Faculty Initiatives** \n
Phone: 615-329-8516 \n
Office: Dubois Hall, Rm 240 \n
Email: aburger@fisk.edu \n''')