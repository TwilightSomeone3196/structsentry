import streamlit as st
from app.utils import render_xrd_chart, generate_pdf_report
from app.xrd_decoder import decode_xrd
from app.struct_evaluator import evaluate_structure
from app.recommender import generate_recommendations
import io

st.set_page_config(page_title="StructSentry", layout="centered")

st.title("🔬 StructSentry: XRD Structure Decoder & Recommender")

st.markdown("Upload your XRD pattern file and get recommendations based on structural evaluation.")

uploaded_file = st.file_uploader("Upload your XRD data file", type=["txt", "csv"])
language_options = ["english", "urdu", "french", "german"]
selected_language = st.session_state.get("language", "english")
language_index = language_options.index(selected_language) if selected_language in language_options else 0
language = st.selectbox("Select output language", language_options, index=language_index)

def display_outputs(data, language, report_name):
    st.subheader("📈 XRD Chart")
    chart_base64 = render_xrd_chart(data)
    st.image(f"data:image/png;base64,{chart_base64}", use_container_width=True)

    st.subheader("🔍 Structural Evaluation")
    evaluation = evaluate_structure({"data": data})
    st.markdown(f"**Score:** {evaluation['score']}")
    st.markdown(f"**Crystalline:** {'Yes' if evaluation['crystalline'] else 'No'}")
    st.markdown(f"**Insights:** {evaluation['insights']}")

    st.subheader("💡 Recommendations")
    recommendations = generate_recommendations(data, language)
    for rec in recommendations:
        st.markdown(f"- {rec}")

    # Generate PDF in memory
    if st.button("📄 Generate Report", key=report_name):
        from fpdf import FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="StructSentry Analysis Report", ln=1, align='C')

        pdf.ln(10)
        pdf.set_font("Arial", "B", size=12)
        pdf.cell(200, 10, txt="XRD Decoded Data:", ln=1)
        pdf.set_font("Arial", size=10)
        for item in data:
            pdf.cell(200, 8, txt=f"Angle: {item['angle']}, Intensity: {item['intensity']}", ln=1)

        pdf.ln(10)
        pdf.set_font("Arial", "B", size=12)
        pdf.cell(200, 10, txt="Recommendations:", ln=1)
        pdf.set_font("Arial", size=10)
        for rec in recommendations:
            pdf.cell(200, 8, txt=f"- {rec}", ln=1)

        buffer = io.BytesIO()
        pdf.output(buffer)
        buffer.seek(0)

        st.download_button(
            label="⬇️ Download Report",
            data=buffer,
            file_name=report_name,
            mime="application/pdf"
        )

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    content = uploaded_file.read().decode("utf-8")
    decoded = decode_xrd(content)
    display_outputs(decoded, language, "structsentry_report.pdf")

st.markdown("---")
if st.button("🧪 Try Demo Mode"):
    demo_data = [
        {"angle": 10, "intensity": 20},
        {"angle": 15, "intensity": 130},
        {"angle": 20, "intensity": 80},
        {"angle": 25, "intensity": 300},
        {"angle": 30, "intensity": 40},
        {"angle": 35, "intensity": 260},
        {"angle": 40, "intensity": 20},
        {"angle": 45, "intensity": 220},
        {"angle": 50, "intensity": 10},
    ]
    display_outputs(demo_data, language, "structsentry_demo_report.pdf")