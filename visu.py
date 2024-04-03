import streamlit as st 
import PIL as pl
import os
import io
import folium
from streamlit_folium import folium_static
st.markdown("<h2 style='text-align: center;'>BALAENOPTERA BORELIS;  BALLENA SEI</h2>", unsafe_allow_html=True)

imagen_path = "imagen/Balaenoptera_borealis.jpg"
imagen_ballena = open(imagen_path, 'rb').read()
st.image(imagen_ballena, caption='Ballena', use_column_width=True)

# Mostrar texto diferente según la opción seleccionada
if st.button('Datos sobre la ballena'):
    # Mostrar las opciones en un expander
    with st.expander('Origen del nombre'):
        st.write('La palabra Sei es de origen noruego y significa bacalao, porque habitualmente esta ballena ha sido observada junto a manchas de bacalao ')
        
    with st.expander('Distribución de la localización'):
        st.write("-Desde los 60 grados al Sur a 60 Norte")
        st.write("-En la migración no frecuenta los mismos sitios de un año a otro")
    
    with st.expander('Reproducción'):
        st.write("-Gestación entre 11 y 12 meses ")
        st.write("-Las crías normalmente nacen en invierno")
        st.write("-Dan a luz en intervalos de 2 a 3 años")
    with st.expander('Alimentación'):
        st.write("-Peces pequeños")
        st.write("-Calamares ")
        st.write("-Planton")
    with st.expander('Distribución del cuerpo'):
        st.write("-Posee entre 30 y 60 plieges ventrales ")
        st.write("-Cuerpo relativamente delgado y de color gris")
        st.write("-Alcanza un tamaño de hasta 19.5 m")
        st.write("-Alcanza un peso de 45 toneladad")
    with st.expander('Curiosidades'):
        st.write("-Prefiere las aguas profundas ")
        st.write("-Difiere de otros de otros rocuales en la imposibilidad de prever sus movimientos migratorios ")
        st.write("-Se mueve en solitario o en grupos pequeños")

data = {
    'Fecha': ['Enero de 1963', 'Febrero de 1975'],
    'Longitud': [10.28, 10.27],
    'Provincia': ['Granma', 'Santiago de Cuba']
}

st.write('Avistamientos en Cuba :')
st.table(data)

# Crear un mapa centrado en Cuba
m = folium.Map(location=[20.0, -75.0], zoom_start=7)

# Agregar marcador para la costa norte de Manzanillo, Granma
folium.Marker([20.3335, -77.1160], popup='Manzanillo, Granma').add_to(m)

# Agregar marcador para la costa sur de Playa Mar Verde, Santiago de Cuba
folium.Marker([19.8654, -76.2976], popup='Mar Verde, Santiago de Cuba').add_to(m)

# Función para obtener la provincia al hacer clic en un marcador
def get_province(lat, lon):
    if lat == 20.3335 and lon == -77.1160:
        return 'Granma'
    elif lat == 19.8654 and lon == -76.2976:
        return 'Santiago de Cuba'
    else:
        return 'Desconocido'

# Mostrar el mapa en Streamlit
folium_static(m)
