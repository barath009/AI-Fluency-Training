import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "groq")
MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

if PROVIDER == "groq":
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = os.getenv("GROQ_API_KEY")
else:
    raise ValueError("Only Groq is configured for this project.")

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)


# Private Mechatronics Lab data
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