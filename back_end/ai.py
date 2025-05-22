import google.generativeai as genai
from PIL import Image
from pdf2image import convert_from_path
import os
import fitz  # ✅ Correct si PyMuPDF est bien installé

GOOGLE_API_KEY = "AIzaSyCj4NsQXxrr2T1ORxvXvcR52QPaJy_FYAE"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def extract_images_from_pdf(pdf_path, output_folder="images"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    images = convert_from_path(pdf_path, dpi=200)
    image_paths = []
    for i, image in enumerate(images):
        img_path = f"{output_folder}/page_{i}.jpg"
        image.save(img_path, "JPEG")
        image_paths.append(img_path)
    return image_paths


async def analyze_medical_file(pdf_path: str, prompt: str):
    try:
        text = extract_text_from_pdf(pdf_path)
        image_paths = extract_images_from_pdf(pdf_path)
        images = [Image.open(path) for path in image_paths]
        content = [prompt, text] + images
        response = model.generate_content(content)
        return response.text
    except Exception as e:
        raise Exception(f"Erreur lors de l'analyse IA : {str(e)}")