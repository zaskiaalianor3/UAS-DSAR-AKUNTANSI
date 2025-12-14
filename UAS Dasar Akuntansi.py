
import streamlit as st
import pandas as pd

# ===== CSS SEDERHANA =====
st.markdown(
    """
    <style>
    body {
        background-color: #f5f7fa;
    }
    .main {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .stButton>button {
        background-color: #2ecc71;
        color: white;
        border-radius: 8px;
        padding: 8px 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===== JUDUL =====
st.title("📊 Aplikasi Akuntansi Sederhana")
st.write("Input transaksi dan lihat laporan secara otomatis")

# ===== INISIALISASI DATA =====
if "data" not in st.session_state:
    st.session_state.data = []

# ===== FORM INPUT =====
st.subheader("➕ Input Transaksi")

with st.form("form_transaksi"):
    tanggal = st.date_input("Tanggal")
    akun = st.text_input("Nama Akun")
    debit = st.number_input("Debit", min_value=0.0, step=1000.0)
    kredit = st.number_input("Kredit", min_value=0.0, step=1000.0)
    submit = st.form_submit_button("Simpan Transaksi")

    if submit:
        st.session_state.data.append({
            "Tanggal": tanggal,
            "Akun": akun,
            "Debit": debit,
            "Kredit": kredit
        })
        st.success("Transaksi berhasil disimpan")

# ===== TABEL TRANSAKSI =====
st.subheader("📋 Data Transaksi")

df = pd.DataFrame(st.session_state.data)
if not df.empty:
    st.dataframe(df, use_container_width=True)
else:
    st.info("Belum ada transaksi")

# ===== LAPORAN LABA RUGI =====
st.subheader("📈 Laporan Laba Rugi")
if not df.empty:
    total_debit = df["Debit"].sum()
    total_kredit = df["Kredit"].sum()
    laba = total_kredit - total_debit

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Debit", f"Rp {total_debit:,.0f}")
    col2.metric("Total Kredit", f"Rp {total_kredit:,.0f}")
    col3.metric("Laba / Rugi", f"Rp {laba:,.0f}")
else:
    st.info("Laporan belum tersedia")

# ===== FOOTER =====
st.markdown("---")
st.markdown("<center>© 2025 Aplikasi Akuntansi Sederhana</center>", unsafe_allow_html=True)
