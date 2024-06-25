#import os
import streamlit as st
import pandas as pd
import plotly_express as px

#path = os.path.dirname(os.getcwd()) + "\\vehicles_us.csv"

car_data = pd.read_csv("vehicles_us.csv")

st.header('Proyecto Srpint 5: Análisis de datos de vehículos.')

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir diagrama de dispersión') # crear un botón
        
if scatter_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.scatter(car_data,x="odometer",y="price")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)