import streamlit as st
import pandas as pd
import plotly_express as px

# Lectura del dataframe
car_data = pd.read_csv("vehicles_us.csv")

# Creando histograma
st.header("Graficas sobre el marketing de vehiculos.")
hist_button = st.button("Construir histograma.")  # Crea boton

if hist_button:
    st.write(
        "Creacion de un histograma para el conjunto de anuncios de venta de coches")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Creando grafico de dispersion
scatter_button = st.button("Construir grafico de dispersión.")  # Crea boton

if scatter_button:
    st.write("Creando grafico de dispersión.")
    fig1 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig1, use_container_width=True)

# Creando histograma del year modelo
model_button = st.button("Histograma por año del modelo")

if model_button:
    st.write("Creando un histograma con el año de salida")
    fig_year = px.histogram(car_data, x="model_year")
    st.plotly_chart(fig_year, use_container_width=True)
