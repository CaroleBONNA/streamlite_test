import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np

st.title('Hello Wilders, welcome to my application!')
st.write("I enjoy to discover streamlit possibilities")
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)
st.write(df_weather)
st.line_chart(df_weather['MAX_TEMPERATURE_C'])
viz_correlation = sns.heatmap(df_weather.select_dtypes('number').corr(),
                              cmap="vlag")
st.pyplot(viz_correlation.figure)
name = st.text_input("Please give me your name :")
name_length = len(name)
st.write("Your name has ", name_length, "characters")