import streamlit as st
import os 

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


st.title("Office of Sponsored Research and Emerging Initiatives.")
col1, col2, col3 = st.columns([5, 20, 10]) 
col2.image("/home/mayaajike/sponsored-research-page/research-page-group-pic.JPG", width=500)
st.write(
    '''
    The mission of Fisk University is to provide a rich academic experience steeped in the liberal arts tradition, where our faculty, staff, and students exhibit a passion for learning and personal growth. \n
    **The Office of Sponsored Research and Programs (OSP)** at Fisk University serves as an advocate for sponsored research; advise the administration of matters of regulatory compliance; 
    assist faculty, staff and students in finding funding opportunities; assist faculty with the development of proposals; and promote internal sponsorship of scholarly activities.

    The OSP endeavors to be the link between principal investigators (PIs) and funding agencies.  The objectives include the following:
    1. Promote grant opportunities for Faculty and Staff
    2. Increase the number of grants awarded yearly
    3. Assist with the grant submittal process
    4. Ensure Pre-Award Process is effective and efficient
    5. Reassure an open relationship between OSP and PIs.
    '''
)
col1, col2, col3 = st.columns([10, 20, 10]) 
col2.subheader("Fisk Research Symposium")
st.write(
    ''' 
        **The Annual Fisk Research Symposium (FRS)** is a time for celebrating our research, scholarship, and creative work accomplishments; it is a venue to showcase, disseminate, and share scholarly contributions with 
        other researchers and scholars. The poster presentation and dialogue with the researchers shows Fisk's commitment to critical thinking
        and inquiry-based learning. Every year, the symposiums reinforce our trust that students at Fisk receive the tools, techniques, and skills 
        essential to their intellectual growth.
    '''
)
col1, col2, col3 = st.columns([10, 20, 10]) 
col2.subheader("Photos of Previous FRS")
col1, col2, col3, col4, col5 = st.columns([5, 5, 5, 5, 5]) 
col1.write("[FRS 2024](https://photos.google.com/share/AF1QipPREGvqvf1IXn1UFDsqTcQ3meJQDJcCz1RC_ItWjE4yEa-G0QJdC3WZlf2Ppyz6qg?key=dlR2NzZHUF8tUWtxTTE0aVZFZ2ZwQzRIUXV5ZWZB)")
col2.write("[FRS 2023](https://photos.google.com/share/AF1QipNh2YLU5c5v6ejO_yxG1dcfiw4QZXUB-UFxT0I9z0Md_5UfbrBwDLhY0GoVUki87Q?key=OWlVNUVzRE1DN2FyTENkbnV5aDJ2Qm9WR0RXVHJR)")
col3.write("[FRS 2022](https://photos.google.com/share/AF1QipO_ZOYBGqlaJ2oVaIB5spPlIAk9-w0BwUUqkgsNOnO6EMghHahIIktV8jJRtNNnvA?key=dlhpWkpybXpmcWtLZGMtVW9mR1RGdC10SFFrdlVR)")
col4.write("[FRS 2019](https://photos.google.com/u/2/share/AF1QipPXYN71C5EEuB6woXwQiBo0FGxUFkf1i8XXDiUBEqyRWq4yF1BnrlVoQANVNWsnIQ?key=VlhuMVZCT05MNVFvN0FLbDBwcV9IaWNnRHdJMTJn)")
col5.write("[FRS 2018](https://photos.google.com/share/AF1QipMAu-QaO7ih-aO7QsrT-y5ZA3UqB7jE-K1BnTtODBF30KtvlLNklWnB2YfCPsaWhg?key=Ti11MHp3clpCa21IVlZ0Q1JxOEg1YUhDZmwwR2lR)")

