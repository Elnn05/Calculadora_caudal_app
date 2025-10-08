import streamlit as st
import math

st.set_page_config(page_title="Calculadora de Caudal para Tuberías")

st.title("Calculadora de Caudal para Tuberías")
st.markdown("### Fórmula: $Q = A \\times v$")
st.markdown("Donde:<br>- $Q$ = Caudal ($m^3/s$)<br>- $A$ = Área de la sección transversal ($m^2$)<br>- $v$ = Velocidad del fluido ($m/s$)", unsafe_allow_html=True)

def calcular_caudal(diametro, velocidad):
    radio = diametro / 2
    area = math.pi * (radio ** 2)
    return area * velocidad

diametro = st.number_input("Diámetro de la tubería (m)", min_value=0.0, format="%.4f")
velocidad = st.number_input("Velocidad del fluido (m/s)", min_value=0.0, format="%.4f")

if st.button("Calcular Caudal"):
    if diametro > 0 and velocidad > 0:
        caudal = calcular_caudal(diametro, velocidad)
        st.success(f"**Caudal:** {caudal:.4f} m³/s")
    else:
        st.warning("Por favor, ingresa valores mayores a cero para ambos campos.")