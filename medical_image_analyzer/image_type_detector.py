import fitz

def detect_medical_image_type_from_comment(comment):
    if not comment:
        return "Inconnu"
    comment = comment.lower()

    if "radiographie" in comment or "radio" in comment or "x-ray" in comment:
        return "Radiographie"
    elif "irm" in comment or "mri" in comment:
        return "IRM"
    elif "echographie" in comment or "ultrasound" in comment:
        return "Échographie"
    elif "scanner" in comment or "ct scan" in comment:
        return "Scanner"
    else:
        return "Inconnu"


def get_comments_for_images(pdf_path):
    comments = []

    with fitz.open(pdf_path) as doc:
        for page_num, page in enumerate(doc):
            blocks = page.get_text("dict")["blocks"]

            # On récupère les blocs de type image (type=1) avec leur bbox
            image_blocks = [b for b in blocks if b["type"] == 1]

            # Récupérer les blocs de texte (type=0)
            text_blocks = [b for b in blocks if b["type"] == 0]

            for img_index, img_block in enumerate(image_blocks):
                image_bbox = img_block["bbox"]
                associated_text = ""

                for block in text_blocks:
                    block_bbox = block["bbox"]

                    # Si le bloc texte est proche verticalement de l'image (moins de 50 pts)
                    if abs(block_bbox[1] - image_bbox[3]) < 50:
                        lines = block.get("lines", [])
                        for line in lines:
                            for span in line["spans"]:
                                associated_text += span["text"] + " "

                comments.append({
                    "page": page_num,
                    "image_index": img_index,
                    "comment": associated_text.strip()
                })

    return comments
