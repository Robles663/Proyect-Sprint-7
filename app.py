import streamlit as st
import pandas as pd
import plotly_express as px

# Lectura del dataframe
car_data = pd.read_csv("vehicles_us.csv")

st.header("Graficas sobre el marketing de vehiculos.")
hist_button = st.button("Construir histograma.")

if hist_button:
    st.write(
        "Creacion de un histograma para el conjunto de anuncios de venta de coches")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Construir grafico de dispersión.")

if scatter_button:
    st.write("Creando grafico de dispersión.")
    fig1 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig1, use_container_width=True)
