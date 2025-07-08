import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.3,
        google_api_key=os.getenv("GEMINI_API_KEY"),
        model_kwargs={"stream": False}
    )

def recommend_structures(structure: str, notes: str, language: str):
    prompt = ChatPromptTemplate.from_template("""
Given the material structure type: {structure},
provide recommended:

1. Candidate materials
2. Suggested processing (e.g., sintering, annealing, doping)
3. Common applications

Notes:
{notes}

Respond concisely in {language}, return only plain text.
""")

    chain = prompt | get_llm()
    return chain.invoke({"structure": structure, "notes": notes, "language": language})