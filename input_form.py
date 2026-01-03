import streamlit as st
from datetime import date

# Form
with st.form("Feedback form"):
    st.header("A Quick Feedback")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Please enter your name", placeholder= "Your full name")
        ratings = st.slider("Rate this site(0=Worst, 10=Best)", 0, 5, 10)
    with col2:
        dob = st.date_input("Please enter your date of birth")
        recommend = st.radio("Would you recommend this site to others", ("Yes", "No"))
        submit = st.form_submit_button("Submit")
    # Handling form submission
    if submit:
        if not name.strip():
            st.error("Name cannot be empty. Please provide your name")
        elif dob > date.today():
            st.error("Date of birth cannot be in the future")
        else:
            st.success("Thank you for your feedback")
            st.write("**Name**", name)
            st.write("**DOB**", dob)
            st.write("**Rating**", ratings)
            st.write("**Would recommend?**", recommend)
            
    