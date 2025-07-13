# StructSentry

StructSentry is an agentic AI tool for material engineers that analyzes XRD data, decodes structures, and recommends material modifications.

---

## 🚀 Features

- Streamlit UI for easy uploads and visualization
- FastAPI backend for inference
- LangChain agent for structure reasoning
- PDF reporting and visualization
- Structure recommendation engine
- LangSmith observability
- Docker-based deployment
- Pytest test suite

---

## 📊 Architecture Diagram

```plaintext
+-------------+        +------------+        +-----------------+
|  Streamlit  | <----> | FastAPI    | <----> | LangChain Agent |
|  Dashboard  |        | Backend    |        | & Tools         |
+-------------+        +------------+        +-----------------+
     |                       |                        |
     v                       v                        v
[User Input]         [XRD Decoder]        [Struct Evaluator & Recommender]
     |                       |                        |
     +------> [PDF Generator, Logging, Tracing] <-----+
```

---

## 🤖 Agent Prompt Design

The LangChain agent receives:

- Decoded XRD pattern (angles, intensities)
- Inferred structure data
- User-selected material goals

It uses internal reasoning to recommend material changes and justify them based on typical crystallographic patterns.

---

## 🧪 Run Locally

```bash
git clone https://github.com/yourname/structsentry.git
cd structsentry
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
streamlit run ui/dashboard.py
```

---

## 🐳 Run with Docker

```bash
docker-compose up --build
```

---

## 🧪 Run Tests

```bash
pytest tests/
```

---

## 📦 .env Setup

Create a `.env` file:

```env
LANGCHAIN_API_KEY=your_key
LANGCHAIN_PROJECT=StructSentry
```

---

## 📹 Demo & Deployment

- Demo video: [Link Placeholder]
- Live App: [Link Placeholder]

---

## 📄 License

MIT License.