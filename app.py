import streamlit as st

# -------------------------------------------------------
# CONFIGURACIÓN GENERAL
# -------------------------------------------------------
st.set_page_config(
    page_title="Proyecto Aplicado – Fundamentos de Programación",
    page_icon="📘",
    layout="centered"
)

st.markdown("""
<style>
.section-header {
    background: linear-gradient(135deg, #1f77b4, #6a5acd);
    padding: 20px;
    border-radius: 12px;
    color: white;
    text-align: center;
    margin-bottom: 20px;
    animation: fadeIn 1.5s ease-in;
}

.card {
    background-color: #f8f9fc;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 2px 2px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# MENÚ LATERAL
# -------------------------------------------------------
menu = st.sidebar.selectbox(
    "Menú de Navegación",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# =======================================================
# HOME – PRESENTACIÓN DEL PROYECTO
# =======================================================
if menu == "Home":

    st.markdown("""
    <style>

    /* HERO PRINCIPAL */
    .hero-box {
        background: linear-gradient(135deg, #4e73df, #6f42c1);
        padding: 35px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        animation: fadeIn 1.5s ease-in;
    }

    /* CARDS CON TEXTO OSCURO FORZADO */
    .card-soft-blue {
        background: linear-gradient(135deg, #e3f2fd, #bbdefb);
        padding: 25px;
        border-radius: 20px;
        margin-bottom: 20px;
        color: #1f2937;  /* Gris oscuro elegante */
    }

    .card-soft-green {
        background: linear-gradient(135deg, #e8f5e9, #c8e6c9);
        padding: 25px;
        border-radius: 20px;
        margin-bottom: 20px;
        color: #1f2937;
    }

    .card-soft-purple {
        background: linear-gradient(135deg, #f3e5f5, #e1bee7);
        padding: 25px;
        border-radius: 20px;
        margin-bottom: 20px;
        color: #1f2937;
    }

    /* Mejorar títulos dentro de cards */
    .card-soft-blue h3,
    .card-soft-green h3,
    .card-soft-purple h3 {
        color: #111827;
        margin-bottom: 10px;
    }

    /* Animación */
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(15px);}
        to {opacity: 1; transform: translateY(0);}
    }

    /* Tecnologías */          
    .tech-badge {
        display: inline-block;
        padding: 8px 15px;
        margin: 5px;
        border-radius: 20px;
        background-color: #1f77b4;
        color: white;
        font-size: 14px;
    }

    </style>
    """, unsafe_allow_html=True)

    # PRESENTACIÓN
    st.markdown("""
    <div class="hero-box">
        <h1>📊 Proyecto Aplicado en Streamlit</h1>
        <h3>Fundamentos de Programación – Módulo 1</h3>
        <p>Aplicación interactiva que integra conceptos fundamentales de programación</p>
    </div>
    """, unsafe_allow_html=True)

    # INFORMACIÓN
    st.markdown("""
    <div class="card-soft-blue">
        <h3>👨‍🎓 Información del Estudiante</h3>
        <p><strong>Nombre completo:</strong> Omar Anthony Poma Vega</p>
        <p><strong>Curso:</strong> Fundamentos de Programación – Módulo 1</p>
        <p><strong>Año:</strong> 2026</p>
    </div>
    """, unsafe_allow_html=True)

    # OBJETIVO
    st.markdown("""
    <div class="card-soft-green">
        <h3>🎯 Objetivo del Proyecto</h3>
        <p>
        Desarrollar una aplicación interactiva utilizando Streamlit que permita
        integrar variables, estructuras de datos, condicionales, funciones,
        programación funcional y Programación Orientada a Objetos (POO).
        </p>
    </div>
    """, unsafe_allow_html=True)

    # TECNOLOGÍAS
    st.subheader("⚙️ Tecnologías Utilizadas")
    st.markdown("""
    <div>
        <span class="tech-badge">Python</span>
        <span class="tech-badge">Streamlit</span>
        <span class="tech-badge">Programación Funcional</span>
        <span class="tech-badge">Programación Orientada a Objetos (POO)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.info("🚀 Utiliza el menú lateral para navegar por cada ejercicio desarrollado.")
# =======================================================
# EJERCICIO 1
# =======================================================
elif menu == "Ejercicio 1":

    st.markdown('<div class="section-header"><h2>💰 Ejercicio 1 – Verificador de Presupuesto</h2></div>', unsafe_allow_html=True)

    presupuesto = st.number_input("Ingrese el presupuesto", min_value=0.0, format="%.2f")
    gasto = st.number_input("Ingrese el gasto", min_value=0.0, format="%.2f")

    if st.button("Evaluar Presupuesto"):

        diferencia = presupuesto - gasto

        if gasto <= presupuesto:
            st.success("El gasto está dentro del presupuesto ✅")
            st.write(f"Diferencia disponible: S/ {round(diferencia,2)}")
        else:
            st.warning("El presupuesto fue excedido ⚠️")
            st.write(f"Exceso: S/ {round(abs(diferencia),2)}")

    st.markdown('</div>', unsafe_allow_html=True)
# =======================================================
# EJERCICIO 2
# =======================================================
elif menu == "Ejercicio 2":

    st.markdown('<div class="section-header"><h2>📋 Ejercicio 2 – Registro de Actividades</h2></div>', unsafe_allow_html=True)

    if "actividades" not in st.session_state:
        st.session_state.actividades = []

    nombre = st.text_input("Nombre de la actividad")
    tipo = st.selectbox("Tipo", ["Inversión", "Gasto", "Ahorro"])
    presupuesto = st.number_input("Presupuesto", min_value=0.0)
    gasto_real = st.number_input("Gasto Real", min_value=0.0)

    if st.button("Agregar Actividad"):
        actividad = {
            "nombre": nombre,
            "tipo": tipo,
            "presupuesto": presupuesto,
            "gasto_real": gasto_real
        }
        st.session_state.actividades.append(actividad)
        st.success("Actividad agregada correctamente")

    st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.actividades:

        st.subheader("📑 Lista de Actividades")
        st.dataframe(st.session_state.actividades)

        st.subheader("Estado de cada actividad")

        for act in st.session_state.actividades:
            if act["gasto_real"] <= act["presupuesto"]:
                st.success(f"{act['nombre']} está dentro del presupuesto")
            else:
                st.warning(f"{act['nombre']} excedió el presupuesto")

        st.markdown('</div>', unsafe_allow_html=True)
# =======================================================
# EJERCICIO 3
# =======================================================
elif menu == "Ejercicio 3":

    st.markdown('<div class="section-header"><h2>📈 Ejercicio 3 – Cálculo de Retorno</h2></div>', unsafe_allow_html=True)

    if "actividades" not in st.session_state or not st.session_state.actividades:
        st.warning("Primero registre actividades en el Ejercicio 2.")
    else:

        def calcular_retorno(actividad, tasa, meses):
            return actividad["presupuesto"] * tasa * meses

        tasa = st.slider("Tasa (%)", 0.0, 1.0, 0.1)
        meses = st.number_input("Meses", min_value=1)

        if st.button("Calcular Retorno"):

            retornos = list(
                map(
                    lambda act: {
                        "nombre": act["nombre"],
                        "retorno": calcular_retorno(act, tasa, meses)
                    },
                    st.session_state.actividades
                )
            )

            for r in retornos:
                st.info(f"{r['nombre']} → Retorno esperado: S/ {round(r['retorno'],2)}")

        st.markdown('</div>', unsafe_allow_html=True)
# =======================================================
# EJERCICIO 4
# =======================================================
elif menu == "Ejercicio 4":

    st.markdown('<div class="section-header"><h2>🧠 Ejercicio 4 – Programación Orientada a Objetos</h2></div>', unsafe_allow_html=True)

    class Actividad:
        def __init__(self, nombre, tipo, presupuesto, gasto_real):
            self.nombre = nombre
            self.tipo = tipo
            self.presupuesto = presupuesto
            self.gasto_real = gasto_real

        def esta_en_presupuesto(self):
            return self.gasto_real <= self.presupuesto

        def mostrar_info(self):
            return f"{self.nombre} | Tipo: {self.tipo} | Presupuesto: {self.presupuesto} | Gasto Real: {self.gasto_real}"

    if "actividades" not in st.session_state or not st.session_state.actividades:
        st.warning("Primero registre actividades en el Ejercicio 2.")
    else:

        objetos = [
            Actividad(
                act["nombre"],
                act["tipo"],
                act["presupuesto"],
                act["gasto_real"]
            )
            for act in st.session_state.actividades
        ]

        for obj in objetos:
            st.write(obj.mostrar_info())

            if obj.esta_en_presupuesto():
                st.success("Cumple el presupuesto ✅")
            else:
                st.warning("No cumple el presupuesto ⚠️")

        st.markdown('</div>', unsafe_allow_html=True)