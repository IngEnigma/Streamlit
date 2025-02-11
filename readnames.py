import streamlit as st
import pandas as pd

names_link = 'dataset.csv'
names_data = pd.read_csv(names_link)
st.title('Names Dataset')
st.dataframe(names_data)