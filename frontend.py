import streamlit as st
from data import gejala
from backend import forward_chaining
from theme import apply_theme   # ⬅️ IMPORT TEMA

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="Sistem Pakar Kerusakan Komputer",
    page_icon="🧠",
    layout="centered"
)

# ==================================================
# APPLY THEME
# ==================================================
apply_theme()

# ==================================================
# HEADER
# ==================================================
st.markdown(
    "<h1 style='text-align:center;'>🧠 Sistem Pakar Diagnosa Kerusakan Komputer</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<div class='subtitle'>Metode Forward Chaining</div>",
    unsafe_allow_html=True
)

st.divider()

# ==================================================
# INPUT GEJALA
# ==================================================
st.subheader("🔍 Pilih Gejala yang Dialami")

fakta = []

with st.expander("📋 Daftar Gejala", expanded=True):
    for kode, teks in gejala.items():
        if st.checkbox(f"{kode} — {teks}", key=kode):
            fakta.append(kode)

st.divider()

# ==================================================
# ACTION BUTTON
# ==================================================
diagnosa = st.button("🔎 Diagnosa Sekarang!", use_container_width=True)

# ==================================================
# HASIL DIAGNOSA
# ==================================================
if diagnosa:
    hasil_final, indikasi = forward_chaining(fakta)

    st.subheader("📊 Hasil Analisis")

    # ---- Diagnosis Utama ----
    if hasil_final:
        st.markdown(
            "<div class='diagnosis-box'><strong>✅ Diagnosis Utama</strong></div>",
            unsafe_allow_html=True
        )
        for h in hasil_final:
            st.markdown(f"🔧 **{h['kerusakan']}**")

    # ---- Indikasi Lainnya ----
    if indikasi:
        st.markdown(
            "<div class='indication-box'><strong>⚠️ Indikasi Kerusakan Lainnya</strong></div>",
            unsafe_allow_html=True
        )
        for i in indikasi:
            st.markdown(f"• **{i['kerusakan']}**")

    # ---- Tidak Ada Hasil ----
    if not hasil_final and not indikasi:
        st.error("❌ Tidak ditemukan indikasi atau diagnosis kerusakan.")

# ==================================================
# FOOTER
# ==================================================
st.divider()
st.markdown(
    "<div class='footer'>© di buat dengan cinta dan kasih sayang ❤️ </div>",
    unsafe_allow_html=True
)
