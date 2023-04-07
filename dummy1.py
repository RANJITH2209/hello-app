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

width = 350
height =200
L = ["PHxYNGo8NcI","FUY07dvaUuE", "ZVR2Way4nwQ","PYxDkGlpj_U","JcI5E2Ng6r4","ydvnVw80I_8","RmajweUFKvM","_L39rN6gz7Y","coOTEc-0OGw"]

col1, col2 = st.columns([1, 1])

# Add content to columns

name =["Machine Learning Tutorial Python - 9  Decision Tree","Decision Analysis 4 (Tree): EVSI - Expected Value of Sample Information",
"Decision Tree Classification Clearly Explained!",
"Decision Trees for A Level Business",
"Decision Tree: Important things to know",
"Decision Analysis 3: Decision Trees",
"Decision Tree In Machine Learning | Decision Tree Algorithm In Python |Machine Learning |Simplilearn",
"Decision and Classification Trees, Clearly Explained!!!",
"1. Decision Tree | ID3 Algorithm | Solved Numerical Example | by Mahesh Huddar"]

col1.header("Youtube Results")
for i in range(9):
		html_code = f'<iframe width="{width}" height={height}" src="https://www.youtube.com/embed/{L[i]}" frameborder="0" allowfullscreen></iframe>'
		# Display HTML code
		col1.markdown(html_code, unsafe_allow_html=True)
		col1.subheader(name[i])

col2.header("Smart Results")

for i in range(9):
		html_code = f'<iframe width="{width}" height={height}" src="https://www.youtube.com/embed/{L[i]}" frameborder="0" allowfullscreen></iframe>'
		# Display HTML code
		col2.markdown(html_code, unsafe_allow_html=True)
		col2.subheader(name[i])
