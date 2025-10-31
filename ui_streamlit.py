import streamlit as st
from preprocess import preprocess
from ascii_core import image_to_ascii
import ramps as r

presets = {
    "classic": r.ramp_classic,
    "detailed": r.ramp_detailed,
    "blocks": r.ramp_blocks,
}

st.set_page_config(layout="wide")
st.title("Image → ASCII Art")

with st.sidebar:
    uploaded = st.file_uploader("Sube una imagen", type=["png", "jpg", "jpeg"])
    width = st.slider("Ancho (cols)", 60, 250, 120, 2)
    aspect = st.slider("Corrección de aspecto", 0.2, 0.6, 0.5, 0.05)
    gamma = st.slider("Gamma", 0.8, 3.0, 1.0, 0.1)
    blur = st.slider("Suavizado", 0.0, 1.0, 0.5, 0.05)
    invert = st.checkbox("Invertir rampa", value=False)
    block_size = st.slider("Tamaño del bloque de muestreo", 1, 8, 4)
    preset = st.selectbox("Preset", ["classic", "detailed", "blocks"])
    ramp = presets[preset]
    custom_ramp = st.checkbox("Usar rampa personalizada", value=False)
    if custom_ramp:
        ramp = st.text_input(
            "Rampa personalizada (oscuro → claro)",
            value=ramp,
            help="Ejemplo: @#%*+=-:.  (primer char = más oscuro)"
        )

if uploaded:
    img = preprocess(uploaded, max_size=800, blur=blur)
    ascii_art = image_to_ascii(
        img, width=width, invert=invert, block_size=block_size, ramp=ramp, gamma=gamma, aspect_correction=aspect
    )

    st.subheader("ASCII")
    st.code(ascii_art, language=None)
    st.download_button("Descargar .txt", ascii_art, file_name="ascii.txt")

    st.subheader("Original")
    st.image(img, width="stretch")
else:
    st.info("Sube una imagen desde la barra lateral para empezar.")
