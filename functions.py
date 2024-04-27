import streamlit as st

def display_fisk_logo():
    left_co, cent_co, last_co = st.columns(3)
    with cent_co:
        st.image('pictures/fisk_logo_transparent.jpeg')
        
def display_title(title):
    output = f'''
        <h1 
            style='
                text-align: center; 
                color: black;
                '>{title}
        </h1>
        '''
    st.markdown(output, unsafe_allow_html=True)

def display_sub_title(title):
    output = f'''
        <h1 
            style='
                text-align: left; 
                color: black;
                '>{title}
        </h1>
        '''
    st.markdown(output, unsafe_allow_html=True)

def display_sponsored_research(subtitle):
    title = "Sponsored Researches"
    output = f'''
        <h1 
            style='
                text-align: center; 
                color: black;
                '>{title}
        </h1>
        '''
    st.markdown(output, unsafe_allow_html=True)

    output = f'''
        <h2 
            style='
                text-align: center; 
                color: black;
                '>{subtitle}
        </h2>
        '''
    st.markdown(output, unsafe_allow_html=True)