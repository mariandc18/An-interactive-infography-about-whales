import streamlit as st

def show_page():
    col0,col1, col2, col3= st.columns([1,6,6,1])
    with col1:
        st.title("Cachalote enano")
        st.image("./photos/cachalote_enano.jpg")
        st.write("Nombre científico: Kogia sima")
        st.write("Ubicación: Se distribuye a lo largo de las zonas tropicales y templadas.")
        st.write("Suborden: Odontoceti")
        st.write("Familia: Kogiidae")
        st.write("Subfamilia: Kogiidae")
        st.write("Cantidad de varamientos: 3")
    
    with col2:
        for _ in range(5):
            st.write("    ")
        if st.button("Características físicas"):
            st.write("- Llegan a alcanzar una talla de 2.7 m")
            st.write("- Pesan 210 kg en edad adulta")
            st.write("- Presentan una aleta dorsal bien definida")
            st.write("- Poseen una marca blanca cóncava detrás del ojo que asemeja el operáculo de los peces")
            st.write("- La pigmentación de la piel es gris azulado")
        
        if st.button("Origen del nombre"):
           st.write("- El género Kogia es un nombre de etimología desconocida. Se cree que podría ser un tributo a un naturalista turco llamado Cogia Effendi, quien observó ballenas en el mar Mediterráneo en la primera parte del siglo XIX. El epíteto sima, proviene del latín y significa nariz chata, por la forma de la cabeza")
          
        if st.button("Reproducción"):
            st.write("- Nacen midiendo aproximadamente 1 metro")
            
        if st.button("Alimentación"):
            st.write("- Peces pequeños")
            st.write("- Crustáceos")
        
        if st.button("Migraciones"):
            st.write("- Suelen habitar aguas a lo largo de la plataforma continental")
            
        if st.button("Hábitat"):
            st.write("-Prefieren aguas calidads, incursionando en aguas más latitudinales durante el período caluroso")
        st.write("   ")
        st.write("   ")
        st.write("Aquí puede escuchar el sonido del Cachalote enano:")
        st.audio("./sounds/kima.mp3",start_time=0)
        
        
        with st.container(border=True):
            st.markdown("Curiosidades:")
            st.write(" Regurgitan periódicamente contenido estomacal no dirigido")
            st.write(" Es muy parecida al cachalote pigmeo")
    
