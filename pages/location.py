import streamlit as st
import streamlit.components.v1 as components
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

def location():
    st.write("Aquí puede apreciar dónde se han avistado varamientos de los diferentes cetáceos en Cuba")
    especie=st.multiselect('Selecciona las especies:',options=["Delfín de dientes estirados (Esteno)","Delfín de pico largo, delfín rotador","Delfín moteado del Atlántico","Delfín moteado pantropical","Ballena Sei o boreal","Falsa orca","Rorcual común (rorcual franco)","Calderón de aleta corta (ballena piloto)","Delfín de Risso (calderón gris)","Orca ballena asesina","Cachalote (ballena de esperma)","Ballena jorobada( yubarta)","Cachalote pigmeo","Cachalote enano","Zifio de Gervais","Ballena de pico de Cuvier"], default=[])

    m = folium.Map(location=[20.0, -75.0], zoom_start=7)
    if "Delfín de dientes estirados (Esteno)" in especie:
        folium.Marker([23.13302, -82.38304], popup='Delfín de dientes estirados (Esteno) - Julio 1954-1', icon=folium.Icon(color='blue')).add_to(m)
        folium.Marker([19.96996307373047, -76.40705871582031], popup='Delfín de dientes estirados (Esteno) - Noviembre 2001-1', icon=folium.Icon(color='blue')).add_to(m)
        folium.Marker([23.155555555556, -81.926666666667], popup='Delfín de dientes estirados (Esteno) - Mayo 2004-1', icon=folium.Icon(color='blue')).add_to(m)
        folium.Marker([22.5078, -78.367], popup='Delfín de dientes estirados (Esteno) - septiembre 2005-2', icon=folium.Icon(color='blue')).add_to(m)
        folium.Marker([19.9,-75.8], popup='Delfín de dientes estirados (Esteno) - Marzo 2009-1', icon=folium.Icon(color='blue')).add_to(m)
    if "Delfín de pico largo, delfín rotador" in especie:
        folium.Marker([19.8554526, -75.3975], popup='Delfín de pico largo (delfín rotador) - Marzo 1989-1', icon=folium.Icon(color='green')).add_to(m)
    if "Delfín moteado del Atlántico" in especie:
        folium.Marker([23.13302, -82.38304], popup='Delfín moteado del Atlántico - 1911-1', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([22.13,-83.56], popup='Delfín moteado del Atlántico - 1967-1', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([23.04111, -81.5775], popup='Delfín moteado del Atlántico - 1991-2', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([23.04111, -81.5775], popup='Delfín moteado del Atlántico - octubre 2004 -2', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([22.13,-83.56], popup='Delfín moteado del Atlántico - noviembre 2004-100', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([23.13,-82.42], popup='Delfín moteado del Atlántico - septiembre 2005-100', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([23.167 ,-82.200], popup='Delfín moteado del Atlántico - abril 2006-100', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([23.13,-82.42], popup='Delfín moteado del Atlántico - enero 2008-2', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([22.63, -79.201], popup='Delfín moteado del Atlántico - febrero 2008-2', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([23.1333, -81.2833], popup='Delfín moteado del Atlántico - marzo 2008-8', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([23.1333, -81.2833], popup='Delfín moteado del Atlántico - agosto 2008-4', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([23.13,-82.42], popup='Delfín moteado del Atlántico - marzo 2010-5', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([23.1333, -81.2833], popup='Delfín moteado del Atlántico - marzo 2010-10', icon=folium.Icon(color='red')).add_to(m)
    if "Delfín moteado pantropical" in especie:
        folium.Marker([23.1453,-82.3724], popup='Delfín moteado pantropical - 1974-1', icon=folium.Icon(color='purple')).add_to(m)
        folium.Marker([22.63, -79.201], popup='Delfín moteado pantropical - julio 2006-50', icon=folium.Icon(color='purple')).add_to(m)
        folium.Marker([23.053415,-82.556181], popup='Delfín moteado pantropical - febrero 2009-1', icon=folium.Icon(color='purple')).add_to(m)
        folium.Marker([19.904185,-75.868076], popup='Delfín moteado pantropical - marzo 2009-1', icon=folium.Icon(color='purple')).add_to(m)
        folium.Marker([22.13,-83.56], popup='Delfín moteado pantropical - septiembre 2009-1', icon=folium.Icon(color='purple')).add_to(m)
    if "Ballena Sei o boreal" in especie:
        folium.Marker([20.02083 , -75.82667], popup='Ballena Sei o boreal -Enero de 1963-1', icon=folium.Icon(color='gray')).add_to(m)
        folium.Marker([19.82, -77.30], popup='Ballena Sei o boreal - Febrero 1975-1', icon=folium.Icon(color='gray')).add_to(m)
    if "Falsa orca" in especie:
        folium.Marker([23.1453,-82.3724], popup='Falsa orca - Julio 1954-1', icon=folium.Icon(color='blue')).add_to(m)
        folium.Marker([23.1542400, -819255600], popup='Falsa orca - Noviembre 2001-1', icon=folium.Icon(color='blue')).add_to(m)
        folium.Marker([22.5078, -78.367], popup='Falsa orca - Mayo 2004-1', icon=folium.Icon(color='blue')).add_to(m)
        folium.Marker([22.5078, -78.367], popup='Falsa orca - septiembre 2005-2', icon=folium.Icon(color='blue')).add_to(m)
        folium.Marker([19.9,-75.8], popup='Falsa orca - Marzo 2009-1', icon=folium.Icon(color='Light blue')).add_to(m)
    if "Rorcual común (rorcual franco)" in especie:
        folium.Marker([22.16667 , -83.91667], popup='Rorcual común (rorcual franco) - Julio 1989-1', icon=folium.Icon(color='Light purple')).add_to(m)
    if "Calderón de aleta corta (ballena piloto)" in especie:
        folium.Marker([23.04855, -81.57282], popup='Calderón de aleta corta (ballena piloto) - 1908-1', icon=folium.Icon(color='Ligthred')).add_to(m)
        folium.Marker([23.067063,-81.513965], popup='Calderón de aleta corta (ballena piloto) - julio 1954-1', icon=folium.Icon(color='Ligthred')).add_to(m)
        folium.Marker([23.1735,-82.2919], popup='Calderón de aleta corta (ballena piloto) - 1964-1', icon=folium.Icon(color='Ligthred')).add_to(m)
        folium.Marker([23.164,-82.3415], popup='Calderón de aleta corta (ballena piloto) - noviembre 1971-1', icon=folium.Icon(color='Ligthred')).add_to(m)
        folium.Marker([23.1453,-82.3724], popup='Calderón de aleta corta (ballena piloto) - octubre 1981-1', icon=folium.Icon(color='Ligthred')).add_to(m)
        folium.Marker([20.75944, -75.52083], popup='Calderón de aleta corta (ballena piloto) - febrero 1986-14', icon=folium.Icon(color='Ligthred')).add_to(m)
        folium.Marker([20.88722, -76.26306], popup='Calderón de aleta corta (ballena piloto) - marzo 1986-2', icon=folium.Icon(color='Ligthred')).add_to(m)
        folium.Marker([19.938719,-75836711], popup='Calderón de aleta corta (ballena piloto) - septiembre 1988-1', icon=folium.Icon(color='Ligthred')).add_to(m)
        folium.Marker([21.12, -76.06], popup='Calderón de aleta corta (ballena piloto) - noviembre 1988-2', icon=folium.Icon(color='Ligthred')).add_to(m)
        folium.Marker([22.41, -78.73], popup='Calderón de aleta corta (ballena piloto) - julio 2004-1', icon=folium.Icon(color='Ligthred')).add_to(m)
    if "Delfín de Risso (calderón gris)" in especie:
        folium.Marker([22.9 , -80.5], popup='Delfín de Risso (calderón gris) -agosto 1972-1', icon=folium.Icon(color='Light gray')).add_to(m)
        folium.Marker([23.13,-82.42], popup='Delfín de Risso (calderón gris) - octubre 1981-1', icon=folium.Icon(color='Light gray')).add_to(m)
        folium.Marker([22.41, -78.73], popup='Delfín de Risso (calderón gris) -septiembre 1997-4', icon=folium.Icon(color='Light gray')).add_to(m)
        folium.Marker([21.67,-79.99], popup='Delfín de Risso (calderón gris) - febrero 2004-1', icon=folium.Icon(color='Light gray')).add_to(m)
    if "Orca ballena asesina" in especie:
        folium.Marker([23.18,-82.214], popup='Orca ballena asesina - 1983-3', icon=folium.Icon(color='white')).add_to(m)
        folium.Marker([23.13,-82.42], popup='Orca ballena asesina - agosto 1984-1', icon=folium.Icon(color='white')).add_to(m)
        folium.Marker([21.832444,-77.697712], popup='Orca ballena asesina - junio 1991-1', icon=folium.Icon(color='white')).add_to(m)
        folium.Marker([23.13,-82.42], popup='Orca ballena asesina - agosto 1994-4', icon=folium.Icon(color='white')).add_to(m)
        folium.Marker([22.41, -78.73], popup='Orca ballena asesina - 2005-4', icon=folium.Icon(color='white')).add_to(m)
        folium.Marker([22.63, -79.201], popup='Orca ballena asesina - abril 2004-1', icon=folium.Icon(color='white')).add_to(m)
    if "Cachalote (ballena de esperma)" in especie:
        folium.Marker([22.9 , -80.5], popup='Cachalote (ballena de esperma) - julio 1954-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([23.01,-80.46], popup='Cachalote (ballena de esperma) - febrero 1963-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([22.5158,-79.4722], popup='Cachalote (ballena de esperma) - febrero 1963-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([22.9 , -80.5], popup='Cachalote (ballena de esperma) - febrero 1963-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([22.2018,-81.1702], popup='Cachalote (ballena de esperma) - julio 1970-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([23.1585,-82.3566], popup='Cachalote (ballena de esperma) - octubre 1971-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([22.2018,-81.1702], popup='Cachalote (ballena de esperma) - octubre 1971-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([19.904185,-75.86], popup='Cachalote (ballena de esperma) - agosto 1974-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([19.904185,-75.86], popup='Cachalote (ballena de esperma) - junio 1979-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([19.9,-75.8], popup='Cachalote (ballena de esperma) - junio 1979-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([20.78378930, -75.80690820], popup='Cachalote (ballena de esperma) - marzo 1986-14-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([19.9,-75.8], popup='Cachalote (ballena de esperma) - octubre 1988-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([23.1585,-82.3566], popup='Cachalote (ballena de esperma) - noviembre 1991-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([23.1585,-82.3566], popup='Cachalote (ballena de esperma) - marzo 2003-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([19.9,-75.8], popup='Cachalote (ballena de esperma) - agosto 2006-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([19.9,-75.8], popup='Cachalote (ballena de esperma) - mayo 2007-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([23.01,-80.46], popup='Cachalote (ballena de esperma) - noviembre 1995-5', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([23.01,-80.46], popup='Cachalote (ballena de esperma) - marzo 2002-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([22.2018,-81.1702 ], popup='Cachalote (ballena de esperma) - marzo 2008-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([19.9,-75.8], popup='Cachalote (ballena de esperma) - septiembre 1943-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([19.9,-75.8], popup='Cachalote (ballena de esperma) - mayo 1978-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([20.78378930, -75.80690820], popup='Cachalote (ballena de esperma) - marzo 1989-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([19.9,-75.8], popup='Cachalote (ballena de esperma) - mayo 1989-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([20.40304, -77.20717], popup='Cachalote (ballena de esperma) - noviembre 1989-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([22.2018,-81.1702], popup='Cachalote (ballena de esperma) - febrero 1996-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([22.41, -78.73], popup='Cachalote (ballena de esperma)- octubre 2000-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([19.9,-75.8], popup='Cachalote (ballena de esperma) - mayo 2006-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([21.5, -77.5], popup='Cachalote (ballena de esperma) - diciembre 2006-1', icon=folium.Icon(color='Ligth red')).add_to(m)
        folium.Marker([19.9,-75.8], popup=' Cachalote (ballena de esperma) - mayo 2009-1', icon=folium.Icon(color='Ligth red')).add_to(m)
    if "Ballena jorobada( yubarta)" in especie:
        folium.Marker([23.1748,-82.303902], popup='Ballena jorobada( yubarta) - 1932-1', icon=folium.Icon(color='Ligth yellow')).add_to(m)
        folium.Marker([21.67,-79.995], popup='Ballena jorobada( yubarta) - junio 1997-1', icon=folium.Icon(color='Ligth yellow')).add_to(m)
        folium.Marker([23.1748,-82.303902], popup='Ballena jorobada( yubarta) - enero 1999-1', icon=folium.Icon(color='Ligth yellow')).add_to(m)
        folium.Marker([21.5, -77.5], popup='Ballena jorobada( yubarta) - julio 2002-2', icon=folium.Icon(color='Ligth yellow')).add_to(m)
        folium.Marker([23.1748,-82.303902], popup='Ballena jorobada( yubarta) - diciembre 2004-1', icon=folium.Icon(color='Ligth yellow')).add_to(m)
        folium.Marker([23.1748,-82.303902], popup='Ballena jorobada( yubarta) - enero 2005-1', icon=folium.Icon(color='Ligth yellow')).add_to(m)
        folium.Marker([23.1748,-82.303902], popup='Ballena jorobada( yubarta)- abril 2006-2', icon=folium.Icon(color='Ligth yellow')).add_to(m)
        folium.Marker([19.9,-75.8], popup='Ballena jorobada( yubarta) - marzo 2008-2', icon=folium.Icon(color='Ligth yellow')).add_to(m)
        folium.Marker([20.35224, -74.484443], popup='Ballena jorobada( yubarta) - diciembre 2006-1', icon=folium.Icon(color='Ligth yellow')).add_to(m)
        folium.Marker([19.8725, -75.5], popup=' Ballena jorobada( yubarta) - febrero 2009-6', icon=folium.Icon(color='Ligth yellow')).add_to(m)
    if "Cachalote pigmeo" in especie:
        folium.Marker([21.5476, -77.189452], popup='Cachalote pigmeo - 1937-1', icon=folium.Icon(color='yellow')).add_to(m)
        folium.Marker([21.5476, -77.189452], popup='Cachalote pigmeo- marzo 1954-1', icon=folium.Icon(color='yellow')).add_to(m)
        folium.Marker([22.2018,-81.1702], popup='Cachalote pigmeo - julio 1954-1', icon=folium.Icon(color='yellow')).add_to(m)
        folium.Marker([23.1585,-82.3566], popup='Cachalote pigmeo - mayo 2005-1', icon=folium.Icon(color='yellow')).add_to(m)
        folium.Marker([23.1585,-82.3566], popup=' Cachalote pigmeo - agosto 2008-1', icon=folium.Icon(color='yellow')).add_to(m)
    if "Cachalote enano" in especie:
        folium.Marker([23.164,-82.3415], popup='Cachalote enano - 1977-1', icon=folium.Icon(color='Dark yellow')).add_to(m)
        folium.Marker([19.892166,-75.44477], popup='Cachalote enano - febrero 2004-1', icon=folium.Icon(color='Dark yellow')).add_to(m)
        folium.Marker([19.9,-75.8], popup=' Cachalote enano - septiembre 2007-1', icon=folium.Icon(color='Dark yellow')).add_to(m)
    if "Zifio de Gervais" in especie:
        folium.Marker([22.84,-83.68], popup='Zifio de Gervais - noviembre 1946-1', icon=folium.Icon(color='Dark blue')).add_to(m)
        folium.Marker([22.84,-83.68], popup='Zifio de Gervais - julio 1954-1', icon=folium.Icon(color='Dark blue')).add_to(m)
        folium.Marker([23.1585,-82.3566], popup='Zifio de Gervais - marzo 1965-1', icon=folium.Icon(color='Dark blue')).add_to(m)
        folium.Marker([22.84,-83.68], popup='Zifio de Gervais - noviembre 1969-2', icon=folium.Icon(color='Dark blue')).add_to(m)
        folium.Marker([23.1585,-82.3566], popup='Zifio de Gervais - noviembre 1971-2', icon=folium.Icon(color='Dark blue')).add_to(m)
        folium.Marker([19.911,-76.00], popup='Zifio de Gervais - junio 1979-1', icon=folium.Icon(color='Dark blue')).add_to(m)
        folium.Marker([23.1585,-82.3566], popup='Zifio de Gervais- noviembre 1982-1', icon=folium.Icon(color='Dark blue')).add_to(m)
        folium.Marker([23.1585,-82.3566], popup='Zifio de Gervais) - abril 1984-1', icon=folium.Icon(color='Dark blue')).add_to(m)
        folium.Marker([19.94, -74.92], popup='Zifio de Gervais - agosto 1988-1', icon=folium.Icon(color='Dark blue')).add_to(m)
        folium.Marker([19.9,-75.8], popup=' Zifio de Gervais - octubre 1988-1', icon=folium.Icon(color='Dark blue')).add_to(m)
    if "Ballena de pico de Cuvier" in especie:
        folium.Marker([22.9 , -80.5], popup='Ballena de pico de Cuvier - julio 1954-1', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker([23.01,-80.46], popup='Ballena de pico de Cuvier - febrero 1963-1', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker([23.126138,-81.485063], popup='Ballena de pico de Cuvier - febrero 1963-1', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker([22.9 , -80.5], popup='Ballena de pico de Cuvier - febrero 1963-1', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker([22.2018,-81.1702], popup='Ballena de pico de Cuvier - julio 1970-1', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker([23.1585,-82.3566], popup='Ballena de pico de Cuvier - octubre 1971-1', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker([23.1585,-82.3566 ], popup='Ballena de pico de Cuvier - octubre 1971-1', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker([23.1585,-82.3566], popup='Ballena de pico de Cuvier - octubre 1971-3', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker([19.9,-75.8], popup='Ballena de pico de Cuvier - agosto 1974-1', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker([19.9,-75.8], popup='Ballena de pico de Cuvier - junio 1979-1', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker([19.9,-75.8], popup='Ballena de pico de Cuvier - junio 1979-1', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker([20.78378930, -75.80690820], popup='Ballena de pico de Cuvier - marzo 1986-14', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker([19.9,-75.8], popup='Ballena de pico de Cuvier - octubre 1988-1', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker([19.9588, -76117611], popup='Ballena de pico de Cuvier- noviembre 1991-1', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker([23.1585,-82.3566], popup='Ballena de pico de Cuvier - marzo 2003-1', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker([19.9,-75.8], popup='Ballena de pico de Cuvier - agosto 2006-1', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker([19.9,-75.8], popup=' Ballena de pico de Cuvier - mayo 2007-1', icon=folium.Icon(color='orange')).add_to(m)


    folium_static(m)