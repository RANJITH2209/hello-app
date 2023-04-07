#importing packages
import streamlit as st
#from IPython.display import HTML
import pandas as pd


st.set_page_config(layout="wide")
#st.title("Team 5")

st.markdown("<h1 style='font-family: cursive; text-align: center;'>Team Senti5</h1>", unsafe_allow_html=True)
st.markdown(
    "<h1 style='text-align: center;'><img src='https://icons.iconarchive.com/icons/dtafalonso/android-lollipop/512/Youtube-icon.png' height='50'/> Smart Youtube Results</h1>",
    unsafe_allow_html=True
)

st.markdown("<h2 style='text-align: right; font-size: 20px;'> ~ From the students of Praxis Business School, Bangalore</h2>", unsafe_allow_html=True)

st.subheader("Search")
topic = st.text_input("")

if topic != "":
  st.markdown("Fetching results, Please wait...")
