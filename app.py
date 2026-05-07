import streamlit as st
import pandas as pd

ruta_zni = "https://raw.githubusercontent.com/andresenvigado-jpg/BootCamp-An-lisis-de-datos-/main/Estado_de_la_prestaci%C3%B3n_del_servicio_de_energ%C3%ADa_en_Zonas_No_Interconectadas_20260422.csv"

df = pd.read_csv(ruta_zni)

st.title('Estado de la prestación del servicio de energía')
st.header('Zonas no Interconectadas (ZNI)')
st.subheader('Álvaro Andrés Serna Vasquez')

st.dataframe(df)


