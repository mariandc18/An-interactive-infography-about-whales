import streamlit as st

def show_page():
    col0,col1, col2, col3= st.columns([1,6,6,1])
    
    with col1:
        st.title("Delfín de pico largo, delfín rotador")
        st.image("./photos/rotador.jpg")
        st.write("Nombre científico: Kogia breviceps")
        st.write("Ubicación: Se encuentre en aguas subtropicales y tropicales de los océanos Atlántico, Pacífico e Índico")
        st.write("Suborden: Odontoceti")
        st.write("Familia: Delphinidae")
        st.write("Subfamilia: Delphinidae")
        st.write("Cantidad de varamientos: 1")
    
    with col2:
        for _ in range(5):
            st.write("    ")
        if st.button("Características físicas"):
            st.write("- Alcanza una talla de 2.35 m los machos y 2.11 m las hembras")
            st.write("- Pesan 78 kg en edad adulta")
            st.write("- Tienen un cuerpo delgado")
            st.write("- Poseen una aleta dorsal triangular")
            st.write("- Poseen manchas oscuras que se extienden desde el dorso hasta el vientre")
        
        if st.button("Origen del nombre"):
           st.write("- El nombre longirostris hace referencia al largo hocico que presentan los individuos de esta especie")
          
        if st.button("Reproducción"):
            st.write("- Al nacer las crías miden 0.77 m")

        if st.button("Alimentación"):
            st.write("- Peces ")
            st.write("- Calamares")
        
        if st.button("Migraciones"):
            st.write("- Se encuentran a lo largo de todo el trópico")
            
        if st.button("Hábitat"):
            st.write("- Prefieren las aguas calidas")
        st.write("   ")
        st.write("   ")
        st.write("Del Delfín de pico largo no se encontró ningún audio")
        
        with st.container(border=True):
            st.markdown("Curiosidades:")
            st.write(" Se alimentan principalmente durante la noche")
            st.write(" Son muy acrobáticos")
    
    