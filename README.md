# StructSentry

StructSentry is an agentic AI tool that helps material engineers decode XRD patterns, analyze structure, and generate recommendations—complete with a downloadable PDF report.

---

## 🧠 Features

- Upload XRD data or try a demo sample
- Automatic structure scoring and crystallinity evaluation
- Simple language-based recommendations
- Downloadable PDF reports
- Streamlit UI + FastAPI backend
- LangChain-based agent with LangSmith tracing
- Docker & pytest support

---

## 📐 Architecture

```text
[User Upload or Demo] 
        ↓
  [Streamlit UI]
        ↓
  [FastAPI Backend]
        ↓
[XRD Decoder → Evaluator → Recommender]
        ↓
     [LangChain Tracing]