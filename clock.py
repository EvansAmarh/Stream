import streamlit as st 
from datetime import datetime

st.title("Clock")
clock = st.empty()
# Loop for continuous update
while True:
    time = datetime.now().strftime("%H:%M:%S")
    clock.info(f'**Current time:** {time}')
    if time > '21:19:15':
    # Clear the time display when the alarmcondition is met and display the alarm
        clock.empty()
        st.warning('Alarm!!')
        break