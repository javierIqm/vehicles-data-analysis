# Importar las bibliotecas necesarias
import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.title("Análisis Exploratorio de Datos")

# Subtítulo
st.write("Esta aplicación permite cargar un archivo CSV y realizar un análisis exploratorio de datos.")

# Cargar datos
st.header("Cargar datos")
uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv"])

# Verificar si se cargó un archivo
if uploaded_file is not None:
    # Leer el archivo CSV
    df = pd.read_csv(uploaded_file)

    # Mostrar los datos cargados
    st.header("Datos cargados")
    st.write(df)

    # Análisis exploratorio
    st.header("Análisis Exploratorio")
    st.write("Resumen estadístico de los datos:")
    st.write(df.describe())

    # Gráfico interactivo
    st.header("Gráfico Interactivo")
    st.write("Selecciona las columnas para crear un gráfico de dispersión.")

    # Seleccionar columnas para el gráfico
    column_x = st.selectbox("Selecciona la columna para el eje X", df.columns)
    column_y = st.selectbox("Selecciona la columna para el eje Y", df.columns)

    # Crear el gráfico con Plotly Express
    fig = px.scatter(df, x=column_x, y=column_y, title=f"{column_x} vs {column_y}")

    # Mostrar el gráfico en la aplicación
    st.plotly_chart(fig)

else:
    st.write("Por favor, sube un archivo CSV para comenzar.")