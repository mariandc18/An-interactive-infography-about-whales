import streamlit as st

def page2():
    col0,col1, col2, col3= st.columns([1,6,6,1])
    with col0:
        for _ in range(20):
            st.write("   ")
        st.button("Back")
    with col1:
        st.title("Rorcual común, rorcual franco")
        st.image("./photos/rorcual_comun.jpg")
        st.write("Nombre científico: Balaenoptera physalus")
        st.write("Ubicación: Menos frecuente en los trópicos")
        st.write("Suborden: Mysticeti")
        st.write("Familia: Balaenopteridae")
        st.write("Subfamilia: Balaenopterinae")
        st.write("Cantidad de varamientos: 1")
    
    with col2:
        for _ in range(5):
            st.write("    ")
        if st.button("Características físicas"):
            st.write("- En el norte alcanzan los 24 m de longitud y los del Sur pueden llegar a 27 m")
            st.write("- Pesan hasta 120 000 kg")
            st.write("- La coloración del vientre es blanca")
            st.write("- Pigmentación asimétrica de la mandíbula inferior")
            st.write("- Posee entre 50 y 100 pliegues ventrales")
        
        if st.button("Origen del nombre"):
           st.write("- Su nombre común se debe a que en el pasado era avistada con mucha frecuencia")
           st.write("- La palabra physalus hace referencia a la capacidad del animal de inflar su garganta")
          
        if st.button("Reproducción"):
            st.write("- Adquiere la madurez sexual entre los 8 y 12 años")
            st.write("- Gestación entre 11 y 12 meses")
            st.write("- Al nacer mide de 6 a 6,5 m de longitud")
            st.write("- El período de lactancia es de hasta las 7 meses")
            
        if st.button("Alimentación"):
            st.write("- Peces pequeños")
            st.write("- Calamares ")
            st.write("- Kril")
        
        if st.button("Migraciones"):
            st.write("- Se observan poblaciones que cambian de área según sea verano o invierno, mientras que otras se mantienen en el mismo lugar")
            
        if st.button("Hábitat"):
            st.write("-Aguas profundas")
            st.write("- Costas")
        st.write("   ")
        st.write("   ")
        st.write("Aquí puede escuchar el sonido del rorcual común:")
        st.audio("./sounds/rorcual_comun.mp3",start_time=0)
        
        
        with st.container(border=True):
            st.markdown("Curiosidades:")
            st.write(" Es considerado el segundo animal más grande de los mares")
            st.write(" Es una especie longeva que puede alcanzar los 80 años de vida")
            st.write(" Solo se suelen ver en parejas")
            st.write(" Está considerada como una especie amenazada")
    
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

        