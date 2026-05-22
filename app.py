import streamlit as st
import google.generativeai as genai

# Configuración
api_key = st.secrets["AIzaSyASV32UU7chcBClu3gQODiqCgHhMxi2wtE"]
genai.configure(api_key=api_key)

st.set_page_config(page_title="NICO DAMORE | OS", layout="wide")
st.title("🖥️ NICO DAMORE | DASHBOARD OPERATIVO")

menu = st.sidebar.selectbox("Selecciona Proyecto", ["EDUL", "SOFI", "SURREAL"])
tema = st.text_area("¿De qué trata la miniatura?")

if st.button("Generar Conceptos"):
    if not tema:
        st.warning("Escribí el tema primero.")
    else:
        try:
            # Usamos el alias 'gemini-1.5-flash' sin sufijos complicados
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"Actúa como Director de Arte. Genera 4 conceptos de miniatura para {menu} sobre: {tema}. Estilo: Tensión visual, urgencia periodística, alto impacto."
            
            with st.spinner('Procesando...'):
                response = model.generate_content(prompt)
                st.write(response.text)
        except Exception as e:
            st.error(f"Error técnico: {e}")
