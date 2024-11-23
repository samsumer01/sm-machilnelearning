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

# s(input_penguins, prefix=encode)

# X = df_penguins[1:]
# input_row = df_penguins[:1]

# # Encode y
# target_mapper = {'Adelie': 0,
#                  'Chinstrap': 1,
#                  'Gentoo': 2}
# def target_encode(val):
#   return target_mapper[val]

# y = y_raw.apply(target_encode)

# with st.expander('Data preparation'):
#   st.write('**Encoded X (input penguin)**')
#   input_row
#   st.write('**Encoded y**')
#   y


# # Model training and inference
# ## Train the ML model
# clf = RandomForestClassifier()
# clf.fit(X, y)

# ## Apply model to make predictions
# prediction = clf.predict(input_row)
# prediction_proba = clf.predict_proba(input_row)

# df_prediction_proba = pd.DataFrame(prediction_proba)
# df_prediction_proba.columns = ['Adelie', 'Chinstrap', 'Gentoo']
# df_prediction_proba.rename(columns={0: 'Adelie',
#                                  1: 'Chinstrap',
#                                  2: 'Gentoo'})

# # Display predicted species
# st.subheader('Predicted Species')
# st.dataframe(df_prediction_proba,
#              column_config={
#                'Adelie': st.column_config.ProgressColumn(
#                  'Adelie',
#                  format='%f',
#                  width='medium',
#                  min_value=0,
#                  max_value=1
#                ),
#                'Chinstrap': st.column_config.ProgressColumn(
#                  'Chinstrap',
#                  format='%f',
#                  width='medium',
#                  min_value=0,
#                  max_value=1
#                ),
#                'Gentoo': st.column_config.ProgressColumn(
#                  'Gentoo',
#                  format='%f',
#                  width='medium',
#                  min_value=0,
#                  max_value=1
#                ),
#              }, hide_index=True)


# penguins_species = np.array(['Adelie', 'Chinstrap', 'Gentoo'])
# st.success(str(penguins_species[prediction][0]))
