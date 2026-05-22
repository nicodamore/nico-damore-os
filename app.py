import streamlit as st
import google.generativeai as genai

# Configuración de la API
api_key = 'AIzaSyASV32UU7chcBClu3gQODiqCgHhMxi2wtE' 
genai.configure(api_key=api_key)

st.set_page_config(page_title="NICO DAMORE | OS", layout="wide")
st.title("🖥️ NICO DAMORE | DASHBOARD OPERATIVO")

# Selección de Proyecto
menu = st.sidebar.selectbox("Selecciona Proyecto", ["EDUL", "SOFI", "SURREAL"])

# Área de Trabajo
st.header(f"Módulo: {menu}")
tema = st.text_area("¿De qué trata la miniatura?")

if st.button("Generar Conceptos"):
    if not tema:
        st.warning("Por favor, describí el tema de la miniatura.")
    else:
        model = genai.GenerativeModel('gemini-1.5-pro')
        prompt = f"Actúa como mi Director de Arte. Genera 4 conceptos de miniatura para {menu} sobre: {tema}. Sigue mi estilo de alto impacto y tensión visual."
        
        with st.spinner('Nico Damore OS procesando...'):
            response = model.generate_content(prompt)
            st.markdown(response.text)
