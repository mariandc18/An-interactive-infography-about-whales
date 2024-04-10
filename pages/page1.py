import streamlit as st

def show_page():
    col0,col1, col2, col3= st.columns([1,6,6,1])
    with col1:
        st.title("Ballena Sei o boreal")
        st.image("./photos/image1.jpg")
        st.write("Nombre científico: Balaenoptera borealis")
        st.write("Ubicación: Desde los 60 grados al Sur a 60 Norte")
        st.write("Suborden: Mysticeti")
        st.write("Familia: Balaenopteridae")
        st.write("Subfamilia: Balaenopterinae")
        st.write("Cantidad de varamientos: 2")
    
    with col2:
        for _ in range(5):
            st.write("    ")
        if st.button("Características físicas"):
            st.write("- Pueden alcanzar hasta 19.5 m de longitud")
            st.write("- Pesan hasta 45 000 kg")
            st.write("- Cuerpo relativamente delgado")
            st.write("- Posee entre 30 y 60 pliegues ventrales")
        
        if st.button("Origen del nombre"):
           st.write("- La palabra Sei es de origen noruego y significa bacalao, porque habitualmente esta ballena ha sido observada junto a manchas de bacalao")
          
        if st.button("Reproducción"):
            st.write("- Gestación entre 11 y 12 meses")
            st.write("- Las crías normalmente nacen en invierno")
            st.write("- Dan a luz en intervalos de 2 a 3 años")
            
        if st.button("Alimentación"):
            st.write("- Peces pequeños")
            st.write("- Calamares ")
            st.write("- Planton")
        
        if st.button("Migraciones"):
            st.write("- No frecuenta los mismos sitios anno tras año.")
            st.write("- En invierno migran desde las frías aguas subpolares a las aguas tropicales")
            st.write("- Se mueve en solitario o en grupos pequennos")
            
        if st.button("Hábitat"):
            st.write("-Aguas profundas")
        st.write("   ")
        st.write("   ")
        st.write("Aquí puede escuchar el sonido de la ballena boreal:")
        st.audio("./sounds/boreal.mp3",start_time=0)
        
        
        with st.container(border=True):
            st.markdown("Curiosidades:")
            st.write(" El soplido dura de 40 a 60 segundos, seguido por una profunda zambullida de entre 5 a 15 minutos.")
            st.write(" Es uno de los cetáceos más rápidos alcanzando hasta los 47 km/h")
    
    
        