import streamlit as st

def show_page():
    col0,col1, col2, col3= st.columns([1,6,6,1])

    with col1:
        st.title("Ballena jorobada, yubarta")
        st.image("./photos/jorobada.jpg")
        st.write("Nombre científico: Megaptera novaeangliae")
        st.write("Ubicación: Entre los 80 grados LN y 80 grados LS")
        st.write("Suborden: Mysticeti")
        st.write("Familia: Balaenopteridae")
        st.write("Subfamilia: Megapterinae")
        st.write("Cantidad de varamientos: 3")
    
    with col2:
        for _ in range(5):
            st.write("    ")
        if st.button("Características físicas"):
            st.write("- Miden desde 16  m a 17 m, siendo las hembra más grandes que los machos.")
            st.write("- Pesan hasta 40 000 kg durante su vida adulta")
            st.write("- Cuerpo robusto y aletas pectorales de hasta 5 m de largo")
            st.write("- Hacia el vientre del animal se destacan entre 14 y 22 pliegues que van desde la mandíbula hasta el área umbilical")
        
        if st.button("Origen del nombre"):
           st.write("- Su nombre común, yubarta, proviene probablemente de la alteración del antiguo nombre francés jubartes, que procede de la palabra inglesa gibbard o de la latina gibbus, que significa joroba.")
          
        if st.button("Reproducción"):
            st.write("- Adquiere la madurez sexual entre los 4 y 7 años de vida")
            st.write("- Gestación de hasta 12 meses")
            st.write("- Los machos compiten agresivamente entre ellos por las hembras, exhibiendo conductas acrobáticas")
            st.write("- El período de lactancia es de hasta las 5 meses")
            
        if st.button("Alimentación"):
            st.write("- Varían su método de alimentación según la estación del año")
            st.write("- Peces pequeños")
            st.write("- Krill")
        
        if st.button("Migraciones"):
            st.write("- En verano se concentran en áreas de alimentación ubicadaa hacia latitudes frías y templadas, mientras que en el invierno migran a aguas tropicales")
            
        if st.button("Hábitat"):
            st.write("-Se suelen distinguir poblaciones en función de su localización, siendo las tres más importantes las presentes en el Atlántico norte, las del hemisferio sur y las del Pacífico norte. No es común que las poblaciones de diferentes lugares interaccionen entre ellas")
        st.write("   ")
        st.write("   ")
        st.write("Aquí puede escuchar el sonido de la ballena jorobada:")
        st.audio("./sounds/jorobada.m4a",start_time=0)
        
        
        with st.container(border=True):
            st.markdown("Curiosidades:")
            st.write(" Son confiados y curiosos por lo que no rehúyen la presencia de barcos")
            st.write(" Esta especie puede alcanzar los 80 años de vida")
            st.write(" Es una de las especies más frecuentes en los mares cubanos")
    
    
