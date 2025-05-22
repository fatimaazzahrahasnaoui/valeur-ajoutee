from transformers import DonutProcessor, VisionEncoderDecoderModel
from PIL import Image
import fitz

def is_scanned_page(pdf_path, page_num=0, threshold=0.1):
    """
    Détecte si une page est scannée via la densité de texte.
    """
    with fitz.open(pdf_path) as doc:
        page = doc.load_page(page_num)
        text = page.get_text()
        return len(text.strip()) / (page.rect.width * page.rect.height) < threshold


def process_scanned_page_with_donut(image_path):
    """
    Applique Donut sur une page scannée pour OCR structuré.
    """
    processor = DonutProcessor.from_pretrained("naver-clova-ix/donut-base-finetuned-docvqa")
    model = VisionEncoderDecoderModel.from_pretrained("naver-clova-ix/donut-base-finetuned-docvqa")
    image = Image.open(image_path).convert("RGB")
    pixel_values = processor(image, return_tensors="pt").pixel_values
    decoder_input_ids = processor.tokenizer("<s_docvqa>", add_special_tokens=False, return_tensors="pt").input_ids
    outputs = model.generate(pixel_values, decoder_input_ids=decoder_input_ids, max_length=model.config.max_length)
    return processor.batch_decode(outputs, skip_special_tokens=True)[0]