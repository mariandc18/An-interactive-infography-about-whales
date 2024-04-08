import streamlit as st

def page6():
    col0,col1, col2, col3= st.columns([1,6,6,1])
    with col0:
        for _ in range(20):
            st.write("   ")
        st.button("Back")
    with col1:
        st.title("Orca, ballena asesina")
        st.image("./photos/asesina.jpg")
        st.write("Nombre científico: Orcinus orca")
        st.write("Ubicación: Cosmopolita")
        st.write("Suborden: Odontoceti")
        st.write("Familia: Delphinidae")
        st.write("Subfamilia: Delphininae")
        st.write("Cantidad de varamientos: 1")
    
    with col2:
        for _ in range(5):
            st.write("    ")
        if st.button("Características físicas"):
            st.write("- A pesar de su denominación como ballena, esta especie pertenece a la familia de los delfines")
            st.write("- Llegan a alcanzar una talla de hasta 9 m los machos y 7,9 m las hembras")
            st.write("- Los machos pueden alcanzar los 5600 kg y las hembras los 3800 kg")
            st.write("- Su pigmentación es básicamente blanca y negra, con una pequeña marca más clara detrás de la aleta dorsal, llamada montura")
            st.write("- Cabeza redonda y carente del hocico")
        
        if st.button("Origen del nombre"):
           st.write("- El término orca fue dado por los antiguos romanos. El término orc o su variante ork, significa pez grande, ballena o monstruo marino")
          
        if st.button("Reproducción"):
            st.write("- Adquieren la madurez sexual entre los 6 y 10 años las hembras y entre los 12 y 16 años en los machos")
            st.write("- Gestación entre los 12 y 16 meses aproximadamente")
            st.write("- Las crías al nacer miden de 2 a 2,6 m")
            st.write("- La duración de la lactancia es desconocida")
            
        if st.button("Alimentación"):
            st.write("- Cuenta con una de las dietas más variadas dentro de los cetáceos que incluye tortugas, focas, peces y ballenas")
        
        if st.button("Migraciones"):
            st.write("- Existen dos tipos de poblaciones: las residentes y las transeúntes. Estas últimas sueles desplazarse de un área geográfica a otra sin realizar períodos de estadía prolongados")
            
        if st.button("Hábitat"):
            st.write("- Se adaptan muy bien al cautiverio")
        st.write("   ")
        st.write("   ")
        st.write("Aquí puede escuchar el sonido de la ballena asesina:")
        st.audio("./sounds/asesina.mp3",start_time=0)
        
        
        with st.container(border=True):
            st.markdown("Curiosidades:")
            st.write(" Es considerada la especie de mayor tamaño entre los delfines")
            st.write(" Su nombre refleja el carácter depredador de la especie y se remonta a épocas antiguas")
            st.write("También se conoce como lobo de mar")
            st.write("La longevidad se estima de 50 a 60 años los machos y 80 a 90 años las hembras")
            st.write(" Son animales muy activos")
            st.write(" En cautiverio se han registrado más ataques a personas que en vida libre, posiblemente por el estrés al que están sometidos al vivir en un espacio reducido")
    
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
        
