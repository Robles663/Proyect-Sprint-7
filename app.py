import streamlit as st
import pandas as pd
import plotly_express as px

# Lectura del dataframe
car_data = pd.read_csv("vehicles_us.csv")

# Funciones para modificar el estado


def state_hist():
    """Modifica el estado a true
    """
    st.session_state.show_hist = True


def state_scatter():
    """Modifica el estado a true
    """
    st.session_state.show_scatter = True


def state_model_hist():
    """Modifica el estado a true
    """
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

# Relacion entre tipo, precio y modelo
t_p = car_data.groupby(['type', 'model_year'])['price'].mean().reset_index()

fig2 = px.scatter(t_p, x='model_year', y='price', color='type', title='Precio promedio por modelo y año de saldia',
                  labels={'model_year': "Año de salida", "price": "Precio (USD)"}, color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig2, use_container_width=True)

# Grafica con las condiciones de los carros
condition_chart = car_data.groupby('condition')['fuel'].count(
).reset_index()  # Obtener la cantidad carros de cada condicion
condition_chart = condition_chart.rename(columns={'fuel': 'cuantity'})

fig3 = px.pie(condition_chart, names="condition", values="cuantity", color_discrete_sequence=px.colors.qualitative.Set2,
              title="Condiciones de los carros en la pagina.",
              category_orders={"condition": ["excellent", "good", "like new", "fair", "new", "salvage"]})

st.plotly_chart(fig3, use_container_width=True)
