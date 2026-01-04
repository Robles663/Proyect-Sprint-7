import streamlit as st
import pandas as pd
import plotly_express as px

# Lectura del dataframe
car_data = pd.read_csv("vehicles_us.csv")

# Funciones para modificar el estado


def state_hist():
    st.session_state.show_hist = True


def state_scatter():
    st.session_state.show_scatter = True


def state_model_hist():
    st.session_state.show_model = True


# Verificar si el estado existe
if "show_hist" not in st.session_state:
    st.session_state.show_hist = False

if "show_scatter" not in st.session_state:
    st.session_state.show_scatter = False

if "show_model" not in st.session_state:
    st.session_state.show_model = False

# Titulo
st.header("Graficas sobre la venta de vehiculos.")

# Botones
st.button("Construir histograma", on_click=state_hist)
st.button("Construir grafico de dispersion", on_click=state_scatter)
st.button("Crear histograma por año del modelo", on_click=state_model_hist)

# Creando histograma
if st.session_state.show_hist:
    st.write(
        "Creacion de un histograma para el conjunto de anuncios de venta de coches")
    hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(hist, use_container_width=True)
if st.session_state.show_scatter:
    st.write("Creando grafico de dispersion")
    scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(scatter, use_container_width=True)

if st.session_state.show_model:
    st.write("Creando histograma por año del modelo")
    model_hist = px.histogram(car_data, x="model_year")
    st.plotly_chart(model_hist, use_container_width=True)
