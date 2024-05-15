import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from streamlit_option_menu import option_menu
from  PIL import Image

st.set_page_config(page_title="Alejandro Paredes", page_icon=":bar_chart:", layout="wide")
hide_st_style = """
<style>
#MainMenu {
  visibility: hidden;
  }
footer {
  visibility: hidden;
  }
header {
  visibility: hidden;
}
</style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)

st.header('**Alejandro Paredes Balgañón**')
st.header('**Uso de Plataformas de Streaming**')
selected = option_menu(None, ["Dashboard","Reporte", "Mapa", "Sobre Mi", "Referencias"],
    icons=['bar-chart','clipboard', 'map', "house", 'gear'],
    menu_icon="cast", default_index=0, orientation="horizontal")

# Referencias
if selected == "Referencias":
  url_Streaming = "https://www.kaggle.com/datasets/rajatkumar30/streaming-application-viewership"
  url_Countinent = "https://www.kaggle.com/datasets/andradaolteanu/country-mapping-iso-continent-region"
  url_CodesCountry = "https://www.kaggle.com/datasets/andradaolteanu/iso-country-codes-global"
  st.write(f'''Para este trabajo se utilizaron algunas bases de datos de kagle:
  - [Conjunto de datos de Streaming]( {url_Streaming} )
  - [Conjunto de datos de los Continetes]( {url_Countinent} )
  - [Conjunto de datos de lo codigos de los países]( {url_CodesCountry} )
  ''')
  st.markdown('________________________')


# Sobre Mi
if selected == 'Sobre Mi':

  st.markdown(""" <style> .font {
  font-size:35px ; font-family: 'Cooper Black'; color: #8eff8e;}
  </style> """,unsafe_allow_html=True)
  st.markdown('<p class="font">Sobre mi 👨‍🎓💻</p>', unsafe_allow_html=True)

  st.write(f'''Bienvenidos a mi página web, yo soy Alejandro Paredes Balgañon.''')
  st.write(f'''Estudiante de séptimo semestre de ingeniería en transformación digital de negocios, interesado en la parte de análisis y visualización de los datos.
            Me considero una persona organizada, responsable, capaz de resolver cualquier problema, y
            busco adquirir nuevas habilidades que me permitan seguir desarrollándome como persona y como profesional.
            ''')

# Reporte
if selected == 'Reporte':
  st.header("Reporte :clipboard:")
  st.markdown('________________________')

# Mapa
if selected == 'Mapa':
  st.header("Mapa :world_map:")
  st.markdown('________________________')

# Dashboard
if selected == 'Dashboard':
  st.header("Dashboard :bar_chart:")
