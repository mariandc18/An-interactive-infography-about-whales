import streamlit as st

def page13():
    col0,col1, col2, col3= st.columns([1,6,6,1])
    with col0:
        for _ in range(20):
            st.write("   ")
        st.button("Back")
    with col1:
        st.title("Cachalote pigmeo")
        st.image("./photos/pigmeo.jpg")
        st.write("Nombre científico: Kogia breviceps")
        st.write("Ubicación: Se encuentre extensamente distribuido a lo largo de las zonas tropicales y templadas")
        st.write("Suborden: Odontoceti")
        st.write("Familia: Kogiidae")
        st.write("Subfamilia: Kogiidae")
        st.write("Cantidad de varamientos: 5")
    
    with col2:
        for _ in range(5):
            st.write("    ")
        if st.button("Características físicas"):
            st.write("- Alcanza una talla de 3.5 m")
            st.write("- Pesan 410 kg en edad adulta")
            st.write("- Especie parecida al gran cachalote con la cabeza  uadrada en adultos")
            st.write("- Presentan una aleta dorsal definida")
            st.write("- Poseen una marca blanca cóncava detrás del ojo que asemeja el operáculo de los peces")
            st.write("- La pigmentación de la piel es gris azulado")
        
        if st.button("Origen del nombre"):
           st.write("- La palabra latina breviceps significa cabeza cortaEl género Kogia es un nombre de etimología desconocida. Se cree que podría ser un tributo a un naturalista turco llamado Cogia Effendi, quien observó ballenas en el mar Mediterráneo en la primera parte del siglo XIX. El epíteto sima, proviene del latín y significa nariz chata, por la forma de la cabeza")
          
        if st.button("Reproducción"):
            st.write("- Se conoce poco del ciclo reproductivo")
            st.write("- Se estima que el período de gestacón es de 9 meses")
            st.write("- Se concidera que las crías nacen en primavera")

        if st.button("Alimentación"):
            st.write("- Peces pequeños")
            st.write("- Crustáceos")
            st.write("- Calamares")
        
        if st.button("Migraciones"):
            st.write("- Incursionan en aguas latitudinales durante el período de verano, donde ocasionalmete ingresa a aguas más cercanas a la costa")
            
        if st.button("Hábitat"):
            st.write("-Prefieren aguas calidas, incursionando en aguas más latitudinales durante el período caluroso")
        st.write("   ")
        st.write("   ")
        st.write("Aquí puede escuchar el sonido del Cachalote pigmeo:")
        st.audio("./sounds/pigmeo.mp3",start_time=0)
        
        
        with st.container(border=True):
            st.markdown("Curiosidades:")
            st.write(" Sale a respirar rápidamente y desaparece")
            st.write(" Regurgitan periódicamente contenido estomacal no dirigido")
            st.write(" Es un animal de nado lento")
            st.write(" La longevidad en la naturaleza es de 17 años")
    
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
