from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from app.xrd_decoder import decode_xrd
from app.struct_evaluator import evaluate_structure
from app.recommender import generate_recommendations

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze/")
async def analyze(file: UploadFile = File(...), language: str = "english"):
    content = await file.read()
    decoded = decode_xrd(content.decode("utf-8"))
    evaluation = evaluate_structure({"data": decoded})
    recommendations = generate_recommendations(decoded, language)
    return {
        "decoded": decoded,
        "evaluation": evaluation,
        "recommendations": recommendations,
    }