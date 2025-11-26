import streamlit as st

st.set_page_config(
    page_title="Dashboard de Proyectos",
    layout="wide"
)

# Creo el menu de la página
st.sidebar.markdown("### 🏠 Inicio")
st.page_link("app.py", label="Home")
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Visualización")
st.page_link("pages/Analisis_Proyectos.py", label="Análisis de Proyectos")
st.page_link("pages/Visualizacion.py", label="Visualización general")