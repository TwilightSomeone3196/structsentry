import os
import logging
from langchain.callbacks.tracers.langchain import LangChainTracer
from langchain_core.runnables import RunnableConfig

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Setup LangSmith tracer using environment variables
if os.getenv("LANGCHAIN_API_KEY") and os.getenv("LANGCHAIN_PROJECT"):
    tracer = LangChainTracer()
    langsmith_config: RunnableConfig = {
        "callbacks": [tracer],
        "tags": ["structsentry"],
        "metadata": {"project": os.getenv("LANGCHAIN_PROJECT")}
    }
    logger.info("LangSmith tracing is enabled.")
else:
    tracer = None
    langsmith_config = {}
    logger.warning("LangSmith is not configured. Tracing is disabled.")

# Example utility functions
def render_xrd_chart(data):
    import matplotlib.pyplot as plt
    import io
    import base64

    angles = [point["angle"] for point in data]
    intensities = [point["intensity"] for point in data]

    plt.figure()
    plt.plot(angles, intensities)
    plt.xlabel("Angle")
    plt.ylabel("Intensity")
    plt.title("XRD Diffraction Pattern")

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode("utf-8")
    plt.close()
    return img_base64

def generate_pdf_report(decoded_data, recommendations):
    from fpdf import FPDF

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="StructSentry Analysis Report", ln=1, align='C')

    pdf.ln(10)
    pdf.set_font("Arial", "B", size=12)
    pdf.cell(200, 10, txt="XRD Decoded Data:", ln=1)

    pdf.set_font("Arial", size=10)
    for item in decoded_data:
        line = f"Angle: {item['angle']}, Intensity: {item['intensity']}"
        pdf.cell(200, 8, txt=line, ln=1)

    pdf.ln(10)
    pdf.set_font("Arial", "B", size=12)
    pdf.cell(200, 10, txt="Recommendations:", ln=1)

    pdf.set_font("Arial", size=10)
    for rec in recommendations:
        pdf.cell(200, 8, txt=f"- {rec}", ln=1)

    output_path = "structsentry_report.pdf"
    pdf.output(output_path)
    return output_path