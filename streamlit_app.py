import streamlit as st
import pandas as pd 
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier

st.title('🤖 Machine learning App')

st.info('This is app builds a machine learning model!')

# with st.expander('Data'):
  # st.write("**Raw Data**")
df=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
dp
