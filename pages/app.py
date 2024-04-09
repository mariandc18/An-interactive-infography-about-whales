import streamlit as st
import importlib, Inicio, page1,page2,page3,page4,page5,page6,page7,page8,page9,page10,page11,page12,page13,page14,page15,page16,page17,location

# Inicializa el estado de sesión para el botón "Inicio" si no existe
if 'inicio_clicked' not in st.session_state:
    st.session_state.inicio_clicked = True
bar_options = st.sidebar.header("Menú de navegación", divider="rainbow")

# Define los botones fuera del bucle con claves únicas
inicio_button = st.sidebar.button("🏠 Inicio", key='button_0')
sobre_cetaceos_button = st.sidebar.button("ℹ Sobre los cetáceos", key='button_1')
st.sidebar.header("Especies")
opcions= ["🐋 Ballena boreal","🐋 Rorcual Común","🐋 Ballena jorobada","🐋 Ballena piloto","🐬 Calderón gris","🐬 Ballena asesina","🐬 Falsa orca","🐬 Esteno", "🐬 Tonina","🐬 Delfín moteado pantropical","🐬Delfín moteado del Atlántico","🐬 Cachalote enano","🐬 Cachalote pigmeo","🐬Delfín Rotador","🐬 Ballena de esperma","🐬Zifio de Gervais","🐬 Ballena de pico de Cuvier","🗺️ Lugares donde se han observado en Cuba"]
elección = st.sidebar.radio('Selecciona una opción:',opcions)

# Usa las variables de los botones en las condiciones
if st.session_state.inicio_clicked or inicio_button:
    Inicio.run_app()
    st.session_state.inicio_clicked = False # Resetea el estado para evitar ejecuciones múltiples

elif sobre_cetaceos_button:
    pass
elif elección =="🐋 Ballena boreal" :
    page1.show_page()
elif elección =="🐋 Rorcual Común":
    page2.show_page()
elif elección == "🐋 Ballena jorobada":
    page3.show_page()
elif elección =="🐋 Ballena piloto":
    page4.show_page()
elif elección == "🐬 Calderón gris":
    page5.show_page()
elif elección == "🐬 Ballena asesina":
    page6.show_page()
elif elección == "🐬 Falsa orca":
    page7.show_page()
elif elección == "🐬 Esteno":
    page8.show_page()
elif elección == "🐬 Tonina":
    page9.show_page()
elif elección == "🐬 Delfín moteado pantropical":
    page10.show_page()
elif elección == "🐬Delfín moteado del Atlántico":
    page11.show_page()
elif elección == "🐬 Cachalote enano":
    page12.show_page()
elif elección == "🐬 Cachalote pigmeo":
    page13.show_page()
elif elección == "🐬Delfín Rotador":
    page14.show_page()
elif elección ==  "🐬 Ballena de esperma":
    page15.show_page()
elif elección ==  "🐬Zifio de Gervais":
    page16.show_page()
elif elección ==  "🐬 Ballena de pico de Cuvier":
    page17.show_page()
elif elección == "🗺️ Lugares donde se han observado en Cuba":
    location.location()


