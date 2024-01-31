import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
st.title('Analyse de corrélation et de distribution')

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_car = pd.read_csv(link)
st.write(df_car)

#Liste des valeurs unique de la colonne continent 
val_unique = df_car['continent'].unique()

#Création de bouton de choix
select_choice = st.multiselect("Selectionner un continent :", val_unique)

#filtrer la df en fonction du continant selectionné

df_car_filtre = df_car[df_car['continent'].isin(select_choice)]

st.write("Corrélation")

#name = st.text_input("Please give me your name :")
fig, ax = plt.subplots()
sns.heatmap(df_car_filtre.select_dtypes('number').corr(), cmap="vlag", annot=True, ax=ax)
st.pyplot(fig)

st.write("Analyse du poids / puissance moteur ")

st.scatter_chart(data=df_car_filtre, x='weightlbs', y='cubicinches')

st.write("Analyse du poids / hp ")

st.line_chart(data=df_car_filtre, x='weightlbs', y='hp')

