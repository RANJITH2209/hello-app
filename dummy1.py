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
	      "Standardization in ML","confusion matrix"]

if (topic not in Topic_list) and (topic != ""):
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


#Logistic Regression

Senti5LogisticRegressionVidID = ['yIYKR4sgzI8', 'zAULhNrnuL4', 'XnOAdxOWXWg']
Senti5LogisticRegressionTitle = ['StatQuest: Logistic Regression',
 'Statistics 101: Logistic Regression, An Introduction',
 'Logistic Regression | Logistic Regression in Python | Machine Learning Algorithms | Simplilearn']
UTubeLogisticRegressionVidID = ['yIYKR4sgzI8', 'C5268D9t9Ak', '3tq4t41MsPc']
UTubeLogisticRegressionTitle = ['StatQuest: Logistic Regression',
 'Logistic Regression [Simply explained]',
 'Logistic Regression: An Introduction']
Logistic_Regression_data = [Senti5LogisticRegressionVidID,Senti5LogisticRegressionTitle,
			   UTubeLogisticRegressionVidID,UTubeLogisticRegressionTitle]
Meta_Data["Logistic Regression"] = Logistic_Regression_data

#Decision Tree

Senti5DecisionTreeVidID = ['RmajweUFKvM', 'coOTEc-0OGw', 'ZVR2Way4nwQ']
Senti5DecisionTreeTitle = ['Decision Tree In Machine Learning | Decision Tree Algorithm In Python |Machine Learning |Simplilearn',
 '1. Decision Tree | ID3 Algorithm | Solved Numerical Example | by Mahesh Huddar',
 'Decision Tree Classification Clearly Explained!']
UTubeDecisionTreeVidID = ['ZVR2Way4nwQ', '_L39rN6gz7Y', 'ydvnVw80I_8']
UTubeDecisionTreeTitle = ['Decision Tree Classification Clearly Explained!',
 'Decision and Classification Trees, Clearly Explained!!!',
 'Decision Analysis 3: Decision Trees']
	  
Decision_Tree = [Senti5DecisionTreeVidID,Senti5DecisionTreeTitle,
		UTubeDecisionTreeVidID,UTubeDecisionTreeTitle]
Meta_Data["Decision Tree"] = Decision_Tree

#p-value
Senti5pvalueVidID = ['KLnGOL_AUgA', '8Aw45HN5lnA', 'eyknGvncKLw']
Senti5pvalueTitle = ['Calculate the P-Value in Statistics - Formula to Find the P-Value in Hypothesis Testing',
 'P-Value Method For Hypothesis Testing',
 'P-value in statistics: Understanding the p-value and what it tells us - Statistics Help']

UTubepvalueVidID = ['CL9MsExcKfU', 'vemZtEM63GY', 'eyknGvncKLw']
UTubepvalueTitle = ['p-Value (Statistics made simple)',
 'p-values: What they are and how to interpret them',
 'P-value in statistics: Understanding the p-value and what it tells us - Statistics Help']
p_value = [Senti5pvalueVidID,Senti5pvalueTitle,
	  UTubepvalueVidID,UTubepvalueTitle]
Meta_Data["p-value"] = p_value

#Confidence intervals
Senti5CIVidID = ['tFWsuO9f74o', 'MUD390jtgQs', 'DT-fPG0Hff8']
Senti5CITitle = ['Understanding Confidence Intervals: Statistics Help',
 "Student's T Distribution - Confidence Intervals & Margin of Error",
 'How To Find The Z Score, Confidence Interval, and Margin of Error for a Population Mean']
UTubeCIVidID = ['hlM7zdf7zwU', 'ENnlSlvQHO0', 'tFWsuO9f74o']
UTubeCITitle = ['Confidence intervals and margin of error | AP Statistics | Khan Academy',
 'Confidence Interval [Simply explained]',
 'Understanding Confidence Intervals: Statistics Help']
