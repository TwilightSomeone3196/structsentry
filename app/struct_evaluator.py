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

def analyze_structure(pattern: str, notes: str, language: str):
    prompt = ChatPromptTemplate.from_template("""
You are a materials science AI. Given the following XRD pattern data and notes, classify the material structure and recommend processing or material match.

Pattern:
{pattern}

Notes:
{notes}

Respond concisely in {language}.
""")
    chain = prompt | get_llm()
    return chain.invoke({"pattern": pattern, "notes": notes, "language": language})