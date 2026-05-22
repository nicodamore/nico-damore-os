import streamlit as st
import google.generativeai as genai
import os

# Configuración
api_key = "AIzaSyASV32UU7chcBClu3gQODiqCgHhMxi2wtE" # REVISÁ QUE ESTÉ TU CÓDIGO AQUÍ
genai.configure(api_key=api_key)

st.set_page_config(page_title="NICO DAMORE | OS", layout="wide")
st.title("🖥️ NICO DAMORE | DASHBOARD OPERATIVO")

menu = st.sidebar.selectbox("Selecciona Proyecto", ["EDUL", "SOFI", "SURREAL"])
tema = st.text_area("¿De qué trata la miniatura?")

if st.button("Generar Conceptos"):
    if not tema:
        st.warning("Escribí el tema.")
    else:
        try:
            # CAMBIO: Usaremos 'gemini-1.5-flash' por ser más estable para respuestas rápidas
            model = genai.GenerativeModel('gemini-pro')
            prompt = f"Actúa como mi Director de Arte. Genera 4 conceptos de miniatura para {menu} sobre: {tema}. Sigue mi estilo de alto impacto y tensión visual."
            
            with st.spinner('Procesando...'):
                response = model.generate_content(prompt)
                st.markdown(response.text)
        except Exception as e:
            st.error(f"Error técnico: {e}")
