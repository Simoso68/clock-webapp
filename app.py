import streamlit as st
import pytz as tz
from time import time, sleep
from datetime import datetime

st.title("Clock")

TZ = st.selectbox("Select your time zone", tz.all_timezones)

st.write("## Unix Time:")

st.write(f"### Base10: {int(time())}")
st.write(f"### Binary: {bin(int(time())).replace('0b', '')}")

st.write("## Local Time:")

st.write(f"### Date (dd/mm/yyyy): {datetime.now(tz.timezone(TZ)).strftime('%d/%m/%Y')}")
st.write(f"### Time: {datetime.now(tz.timezone(TZ)).strftime('%H:%M:%S')}")

sleep(0.5) # Updates every 0.5 seconds

st.rerun()