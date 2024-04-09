import streamlit as st
import importlib, Inicio

# Inicializa el estado de sesión para el botón "Inicio" si no existe
if 'inicio_clicked' not in st.session_state:
    st.session_state.inicio_clicked = True

options = ["🏠 Inicio", "ℹ Sobre los cetáceos", "🐋 Especies"]
bar_options = st.sidebar.header("Menú de navegación", divider="rainbow")

# Define los botones fuera del bucle con claves únicas
inicio_button = st.sidebar.button("🏠 Inicio", key='button_0')
sobre_cetaceos_button = st.sidebar.button("ℹ Sobre los cetáceos", key='button_1')
especies_button = st.sidebar.button("🐋 Especies", key='button_2')

# Usa las variables de los botones en las condiciones
if st.session_state.inicio_clicked or inicio_button:
    Inicio.run_app()
    st.session_state.inicio_clicked = False # Resetea el estado para evitar ejecuciones múltiples
elif sobre_cetaceos_button:
    pass
elif especies_button:
    pages = ["page1", "page2", "page3", "page4", "page5", "page6", "page7", "page8", "page9", "page10", "page11", "page12", "page13", "page14", "page15", "page16", "page17"]
    current_page_index = st.session_state.get('current_page_index', 0)

    # Determinar la página actual y mostrar su contenido
    current_page = pages[current_page_index]
    selected_module = importlib.import_module(current_page)
    selected_module.show_page() 
    # Botones de navegación con claves únicas
    if st.button('← Anterior', key=f'back_button_{current_page}'):
        current_page_index -= 1
    st.session_state['current_page_index'] = current_page_index
    if st.button('Siguiente →', key=f'next_button_{current_page}'):
        current_page_index += 1
    st.session_state['current_page_index'] = current_page_index
                                           