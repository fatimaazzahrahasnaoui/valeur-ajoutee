import os
import uuid  # ⬅️ Import ajouté ici
from fastapi import UploadFile

UPLOAD_DIR = "uploads"

async def save_upload(file: UploadFile) -> str:
    file_id = str(uuid.uuid4())
    file_extension = os.path.splitext(file.filename)[-1]
    file_name = f"{file_id}{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, file_name)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return file_path