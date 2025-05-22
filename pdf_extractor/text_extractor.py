import fitz

def extract_text(pdf_path):
    with fitz.open(pdf_path) as doc:
        # Corrigé : utiliser ''.join() au lieu de '","join()'
        text = "\n".join(page.get_text() for page in doc)
    return text
9