import streamlit as st

def page11():
    col0,col1, col2, col3= st.columns([1,6,6,1])
    with col0:
        for _ in range(20):
            st.write("   ")
        st.button("Back")
    with col1:
        st.title("Delfín moteado del Atlántico")
        st.image("./photos/moteado.jpg")
        st.write("Nombre científico: Stenella longirostris")
        st.write("Ubicación: Común en las aguas cubanas")
        st.write("Suborden: Odontoceti")
        st.write("Familia: Delphinidae")
        st.write("Subfamilia: Delphinidae")
        st.write("Cantidad de varamientos: 12")
    
    with col2:
        for _ in range(5):
            st.write("    ")
        if st.button("Características físicas"):
            st.write("- Pueden alcanzar hasta 2.26 m de longitud los machos y las hembras 2.29 m")
            st.write("- Llegan a alcanzar un peso entre los 90 kg y 140 kg")
            st.write("- Cuerpo robusto con aleta dorsal notablemente curvada")
            st.write("- Su dorso se cubre de manchas según se va desarrollando")
        
        if st.button("Origen del nombre"):
           st.write("-  Su nombre se debe a las manchas que posee por todo el cuerpo y a su localizacón ")
          
        if st.button("Reproducción"):
            st.write("- Gestación entre 10 y 12 meses")
            st.write("- Las crías nacen con una longitud corporal de 0.90 y 1.10 m")
            
        if st.button("Alimentación"):
            st.write("- Peces ")
            st.write("- Cefalópodos ")
        
        if st.button("Migraciones"):
            st.write("- No migratorio")
            
        if st.button("Hábitat"):
            st.write("-Aguas templadas y tropicales del Atlántico")
        st.write("   ")
        st.write("   ")
        st.write("Aquí puede escuchar el sonido del Delfín moteado del Atlántico:")
        st.audio("./sounds/Moteado.mp3",start_time=0)
        
        
        with st.container(border=True):
            st.markdown("Curiosidades:")
            st.write(" Las crías son confundidas con las del delfín tonina")
            st.write(" Es de los más activos que se encuentran en nuestras aguas")
    
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
        