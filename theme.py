import streamlit as st

def apply_theme():
    st.markdown("""
    <style>
    /* ===== Global Background ===== */
    .stApp {
        background: linear-gradient(135deg, #0F2027, #203A43, #2C5364);
        color: #EAEAEA;
    }

    /* ===== Title ===== */
    h1 {
        font-family: 'Trebuchet MS', 'Comic Sans MS', sans-serif;
        color: #EAF6FF;
    }

    /* ===== Subtitle ===== */
    .subtitle {
        text-align: center;
        color: #A8DADC;
        font-size: 16px;
    }

    /* ===== Expander ===== */
    details {
        background-color: #1B262C;
        border-radius: 18px;
        padding: 12px;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.4);
    }

    /* ===== Button ===== */
    .stButton > button {
        background: linear-gradient(135deg, #56CCF2, #2F80ED);
        color: #000;
        border-radius: 30px;
        padding: 14px;
        font-size: 16px;
        font-weight: bold;
        border: none;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #6EE7F9, #3B82F6);
        color: #000;
    }

    /* ===== Diagnosis Box ===== */
    .diagnosis-box {
        background-color: #0F5132;
        border-radius: 20px;
        padding: 16px;
        margin-top: 10px;
        border-left: 6px solid #2ECC71;
    }

    /* ===== Indication Box ===== */
    .indication-box {
        background-color: #3A3A00;
        border-radius: 20px;
        padding: 16px;
        margin-top: 10px;
        border-left: 6px solid #F1C40F;
    }

    /* ===== Footer ===== */
    .footer {
        text-align: center;
        color: #B0BEC5;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)
