import streamlit as st

def page1():
    col0,col1, col2, col3= st.columns([1,6,6,1])
    with col0:
        for _ in range(20):
            st.write("   ")
        st.button("Back")
    with col1:
        st.title("Cachalote, ballena de esperma")
        st.image("./photos/ballena_de_esperma.jpg")
        st.write("Nombre científico: Physeter macrocephalus")
        st.write("Ubicación: Pueden encontrarse desde las regiones polares hasta el ecuador")
        st.write("Suborden: Odontoceti ")
        st.write("Familia: Physeteridae")
        st.write("Subfamilia: Ziphiidae")
        st.write("Cantidad de varamientos: Más de 15")
    
    with col2:
        for _ in range(5):
            st.write("    ")
        if st.button("Características físicas"):
            st.write("- Es el odontoceto de mayor tamaño")
            st.write("- Los machos poseen una talla de 18.3 m y las hembras 11 m")
            st.write("- Los machos llegan a alcanzar un peso de 57000 kg y las hembras 24000kg")
            st.write("- La piel es rugosa y la coloración gris oscuro")
            st.write("- El tamaño de la cabeza ocupa una tercera parte del cuerpo")
        if st.button("Origen del nombre"):
           st.write("- Su nombre viene del latín Physeter, soplador y macrochephalus, cabeza grande")
          
        if st.button("Reproducción"):
            st.write("- Alcanzan la madurez sexual de 7 a 12 años las hembras y de 18 a 21 los machos")
            st.write("- El período de gestación es de 16 meses")
            st.write("- Las crías recien nacidas miden 4 m")

        if st.button("Alimentación"):
            st.write("- Calamares gigantes")
        
        if st.button("Migraciones"):
            st.write("- Existen diferencias marcadas entre los patrones migratorios de las hembras y los machos adultos")

        if st.button("Hábitat"):
            st.write("-Aguas oceánicas y en lugares cercanos a las costas")
        st.write("   ")
        st.write("   ")
        st.write("Aquí puede escuchar el sonido de la ballena de esperma:")
        st.audio("./sounds/Cachalote.mp3",start_time=0)
        
        
        with st.container(border=True):
            st.markdown("Curiosidades:")
            st.write(" Tiene una longevidad de 60 a 70 años")
            st.write(" Acusticamente se caracterizan por la emisón de pulsos de sonido denominados codas")
            st.write(" Está contemplada como una especie vulnerable a la extinción")
    with col3:
        st.write("   ")
        st.write("   ")
        st.write("   ")
        st.write("   ")
        st.write("   ")
        st.write("   ")
        st.write("   ")
        st.write("   ")
        st.write("   ")
        st.write("   ")
        st.write("   ")
        st.write("   ")
        st.write("   ")
        st.write("   ")
        st.write("   ")
        st.write("   ")
        st.write("   ")
        st.write("   ")
        st.write("   ")
        st.write("   ")
        st.write("   ")
        st.button("Next")