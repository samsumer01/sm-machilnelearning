import streamlit as st
import pandas as pd 
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier

st.title('🤖 Machine learning App')

st.info('This is app builds a machine learning model!')
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
df

