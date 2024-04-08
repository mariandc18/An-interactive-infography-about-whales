import streamlit as st

def page7():
    col0,col1, col2, col3= st.columns([1,6,6,1])
    with col0:
        for _ in range(20):
            st.write("   ")
        st.button("Back")
    with col1:
        st.title("Falsa Orca")
        st.image("./photos/falsa_orca.jpg")
        st.write("Nombre científico: Pseudorca crassidnes")
        st.write("Ubicación: Zonas tropicales y templadas de la mayoría de los océanos y mares")
        st.write("Suborden: Odontoceti")
        st.write("Familia: Delphinidae")
        st.write("Subfamilia: Delphininae")
        st.write("Cantidad de varamientos: 5")
    
    with col2:
        for _ in range(5):
            st.write("    ")
        if st.button("Características físicas"):
            st.write("- Llega a alcanzar los 1360 kg")
            st.write("- Llegan a alcanzar una talla de hasta 6 m los machos y 5 m las hembras")
            st.write("- La cabeza, totalmente negra, es larga y fina, se adelgaza hasta acabar en un rostrum redondeado")
            st.write("- Cuerpo esbelto")
        
        if st.button("Origen del nombre"):
           st.write("- Pseudorca significa parecido a la orca, y crassidens, de dientes grandes")
          
        if st.button("Reproducción"):
            st.write("- Las crías al nacer miden de 1,6 a 1,9 m")
            st.write("- La duración de la lactancia es de 12 hasta 18 meses")
            
        if st.button("Alimentación"):
            st.write("- Peces grandes como atunes")
            st.write("- Calamar")
            st.write("- Cetáceos pequeños")
        
        if st.button("Migraciones"):
            st.write("- Viajan en grupos de 10-15 individuos")
            st.write("- Se adapta bien al cautiverio")
            
        if st.button("Hábitat"):
            st.write("- Se puede encontrar en el Mar Caribe y el Golfo de México")
        st.write("   ")
        st.write("   ")
        st.write("Aquí puede escuchar el sonido de la falsa orca:")
        st.audio("./sounds/falsa_orca.mp3",start_time=0)
        
        
        with st.container(border=True):
            st.markdown("Curiosidades:")
            st.write(" Son rápidas y acrobáticas")
            st.write(" Es famosa por sus varamientos en masa")
            st.write(" Cuando salen a la superficie suelen sacar totalmente la cabeza y buena parte del cuerpo.")
            st.write("La longevidad se estima de 58 años los machos y 63 años las hembras")
            
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
        