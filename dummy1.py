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

Topic_list = ["KNN","Linear Regression","Logistic Regression","Decision Tree","p-value",
	      "Confidence intervals","Normal distribution","Gradient descent",
	      "Primary key in SQL","confusion matrix"]
if topic not in Topic_list:
	st.write("Please check the topic asssigned to you ! Re-enter the topic as it is....")
if topic in Topic_list:
	st.write("Fetching results, Please wait...")

width = 350
height =200
#Meta Data
Meta_Data = {}

## KNN

UTubeKNNVidID = ['CJjSPCslxqQ', 'HVXime0nQeI', '4HKqjENq9OU']



UTubeKNNTitle = ['K-Nearest Neighbor Classification ll KNN Classification Explained with Solved Example in Hindi',
 'StatQuest: K-nearest neighbors, Clearly Explained',
 'KNN Algorithm In Machine Learning | KNN Algorithm Using Python | K Nearest Neighbor | Simplilearn']
Senti5KNNVidID = ['4HKqjENq9OU', 'CJjSPCslxqQ', 'IPqZKn_cMts']
Senti5KNNTitle = ['KNN Algorithm In Machine Learning | KNN Algorithm Using Python | K Nearest Neighbor | Simplilearn',
 'K-Nearest Neighbor Classification ll KNN Classification Explained with Solved Example in Hindi',
 'KNN Algorithm Explained with Simple Example   Machine Leaning']


KNN_data = [Senti5KNNVidID,Senti5KNNTitle,
			  UTubeKNNVidID,UTubeKNNTitle]
Meta_Data["KNN"] = KNN_data


## Linear Regression

Senti5LinearRegressionVidID = ['ZkjP5RJLQF4', 'zPG4NjIkCjc', 'owI7zxCqNY0']
Senti5LinearRegressionTitle = ['Statistics 101: Linear Regression, The Very Basics 📈',
 'An Introduction to Linear Regression Analysis',
 'Video 1: Introduction to Simple Linear Regression']

UTubeLinearRegressionVidID = ['zPG4NjIkCjc', 'nk2CQITm_eo', 'owI7zxCqNY0']

UTubeLinearRegressionTitle = ['An Introduction to Linear Regression Analysis',
 'Linear Regression, Clearly Explained!!!',
 'Video 1: Introduction to Simple Linear Regression']

Linear_Regression_data = [Senti5LinearRegressionVidID,Senti5LinearRegressionTitle,
			 UTubeLinearRegressionVidID,UTubeLinearRegressionTitle]

Meta_Data["Linear Regression"] = Linear_Regression_data

 







st.write("Results fetched")



col1, empty,col2 = st.columns(3)
col1.header("FrameWork 1")
col2.header("FrameWork 2")


try:
	for i in range(3):

		col1, empty,col2 = st.columns(3)

		youtube_vd_id1 = Meta_Data[topic][0][i] 
		html_code1 = f'<iframe width="{width}" height={height}" src="https://www.youtube.com/embed/{youtube_vd_id1}" frameborder="1" allowfullscreen></iframe>'
		col1.markdown(html_code1, unsafe_allow_html=True)
		col1.subheader(Meta_Data[topic][1][i])


		youtube_vd_id2 = Meta_Data[topic][2][i]
		html_code2 = f'<iframe width="{width}" height={height}" src="https://www.youtube.com/embed/{youtube_vd_id2}" frameborder="1" allowfullscreen></iframe>'
		col2.markdown(html_code2, unsafe_allow_html=True)
		col2.subheader(Meta_Data[topic][3][i])
except:
	st.write("")
