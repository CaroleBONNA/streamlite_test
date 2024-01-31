import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
st.title('Analyse de corrélation et de distribution')

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_car = pd.read_csv(link)
st.write(df_car)


#st.line_chart(df_weather['MAX_TEMPERATURE_C'])
#name = st.text_input("Please give me your name :")
fig, ax = plt.subplots()
sns.heatmap(df_car.select_dtypes('number').corr(), cmap="vlag", ax=ax)
st.pyplot(fig)