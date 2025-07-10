import streamlit as st
import requests
import time
from streamlit_lottie import st_lottie
import requests as rqs
from app.utils import render_xrd_chart, generate_pdf_report

# === SETUP ===
st.set_page_config(page_title="StructSentry", layout="wide", page_icon="🧪")

def load_lottie_local(filepath: str):
    try:
        return json.loads(Path(filepath).read_text(encoding="utf-8"))
    except Exception:
        return None

lottie_bot = load_lottie_local("animation.json")

# === CUSTOM STYLING ===
st.markdown("""
    <style>
    .title {
        font-size: 3em;
        font-weight: 900;
        text-align: center;
        color: #0B5ED7;
        margin-bottom: 0.1em;
    }
    .subtitle {
        font-size: 1.2em;
        text-align: center;
        color: #666;
        margin-bottom: 2em;
    }
    .card {
        padding: 1.2em;
        border-radius: 12px;
        margin-bottom: 1em;
        background-color: #f9f9f9;
        border: 1px solid #eee;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    }
    .section-title {
        font-size: 22px;
        font-weight: 600;
        margin-top: 2em;
        border-bottom: 1px solid #ddd;
        padding-bottom: 4px;
        color: #222;
    }
    .stButton>button {
        transition: all 0.2s ease;
        border-radius: 8px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #198754;
        color: white !important;
        transform: scale(1.03);
    }
    </style>
""", unsafe_allow_html=True)

# === HEADER ===
st.markdown('<div class="title">🧪 StructSentry</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Powered XRD Decoder & Materials Recommendation</div>', unsafe_allow_html=True)
st_lottie(lottie_bot, height=200, key="science-bot")

# === INPUT FORM ===
st.markdown("---")
st.markdown('<div class="section-title">📥 Submit XRD Pattern</div>', unsafe_allow_html=True)

pattern = st.text_area("📈 XRD Pattern (paste raw values or diffraction summary)", height=200)
notes = st.text_area("🗒️ Additional Notes (optional)", height=100)
language = st.selectbox("🌐 Output Language", ["english", "urdu", "french", "german"])

structure, recommendation = None, None

if st.button("🔍 Analyze Structure", use_container_width=True):
    with st.spinner("Analyzing XRD pattern using Gemini..."):
        time.sleep(0.8)
        response = requests.post(
            "http://localhost:8000/analyze",
            data={"xrd_pattern": pattern, "notes": notes, "language": language}
        )
        result = response.json()

        structure = result.get("structure", {})
        recommendation = result.get("recommendation", "No recommendation returned.")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<div class="section-title">🔬 Structure Analysis</div>', unsafe_allow_html=True)
            if structure:
                st.markdown(f"""<div class="card">
                <b>Structure:</b> {structure.get("structure", "N/A")}<br><br>
                <b>Confidence:</b> {structure.get("confidence", "N/A")}<br><br>
                <b>Justification:</b><br>{structure.get("justification", "N/A")}
                </div>""", unsafe_allow_html=True)
            else:
                st.warning("No structural data was returned.")

        with col2:
            st.markdown('<div class="section-title">📦 Recommendations</div>', unsafe_allow_html=True)
            st.markdown(f"""<div class="card">
            {recommendation}
            </div>""", unsafe_allow_html=True)

# === Visualization and Report ===
st.markdown("### 📉 Visualization")
if st.button("🔬 Visualize XRD Pattern"):
    render_xrd_chart()

st.markdown("### 📄 PDF Report")
if structure and recommendation:
    generate_pdf_report(structure, recommendation)

# === Feedback ===
st.markdown("---")
st.markdown("#### 🙋 Did this help?")
fb1, fb2 = st.columns(2)
with fb1:
    st.button("👍 Yes", use_container_width=True)
with fb2:
    st.button("👎 No", use_container_width=True)