import streamlit as st

def show_page():
    col0,col1, col2, col3= st.columns([1,6,6,1])
    
    with col1:
        st.title("Ballena de pico de Cuvier")
        st.image("./photos/ziphio_cuvier.jpg")
        st.write("Nombre científico: Ziphis cavirostris")
        st.write("Ubicación: En todos los océanos excepto en las aguas polares del Ártico y de la Antártica")
        st.write("Suborden: Odontoceti ")
        st.write("Familia: Ziphiidae")
        st.write("Subfamilia: Ziphiidae")
        st.write("Cantidad de varamientos: 32")
    
    with col2:
        for _ in range(5):
            st.write("    ")
        if st.button("Características físicas"):
            st.write("- La talla de los adultos es aproximadamente 7 m")
            st.write("- El peso oscila entre 2600 kg y 3000 kg")
            st.write("- Cuerpo robusto y fusiforme")
            st.write("- Poseen una mandíbula prominente")
            st.write("- Presentan una característica depresión al inicio del espiraculo")
        if st.button("Origen del nombre"):
           st.write("- El nombre de la especie procede del término latino cavus, que significa cóncavo, aludiendo a la concavidad que presenta en el cráneo exclusiva de los machos")
          
        if st.button("Reproducción"):
            st.write("- No muestran una época clara de reproducción")
            st.write("- Las crías al nacer pueden llegar a medir 2.7 m")
            st.write("- El peso de los neonatos está establecido entre los 250 kg y los 300 kg ")
            
        if st.button("Alimentación"):
            st.write("- Cefalópodos")
            st.write("- Crustácios ")
            st.write("- Peces mesopelágicos")
        
        if st.button("Migraciones"):
            st.write("- Estas especies muestran una fidelidad territorial en algunas zonas ")
            st.write("- Se han registrado desplazamientos de largas distancias de zifios de Cuvier ")
            
        if st.button("Hábitat"):
            st.write("-Aguas profundas cálidas y templadas")
        st.write("   ")
        st.write("   ")
        st.write("Aquí puede escuchar el sonido de la ballena de pico de Cuvier:")
        st.audio("./sounds/zifio_de_cuvier.mp3",start_time=0)
        
        
        with st.container(border=True):
            st.markdown("Curiosidades:")
            st.write(" Todos los individuos tienen cicatrices ondulantes dobles provocadas por los dientes de otros individuos")
            st.write(" El zifio de Cuvier es el mamífero que mayor profundidad y tiempo puede estar sumergido")
    
    