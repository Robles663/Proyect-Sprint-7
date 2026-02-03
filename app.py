import streamlit as st
import pandas as pd
import plotly_express as px

# Lectura del dataframe
car_data = pd.read_csv("vehicles_us.csv")

# Funcion para crear histogramas


def hist_plot(tabla, x_name, titulo, labels=None):
    kwargs = {}
    if labels is not None:
        kwargs['labels'] = labels

    hist_fig = px.histogram(tabla, x=x_name, title=titulo, **kwargs)
    return hist_fig

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
st.header("Graficas sobre la venta de vehiculos y sus anuncios.")

# Botones
st.button("Construir histograma entre cantidad de anuncios-odometro",
          on_click=state_hist)
st.button("Construir grafico de dispersion entre el precio y odometro",
          on_click=state_scatter)
st.button("Crear histograma con respecto al año del modelo",
          on_click=state_model_hist)

# Creando histograma
if st.session_state.show_hist:
    st.write(
        "Creacion de un histograma para el conjunto de anuncios de venta de coches")
    hist = hist_plot(car_data,
                     'odometer',
                     'Cantidad de anuncios por odometro')
    st.plotly_chart(hist, width="stretch")
if st.session_state.show_scatter:
    st.write("Creando grafico de dispersion")
    scatter = px.scatter(car_data, x="odometer", y="price", title='Grafica - Odometro',
                         labels={'odometer': 'Odometro', 'price': 'Precio (USD)'})
    st.plotly_chart(scatter, width="stretch")

if st.session_state.show_model:
    st.write("Creando histograma por año del modelo")
    model_hist = hist_plot(car_data,
                           'model_year',
                           "Histograma por año de salida",
                           {"model_year": "Año"})
    st.plotly_chart(model_hist, width="stretch")


st.header("Graficas comparativas entre las caracteristicas de los vehiculos y sus dias en las paginas.")

# Grafica con las condiciones de los carros
condition_chart = car_data.groupby('condition')['fuel'].count(
).reset_index()  # Obtener la cantidad carros de cada condicion
condition_chart = condition_chart.rename(columns={'fuel': 'cuantity'})

fig3 = px.pie(condition_chart, names="condition", values="cuantity", color_discrete_sequence=px.colors.qualitative.Set2,
              title="Condiciones de los carros en la pagina.",
              category_orders={"condition": ["excellent", "good", "like new", "fair", "new", "salvage"]})

st.plotly_chart(fig3, width="stretch")

# Grafica de los carros que se venden en menos de 5 dias.
car_data_copy = car_data.copy()  # Copia del dataframe y se hace filtrado
car_data_copy = car_data_copy.sort_values(
    by="days_listed").reset_index(drop=True)
car_data_copy = car_data_copy[['model_year', 'type',
                               'condition', 'odometer', 'days_listed']]

# Carros que duren menos de 5 dias  en venderse
days = car_data_copy[car_data_copy["days_listed"] <= 5]
group_days = days.groupby('type')['odometer'].count().reset_index()
fig4 = px.pie(group_days, title="Tipos de carros con mayores ventas", names='type', values='odometer',
              color_discrete_sequence=px.colors.qualitative.Set2)

st.plotly_chart(fig4, width="stretch")

# Relacion entre tipo, precio y modelo
t_p = car_data.groupby(['type', 'model_year'])['price'].mean().reset_index()

fig2 = px.scatter(t_p, x='model_year', y='price', color='type', title='Precio promedio por modelo y año de saldia',
                  labels={'model_year': "Año de salida", "price": "Precio (USD)"}, color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig2, width="stretch")

# Relacion entre el precio y tipo de carro de los ultimos 10 años
less_10 = car_data[car_data['model_year'] >= 2004]
fig5 = px.scatter(less_10, x='model_year', y='price', color='type', title='Relacion entre el precio y tipo de carro (ultimos 15 años)', labels={
                  "model_year": "Año de salida", "price": "Precio (USD)"}, color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig5, width="stretch")

# Relacion entre el precio-odometro y tipo de carro de los ultimos 15 años
fig6 = px.scatter(less_10, x='odometer', y='price', color='type', title='Relacion entre el precio y millas recorridas (ultimos 15 años)', labels={
                  "model_year": "Año de salida", "price": "Precio (USD)"}, color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig6, width="stretch")

# Comparacion de precios entre modelos
st.title('Comparar precios entre modelos')
model_1 = st.selectbox(
    "Seleccione un modelo",
    sorted(car_data['model'].unique()))

model_2 = st.selectbox(
    "Seleccione un modelo para comparar",
    sorted(car_data['model'].unique())
)
normalize = st.checkbox("Normalizar el histograma", value=True)


filtered_model = car_data[car_data['model'].isin([model_1, model_2])]

histnorm = "percent" if normalize else None

comp_model = px.histogram(filtered_model, x='price', color='model',
                          opacity=0.6, title='Histograma entre modelos',
                          histnorm=histnorm)
st.plotly_chart(comp_model, width='stretch')
