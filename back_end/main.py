from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import os
import uuid

from upload import save_upload
from ai import analyze_medical_file

app = FastAPI()

# Autoriser React en local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/analyze")
async def analyze_file(
    file: UploadFile = File(...),
    prompt: str = "Résume mon état de santé à partir de ce dossier."
):
    print(f"🟩 Prompt reçu par FastAPI : {prompt}")
    try:
        file_path = await save_upload(file)
        result = await analyze_medical_file(file_path, prompt)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))