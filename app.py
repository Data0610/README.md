import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el archivo CSV
data = pd.read_csv('datos.csv')

# Título de la aplicación
st.header("Análisis de Datos con Streamlit")

# Botón para construir el histograma
if st.button('Construir Histograma'):
    fig = px.histogram(data, x='nombre_columna')  # Reemplaza 'nombre_columna' con la columna que desees visualizar
    st.plotly_chart(fig)  # Muestra el gráfico
