import os
import fitz

def extract_images(pdf_path, output_folder="images"):
    """
    Extrait toutes les images du PDF et les sauvegarde dans un dossier.
    Retourne la liste des chemins d'images extraites.
    """
    os.makedirs(output_folder, exist_ok=True)
    print(f"Dossier {output_folder} créé ou déjà existant")

    
    image_paths = []

    with fitz.open(pdf_path) as doc:
        for page_num, page in enumerate(doc):
            image_list = page.get_images(full=True)
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                image_path = os.path.join(output_folder, f"page_{page_num}_img_{img_index}.{image_ext}")
                with open(image_path, "wb") as img_file:
                    img_file.write(image_bytes)
                image_paths.append(image_path)
    return image_paths