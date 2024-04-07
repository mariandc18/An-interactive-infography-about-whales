import streamlit as st

def page12():
    col0,col1, col2, col3= st.columns([1,6,6,1])
    with col0:
        for _ in range(20):
            st.write("   ")
        st.button("Back")
    with col1:
        st.title("Tonina, delfín mular, delfín nariz de botella")
        st.image("./photos/tonina.jpg")
        st.write("Nombre científico: Tursiops truncatus")
        st.write("Ubicación: Aguas tropicales y templadas de todo el mundo, y en todos los océanos excepto Ártico y el Antártico")
        st.write("Suborden: Odontoceti")
        st.write("Familia: Delphinidae")
        st.write("Subfamilia: Delphinidae")
        st.write("Cantidad de varamientos: 3")
    
    with col2:
        for _ in range(5):
            st.write("    ")
        if st.button("Características físicas"):
            st.write("- Las tallas están entre 2.45 m y 3.80 m los machos y las hembras entre 2.40 m y 3.70 m")
            st.write("- Los machos llegan a pesar 500 kg y las hembras 260 kg")
            st.write("- Contextura larga y robusta")
            st.write("- Aleta dorsal falcada y bien definida")
            st.write("- Generalmente son azules grisaseos")
        
        if st.button("Origen del nombre"):
           st.write("-  Tursiops significa animal marino parecido al delfín.El nombre en ingles es nariz de botella  ")
          
        if st.button("Reproducción"):
            st.write("- Alcanza la madurez sexual a los 10 años las hembras y 13 los machos")
            st.write("- Gestacón de 12 meses")
            st.write("- Las crías al nacer medin entre 0.8 m y 1.40 m")
            st.write("- Gestacón de 12 meses")
            
            
        if st.button("Alimentación"):
            st.write("- Peces voladores ")
            st.write("- Caballas ")
            st.write("- Calamares ")
        
        if st.button("Migraciones"):
            st.write("- Las migraciones del delfín moteado pantropical son un fenómeno fascinante que se observa principalmente en la costa este de Australia, donde los delfines se desplazan en grandes grupos desde sus áreas de reproducción en el norte hasta las áreas de alimentación en el sur")
            
        if st.button("Hábitat"):
            st.write("- Aguas tropicales y templadas")
        st.write("   ")
        st.write("   ")
        st.write("Aquí puede escuchar el sonido del Delfín moteado del Atlántico:")
        st.audio("./sounds/nariz.mp3",start_time=0)
        
        
        with st.container(border=True):
            st.markdown("Curiosidades:")
            st.write(" Es una especie residente en Cuba")
            st.write(" El tamaño, la pigmentación y las características particulares dependen de la ubicación geográfica")
            st.write(" La longevidad se estima entre 50 y 60 años")
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
        