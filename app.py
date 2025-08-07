import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

#Encabezado 
st.header('Venta de Vehículos')

# Construimos un botón para construir un histograma

# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)


# Construimos un botón para construir un gráfico de dispersión

# Crear un botón en la aplicación Streamlit
dis_button = st.button('Construir Gráfico de Dispersión')

# Lógica a ejecutar cuando se hace clic en el botón
if dis_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un Gráfico de Dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un gráfico de dispersión utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Relación entre Odómetro y Precio')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)


# Usamos checkbox en lugar de botones

# Crear un botón en la aplicación Streamlit
build_histogram = st.checkbox('Construir un histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón en la aplicación Streamlit
build_dispersion = st.checkbox('Construir Gráfico de Dispersión')

# Lógica a ejecutar cuando se hace clic en el botón
if build_dispersion:# si la casilla de verificación está seleccionada
    # Escribir un mensaje en la aplicación
    st.write('Creación de un Gráfico de Dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Relación entre Odómetro y Precio')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)