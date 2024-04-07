import streamlit as st

def page4():
    col0,col1, col2, col3= st.columns([1,6,6,1])
    with col0:
        for _ in range(20):
            st.write("   ")
        st.button("Back")
    with col1:
        st.title("Calderón de aleta corta, ballena piloto")
        st.image("./photos/pilot_whale.jpg")
        st.write("Nombre científico: Globicephala macrorhynchus")
        st.write("Ubicación: A lo largo de todo el trópico")
        st.write("Suborden: Odontoceti")
        st.write("Familia: Delphinidae")
        st.write("Subfamilia: Delphininae")
        st.write("Cantidad de varamientos: 9")
    
    with col2:
        for _ in range(5):
            st.write("    ")
        if st.button("Características físicas"):
            st.write("- Los machos miden de 5,3 m a 7,2 m y las hembras de 4,1 a 5,5 m.")
            st.write("- Cabeza con forma abombada, por la protuberancia que se extiende por encima de la boca")
            st.write("- Se distingue del calderón común por sus aletas pectorales")
            st.write("- El color del cuerpo es básicamente pardo oscuro o negro")
        
        if st.button("Origen del nombre"):
           st.write("- Su nombre científico proviene de los términos latinos globicephala que significa cabeza de globo y macrorynchus,pico grande.")
          
        if st.button("Reproducción"):
            st.write("- Las hembras adqueren  la madurez sexual a los 6 años y los machos, a los 11")
            st.write("- Gestación de hasta 15 meses")
            st.write("- Las crías pueden alcanzar los 1,4 y 1,85 m de longitud")
            st.write("- El ciclo reproductivo dura aproximadamente 3 años")
            
        if st.button("Alimentación"):
            st.write("- Se alimentan habitualmente del calamar")
        
        if st.button("Migraciones"):
            st.write("- Se han documentado cambios en su distribución, principalmente en el norte del Golfo de México y hacia el sur de California")
            
        if st.button("Hábitat"):
            st.write("- Aguas cálidas del mundo")
        st.write("   ")
        st.write("   ")
        st.write("Aquí puede escuchar el sonido de la ballena piloto:")
        st.audio("./sounds/piloto.mp3",start_time=0)
        
        
        with st.container(border=True):
            st.markdown("Curiosidades:")
            st.write(" La longevidad de esta especie oscila entre 40 y 65 años")
            st.write(" Es una especie muy social con fuertes vínculos familiares")
    
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

