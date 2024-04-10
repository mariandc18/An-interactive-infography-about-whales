import streamlit as st

def run_app(): 
    st.title("Maravillas Acuáticas: Cetáceos en las aguas cubanas")
    st.image("./photos/delfin.jpg")
    st.header("Conoce sobre las especies de cetáceos que han sido avistadas en Cuba y sus varamientos")
    st.header("¿Cómo navegar por la app?", divider="blue")
    st.write("En la parte izquierda de la aplicación aparece un menú que contiene los principales contenidos que se abordan en la infografía. Haga click sobre el tema que desee conocer y sumérjase en el fascinante mundo de las ballenas y los delfines")
    
    st.header("Autores de la infografía",divider="blue")
    st.write("- Marian Aguilar Tavier")
    st.write("- Jennifer de la Caridad Sánchez Santana")
    st.write("Ambas estudiantes de 2do año de Data Science en la Universidad de La Habana")

    

