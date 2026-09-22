import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "groq")

if PROVIDER == "groq":
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

elif PROVIDER == "ollama":
    BASE_URL = "http://localhost:11434/v1"
    API_KEY = "ollama"
    MODEL = os.getenv("MODEL", "qwen2.5:1.5b")

else:
    raise ValueError("Unsupported provider")

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)


# PRIVATE DATA
EQUIPMENT = {
    "ROB01": {
        "name": "Robotic Arm",
        "price": 200000,
        "status": "Available"
    },
    "CNC01": {
        "name": "CNC Machine",
        "price": 450000,
        "status": "In Use"
    },
    "PLC01": {
        "name": "PLC Trainer",
        "price": 75000,
        "status": "Maintenance"
    },
    "3DPR01": {
        "name": "3D Printer",
        "price": 85000,
        "status": "Available"
    }
}