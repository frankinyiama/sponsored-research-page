import streamlit as st


sidebar = st.sidebar
sidebar.write("Home")
sidebar.write("General")
sidebar.write("Directory")
sidebar.write("Pre-Awards / Proposals")
sidebar.write("Post-Awards")
sidebar.write("Donors")
sidebar.write("Overview")
sidebar.write("Office of Research")
sidebar.write("Contact")


col1, col2, col3 = st.columns([7.5, 10, 5]) 
col2.title("Contacts")
col1, col2, col3 = st.columns([10, 2, 10]) 
col1.image("/home/mayaajike/sponsored-research-page/sajid-hussain-headshot.jpeg", width=255)
col1.write(
'''**Dr. Sajid Hussain, PhD** \n
**Director, Office of Sponsored Research and Programs** \n
Phone: 615-329-8624 \n
Office: Cravath Hall, Room 110B \n
Email: shussain@fisk.edu''')


col3.image("/home/mayaajike/sponsored-research-page/Arnold-Burger-headshot-fisk-research-page.jpg", width=180)
col3.write('''
**Arnold Burger, PhD** \n
**Sr. Vice Provost for Faculty Initiatives** \n
Phone: 615-329-8516 \n
Office: Dubois Hall, Rm 240 \n
Email: aburger@fisk.edu \n''')





 