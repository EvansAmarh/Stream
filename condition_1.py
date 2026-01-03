import streamlit as st 

# # Display name
# def display_name(name):
#     st.info(f"**Name:** {name}")
# name = st.text_input("Please enter your name")
# if name:
#     display_name(name)
# else:
#     st.error("No name entered")
    
    
# Exception
col1, col2 = st.columns(2)
with col1:
    n1 = st.number_input("Enter a value", value=0, step=2)
with col2:
    n2 = st.number_input("Enter a second value", value=0, step=5)
try:
    st.info(f"**{n1}/{n2}=**{n1/n2}")
# except ZeroDivisionError:
#     st.error("Cannot divide by zero")
except Exception as e:
    st.error(f"Error: {e}")
    