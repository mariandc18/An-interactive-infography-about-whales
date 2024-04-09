import streamlit as st

def show_page():
    col0,col1, col2, col3= st.columns([1,6,6,1])
    
    with col1:
        st.title("Zifio de Gervais")
        st.image("./photos/zifio_de_gervais.jpg")
        st.write("Nombre científico: Mesoplodon euroopaeus")
        st.write("Ubicación: Amplia distribución en aguas templadas del Atlántico norte ")
        st.write("Suborden: Odontoceti ")
        st.write("Familia: Ziphiidae")
        st.write("Subfamilia: Ziphiidae")
        st.write("Cantidad de varamientos: 12")
    
    with col2:
        for _ in range(5):
            st.write("    ")
        if st.button("Características físicas"):
            st.write("- Los machos miden 4.5 m y las hembras 5.2")
            st.write("- El peso supera los 1200 kg")
            st.write("- El cuerpo da la impresión de estar comprimido")
            st.write("- La cabeza es proporcionalmente pequeña y redonda")
        if st.button("Origen del nombre"):
           st.write("- La etimología del término zifio proviene del griego xiphos (espada), refiriéndose a la nariz pronunciada de estos animales, que les da una apariencia similar a una espada")
          
        if st.button("Reproducción"):
            st.write("- Las crías recien nacidas miden 2.5 m de longitud")

        if st.button("Alimentación"):
            st.write("- Calamares")
            st.write("- Peces pequeños")
            st.write("- Gambas")
        
        if st.button("Migraciones"):
            st.write("- No es una especie migratoria ")
            
        if st.button("Hábitat"):
            st.write("-Aguas profundas")
        st.write("   ")
        st.write("   ")
        st.write("Aquí puede escuchar el sonido de la ballena Zifio de Gervais:")
        st.audio("./sounds/gervais.mp3",start_time=0)
        
        
        with st.container(border=True):
            st.markdown("Curiosidades:")
            st.write(" No se conocian especímenes vivos hasta 1998")
            st.write(" No existen datos sobre la población de la especie, o su estado de conservación")
    
    