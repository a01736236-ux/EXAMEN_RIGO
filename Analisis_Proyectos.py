import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Dashboard principal de proyectos")

# Cargo los datos
def cargar_datos():
    return pd.read_csv("datos/exam_data.csv")

df = cargar_datos()

# Ocupo sidebar para los filtros
st.sidebar.header("Filtros")

estado = st.sidebar.selectbox("Estado", ["Todos"] + sorted(df["State"].unique()))
categoria = st.sidebar.selectbox("Categoría", ["Todos"] + sorted(df["Category"].unique()))
avance_min = st.sidebar.slider("Avance mínimo (%)", 0, 100, 0)
manager = st.sidebar.selectbox("Manager", ["Todos"] + sorted(df["Manager"].unique()))

# ocupo df_filtrado para filtrar los datos 
df_filtrado = df.copy()

if estado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["State"] == estado]

if categoria != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Category"] == categoria]

df_filtrado = df_filtrado[df_filtrado["PercentComplete"] >= avance_min]

if manager != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Manager"] == manager]

# muestro los kpis con st.columns
col1, col2, col3, col4 = st.columns(4)

total_proyectos = len(df_filtrado)
promedio_avance = df_filtrado["PercentComplete"].mean()
managers_unicos = df_filtrado["Manager"].nunique()
total_presupuesto = df_filtrado["BudgetThousands"].sum()

col1.metric("Total Proyectos", total_proyectos)
col2.metric("Promedio avance (%)", round(promedio_avance, 1) if total_proyectos > 0 else 0)
col3.metric("Managers únicos", managers_unicos)
col4.metric("Total Presupuesto (k$)", f"{round(total_presupuesto, 1)}K")

st.markdown("---")

# muestro la tabla de datos
st.subheader("Tabla de proyectos")
st.dataframe(df_filtrado, use_container_width=True)

# muestro la gráfica de dispersión
st.subheader("Visualizaciones y comparación")

if not df_filtrado.empty:
    fig = px.scatter(
        df_filtrado,
        x="BudgetThousands",
        y="PercentComplete",
        color="State",
        hover_data=["ProjectName", "Manager", "Country"],
        title="Avance vs Presupuesto (k$)"
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No hay datos con los filtros seleccionados.")