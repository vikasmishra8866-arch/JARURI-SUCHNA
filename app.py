import streamlit as st

# Page configuration
st.set_page_config(
    page_title="RC Information Portal",
    page_icon="🚗",
    layout="centered"
)

# Custom CSS for styling only the required elements
st.markdown("""
    <style>
    /* Background and overall style */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Input Box styling */
    .stTextInput input {
        border: 2px solid #2e7d32 !important;
        border-radius: 8px !important;
        padding: 10px !important;
        text-align: center;
        font-size: 18px;
    }

    /* Button styling */
    .stButton > button {
        width: 100%;
        background-color: #1a73e8 !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        height: 50px !important;
        border: none !important;
        font-size: 18px !important;
    }

    /* Red Info Box for the Hindi Text */
    .info-box {
        background-color: #ff4b4b;
        color: white;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
        margin-top: 25px;
        font-size: 1.1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 1. Vehicle Number Input Box
veh_number = st.text_input("", placeholder="VEHICLE NUMBER FILL KAREIN (Ex: UP32AB1234)")

# 2. Get RC Book Button
if st.button("GET RC BOOK"):
    if veh_number:
        st.info(f"Processing details for: {veh_number}")
    else:
        st.warning("Pehle Vehicle Number likhein.")

# 3. Important Notice in Hindi (Centre aligned and inside a box)
st.markdown("""
    <div class="info-box">
        🔔 ध्यान दें! सभी को सूचित किया जा रहा है कि 09/06/2026 से RC का चार्ज 39 रुपये कर दिया गया है।
    </div>
    """, unsafe_allow_html=True)
