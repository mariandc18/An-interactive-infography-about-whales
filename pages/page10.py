import streamlit as st

def page10():
    col0,col1, col2, col3= st.columns([1,6,6,1])
    with col0:
        for _ in range(20):
            st.write("   ")
        st.button("Back")
    with col1:
        st.title("Delfín moteado pantropical")
        st.image("./photos/pantropical.jpg")
        st.write("Nombre científico: Stenella attenuata")
        st.write("Ubicación: Aguas tropicales y templadas de los océanos Atlántico, Pacífico e Índico")
        st.write("Suborden: Odontoceti")
        st.write("Familia: Delphinidae")
        st.write("Subfamilia: Delphinidae")
        st.write("Cantidad de varamientos: 3")
    
    with col2:
        for _ in range(5):
            st.write("    ")
        if st.button("Características físicas"):
            st.write("- Pueden alcanzar hasta 2.57 m de longitud los machos y las hembras 2.40 m")
            st.write("- Llegan a alcanzar un peso de 120 kg")
            st.write("- Cuerpo delgado pero fuerte")
            st.write("- Hocico largo y pronunciado")
            st.write("- Presentan una banda oscura desde las aletas hasta los pectorales")
            st.write("- Coloración de la región dorsal y las aletas pectorales es gris oscura")
        
        if st.button("Origen del nombre"):
           st.write("-  El nombre común para esta especie se debe a su rango de distribución ")
          
        if st.button("Reproducción"):
            st.write("- Las crías al nacer llegan a medir 0.85 m")
            
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
        st.write("Aquí puede escuchar el sonido del Delfín moteado del pantropical:")
        st.audio("./sounds/....mp3",start_time=0)
        
        
        with st.container(border=True):
            st.markdown("Curiosidades:")
            st.write(" Antiguamente esta especie y el Delfín moteado del Atlántico eran considerados la misma")
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
        