CI = [Senti5CIVidID,Senti5CITitle,
     UTubeCIVidID,UTubeCITitle]
Meta_Data["Confidence intervals"] = CI

#Normal distribution
Senti5NormalDistVidID = ['mtbJbDwqWLE', 'p_KApjpyBHE', 'CjF_yQ2N638']
Senti5NormalDistTitle = ['The Normal Distribution and the 68-95-99.7 Rule (5.2)',
 'Normal Distribution: Calculating Probabilities/Areas (z-table)',
 'Standard Normal Distribution Tables, Z Scores, Probability & Empirical Rule  - Stats']
UTubeNormalDistVidID = ['xI9ZHGOSaCg', 'rzFX5NWojp0', 'gHBL5Zau3NE']

UTubeNormalDistTitle = ['Normal Distribution EXPLAINED with Examples',
 'The Normal Distribution, Clearly Explained!!!',
 'Normal Distribution & Probability Problems']

Normal_dist = [Senti5NormalDistVidID,Senti5NormalDistTitle,
	      UTubeNormalDistVidID,UTubeNormalDistTitle]
Meta_Data["Normal distribution"] = Normal_dist

#Gradient descent
Senti5GDVidID = ['sDv4f4s2SB8', 'IHZwWFHWa-w', 'fXQXE96r4AY']
Senti5GDTitle = ['Gradient Descent, Step-by-Step',
 'Gradient descent, how neural networks learn | Chapter 2, Deep learning',
 'Intro to Gradient Descent || Optimizing High-Dimensional Equations']
UTubeGDVidID = ['sDv4f4s2SB8', 'IHZwWFHWa-w', 'i62czvwDlsw']
UTubeGDTitle = ['Gradient Descent, Step-by-Step',
 'Gradient descent, how neural networks learn | Chapter 2, Deep learning',
 'Gradient Descent Explained']

GD = [Senti5GDVidID,Senti5GDTitle,
     UTubeGDVidID,UTubeGDTitle]
Meta_Data["Gradient descent"] = GD

#Standardization in ML
Senti5SDVidID = ['mnKm3YP56PY', 'bqhQ2LWBheQ', 'sxEqtjLC0aM']
Senti5SDTitle = ['Standardization Vs Normalization- Feature Scaling',
 'Normalization Vs. Standardization (Feature Scaling in Machine Learning)',
 'Standardization vs Normalization Clearly Explained!']
UTubeSDVidID = ['sxEqtjLC0aM', 'mnKm3YP56PY', '2mcEMRGW1eY']
UTubeSDTitle = ['Standardization vs Normalization Clearly Explained!',
 'Standardization Vs Normalization- Feature Scaling',
 'Standardization Feature Scaling || Lesson 24 || Machine Learning || Learning Monkey |']
SD = [Senti5SDVidID,Senti5SDTitle,
	  UTubeSDVidID,UTubeSDTitle]
Meta_Data["Standardization in ML"] = SD

#confusion matrix
Senti5CMVidID = ['AyP85ocS-8Y', 'Kdsp6soqA7o', '8Oog7TXHvFY']
Senti5CMTitle = ['Confusion Matrix ll Accuracy,Error Rate,Precision,Recall Explained with Solved Example in Hindi',
 'Machine Learning Fundamentals: The Confusion Matrix',
 'Making sense of the confusion matrix']
UTubeCMVidID = ['Kdsp6soqA7o', 'prWyZhcktn4', 'LxcRFNRgLCs']
UTubeCMTitle = ['Machine Learning Fundamentals: The Confusion Matrix',
 'Confusion Matrix In Machine Learning | Confusion Matrix Explained With Example | Simplilearn',
 'The Confusion Matrix : Data Science Basics']
cm = [Senti5CMVidID,Senti5CMTitle,
     UTubeCMVidID,UTubeCMTitle]
Meta_Data["confusion matrix"] = cm

if (topic in Topic_list) and (topic != ""):
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
