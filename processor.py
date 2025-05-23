from pdf_extractor.text_extractor import extract_text
from pdf_extractor.image_extractor import extract_images
from pdf_extractor.scanned_page_processor import is_scanned_page, process_scanned_page_with_donut
from cleaner.text_cleaner import clean_text
from prompter.prompt_builder import PromptBuilder
from llm.medical_llm import MedicalLLM
from medical_image_analyzer.image_type_detector import get_comments_for_images, detect_medical_image_type_from_comment
from medical_image_analyzer.radiograph_analyzer import analyze_chest_xray
from medical_image_analyzer.ultrasound_analyzer import analyze_ultrasound
from response_formatter.json_formatter import format_response_as_json
import os
import sys

# Ajouter le chemin vers nnUNet
sys.path.append(os.path.abspath("medical_image_analyzer/nnUNet"))

def process_medical_dossier(pdf_path, user_question):
    # 1. Extraction du texte brut
    raw_text = extract_text(pdf_path)
    cleaned_text = clean_text(raw_text)

    # 2. Extraction des images
    image_paths = extract_images(pdf_path)

    # 3. Détection du type d'image via les commentaires
    image_analysis = get_comments_for_images(pdf_path)
    visual_reports = []

    for analysis in image_analysis:
        image_index = analysis["image_index"]
        image_type = detect_medical_image_type_from_comment(analysis["comment"])
        image_path = image_paths[image_index] if image_index < len(image_paths) else None

        report = {
            "page": analysis["page"],
            "image_index": image_index,
            "type": image_type,
            "description": analysis["comment"]
        }

        # 4. Analyse spécifique selon le type d’image
        if image_path:
            try:
                if image_type == "Radiographie":
                    xray_report = analyze_chest_xray(image_path)
                    report["analysis"] = xray_report
               
                elif image_type == "Échographie":
                    us_report = analyze_ultrasound(image_path)
                    report["analysis"] = us_report
            except Exception as e:
                report["analysis_error"] = str(e)

        visual_reports.append(report)

    # 5. Construction du prompt
    prompt = PromptBuilder.build_medical_prompt(user_question, cleaned_text, visual_reports)

    # 6. Appel au LLM
    llm = MedicalLLM()  # Maintenant utilise l’API Colab
    response = llm.answer_question(cleaned_text, user_question)


    # 7. Formatage final
    final_response = {
    "texte_nettoye": cleaned_text,
    "reponse": format_response_as_json(response)  # ou juste `response` si déjà lisible
}
    print(final_response)
    return final_response



