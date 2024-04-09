import streamlit as st

def show_page():
    col0,col1, col2, col3= st.columns([1,6,6,1])
    with col1:
        st.title("Delfín de dientes estriados, esteno")
        st.image("./photos/esteno.jpg")
        st.write("Nombre científico: Steno bredanensis")
        st.write("Ubicación: Zonas tropicales y templadas de la mayoría de los océanos y mares")
        st.write("Suborden: Odontoceti")
        st.write("Familia: Delphinidae")
        st.write("Subfamilia: Delphininae")
        st.write("Cantidad de varamientos: 4")
    
    with col2:
        for _ in range(5):
            st.write("    ")
        if st.button("Características físicas"):
            st.write("- Llega a alcanzar los 160 kg")
            st.write("- Llegan a alcanzar una talla de hasta 2,65 m los machos y 2,55 m las hembras")
            st.write("- Apariencia física parecida a los reptiles, con ojos grandes y cabeza cónica")
            st.write("- Generalmente, presenta manchas pequeñas de forma circular a lo largo del cuerpo color amarillo-blanco, las cuales son las cicatrices causadas por la mordedura de tiburones")
        
        if st.button("Origen del nombre"):
           st.write("- Su nombre se debe a su peculiar esmalte dental, recubierto de estrías longitudinales")
          
        if st.button("Reproducción"):
            st.write("- Alcanza la madurez sexual a los 10 años las hembras y 14 años los machos")
            st.write("- La gestación es de 10 meses")
            st.write("- Las crías al nacer miden de 1 m")
            
        if st.button("Alimentación"):
            st.write("- Peces")
            st.write("- Cefalópodos")
        
        if st.button("Migraciones"):
            st.write("- Forman grupos de 10 a 50 individuos")
            
        if st.button("Hábitat"):
            st.write("- Se puede encontrar en el Mar Caribe y el Golfo de México")
        st.write("   ")
        st.write("   ")
        st.write("Aquí puede escuchar el sonido del esteno:")
        st.audio("./sounds/esteno.mp3",start_time=0)
        
        
        with st.container(border=True):
            st.markdown("Curiosidades:")
            st.write(" Puede surcar las olas de proa que generan los barcos, pero no es fácil que realice saltos completos")
            st.write(" La característica más notable de su comportamiento es que el grupo se mueve de forma compacta")
            st.write(" Pueden estar hasta 15 minutos sumergidos, por lo que es difícil su observación")
            st.write(" La longevidad es de 30 años")
            
    
        
