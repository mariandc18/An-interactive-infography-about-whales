import streamlit as st

def page5():
    col0,col1, col2, col3= st.columns([1,6,6,1])
    with col0:
        for _ in range(20):
            st.write("   ")
        st.button("Back")
    with col1:
        st.title("Delfín de Risso, calderón gris")
        st.image("./photos/risso.jpg")
        st.write("Nombre científico: Grampus griseus")
        st.write("Ubicación: Zonas tropicales y templadas de la mayoría de los océanos y mares del mundo")
        st.write("Suborden: Odontoceti")
        st.write("Familia: Delphinidae")
        st.write("Subfamilia: Delphininae")
        st.write("Cantidad de varamientos: 7")
    
    with col2:
        for _ in range(5):
            st.write("    ")
        if st.button("Características físicas"):
            st.write("- Los adultos llegan a pesar entre 300 y 600 kg")
            st.write("- Llegan a alcanzar una talla de hasta 3,83 los machos y 3,66 las hembras")
            st.write("- Los adultos presentan manchas grisáceas a lo largo de toda la superficie corporal")
            st.write("- Su cuerpo tiende a ser robusto")
        
        if st.button("Origen del nombre"):
           st.write("- Su nombre científico proviene de los términos latinos globicephala que significa cabeza de globo y macrorynchus,pico grande.")
          
        if st.button("Reproducción"):
            st.write("- Adquieren la madurez sexual a partir de una talla aproximada de 2,60m")
            st.write("- Gestación de hasta 12 meses aproximadamente")
            st.write("- Las crías al nacer miden de 1 a 1,5 m")
            st.write("- La duración de la lactancia es desconocida")
            
        if st.button("Alimentación"):
            st.write("- Calamares y pulpos, aunque ocasionalmente pueden consumir peces")
        
        if st.button("Migraciones"):
            st.write("- Su distribución se ve afectada por fenómenos naturales como El Niño, el cual provoca, en ocasiones, el desplazamiento de especies, y en otros casos la concentración de ejemplares.")
            
        if st.button("Hábitat"):
            st.write("- Prefieren las aguas profundas aunque pueden aparecer cerca de la costa")
        st.write("   ")
        st.write("   ")
        st.write("Aquí puede escuchar el sonido del calderón gris:")
        st.audio("./sounds/risso.mp3",start_time=0)
        
        
        with st.container(border=True):
            st.markdown("Curiosidades:")
            st.write(" Suelen vivir hasta los 30 años")
            st.write(" Se les suele observar espiando a su alrededor, sacando la cabeza e incluso el cuerpo fuera del agua, el cual exponen en posición vertical")
    
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

