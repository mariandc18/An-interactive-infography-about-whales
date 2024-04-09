import streamlit as st
import importlib, Inicio, page1,page2,page3,page4,page5,page6,page7,page8,page9,page10,page11,page12,page13,page14,page15,page16,page17,location

# Inicializa el estado de sesión para el botón "Inicio" si no existe
if 'inicio_clicked' not in st.session_state:
    st.session_state.inicio_clicked = True
bar_options = st.sidebar.header("Menú de navegación", divider="rainbow")

# Define los botones fuera del bucle con claves únicas
inicio_button = st.sidebar.button("🏠 Inicio", key='button_0')
sobre_cetaceos_button = st.sidebar.button("ℹ Sobre los cetáceos", key='button_1')
location_button= st.sidebar.button("🗺️ Lugares donde se han observado en Cuba", key="button_19")
st.sidebar.header("Especies")
boreal_button = st.sidebar.button("🐋 Ballena boreal", key='button_2')
rorcual_button = st.sidebar.button("🐋 Rorcual Común", key='button_3')
yubarta_button = st.sidebar.button("🐋 Ballena jorobada", key='button_4')
piloto_button = st.sidebar.button("🐋 Ballena piloto", key='button_5')
gray_button = st.sidebar.button("🐬 Calderón gris", key='button_6')
asesina_button = st.sidebar.button("🐬 Ballena asesina", key='button_7')
falsa_orca_button = st.sidebar.button("🐬 Falsa orca", key='button_8')
esteno_button = st.sidebar.button("🐬 Esteno", key='button_9')
tonina_button = st.sidebar.button("🐬 Tonina", key='button_10')
pantropical_button = st.sidebar.button("🐬 Delfín moteado pantropical", key='button_11')
Atlantico_button = st.sidebar.button("🐬Delfín moteado del Atlántico", key='button_12')
enano_button = st.sidebar.button("🐬 Cachalote enano", key='button_13')
pigmeo_button = st.sidebar.button("🐬 Cachalote pigmeo", key='button_14')
rotador_button = st.sidebar.button("🐬Delfín Rotador", key='button_15')
cachalote_button = st.sidebar.button("🐬 Ballena de esperma", key='button_16')
zifio_button = st.sidebar.button("🐬Zifio de Gervais", key='button_17')
cuvier_button = st.sidebar.button("🐬 Ballena de pico de Cuvier", key='button_18')

# Usa las variables de los botones en las condiciones
if st.session_state.inicio_clicked or inicio_button:
    Inicio.run_app()
    st.session_state.inicio_clicked = False # Resetea el estado para evitar ejecuciones múltiples

elif sobre_cetaceos_button:
    pass
elif boreal_button:
    page1.show_page()
elif rorcual_button:
    page2.show_page()
elif yubarta_button:
    page3.show_page()
elif piloto_button:
    page4.show_page()
elif gray_button:
    page5.show_page()
elif asesina_button:
    page6.show_page()
elif falsa_orca_button:
    page7.show_page()
elif esteno_button:
    page8.show_page()
elif tonina_button:
    page9.show_page()
elif pantropical_button:
    page10.show_page()
elif Atlantico_button:
    page11.show_page()
elif enano_button:
    page12.show_page()
elif pigmeo_button:
    page13.show_page()
elif rotador_button:
    page14.show_page()
elif  cachalote_button:
    page15.show_page()
elif  zifio_button:
    page16.show_page()
elif  cuvier_button:
    page17.show_page()
elif location_button:
    location.location()


elección = st.sidebar.radio('Selecciona una opción:',["🗺️ Lugares donde se han observado en Cuba",""])
if 'mapa_mostrado' not in st.session_state:
    st.session_state.mapa_mostrado = False

if elección and not st.session_state.mapa_mostrado:
    location.location()
    st.session_state.mapa_mostrado = True