import streamlit as st
import pandas as pd

names_link = 'dataset.csv'
names_data = pd.read_csv(names_link)
st.title('Names Dataset')

st.write('Jesus Abraham Contreras Meneses')
st.write('zs22019956')
st.image("credencial.png")

st.dataframe(names_data)