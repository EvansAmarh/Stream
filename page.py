import streamlit as st 
from PIL import Image

icon = Image.open("favicon.ico")
st.set_page_config(
    page_title="The Big Benz",
    page_icon=icon,
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        "Get help": "https://streamlit.io/",
        "Report a bug": "https://github.com",
        "About": "About this app: **The Benz**"
    }
) 
title = "The Benz"
st.sidebar.title(title)
st.title(title)

# Customizing CSS to hide header and footer
hide_streamlit_style = """
    <style>
    /* Hide Streamlit header */
    header {
        visibility: hidden;
    }
    /* Hide Streamlit footer */
    footer {
        visibility: hidden;
    }
    </style>
"""
st.markdown(hide_streamlit_style,
unsafe_allow_html=True)

# Add custom footer to the sidebar
custom_footer_style = """
    <div class="markdown-text-container stText" style="width: 698px;">
    <footer><p></p></footer>
    <div style="font-size: 12px;">Hello world v 0.1</div>
    <div style="font-size: 12px;">Hello world LLC.</div></div>
"""
st.sidebar.markdown(custom_footer_style,
unsafe_allow_html=True)
    
