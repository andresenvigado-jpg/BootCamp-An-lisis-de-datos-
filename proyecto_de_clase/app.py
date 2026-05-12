import streamlit as st
import pandas as pd

##Carga de datos
ruta_zni = "data\ZNI.csv"

df = pd.read_csv(ruta_zni)

#  Analisis de datos 
filas = df.shape[0]
columnas = df.shape[1]

#  Visualizar de datos
col1,col2 = st.columns(2) 

with col1:
    with st.container(border=True):
         st.subheader('Numero de filas')
         st.text(filas)

with col2:
    with st.container(border=True):
         st.subheader('Numero de columnas ')
         st.text(filas)

col3,col4 = st.columns(2) 
with col3:
    st.metric('Número de filas', filas , border=True)
with col4:
    st.metric('Número de columnas', columnas , border=True)
         
#st.title('Estado de la prestación del servicio de energía')
#st.header('Zonas no Interconectadas (ZNI)')
#st.subheader('Álvaro Andrés Serna Vasquez')

#st.dataframe(df)
