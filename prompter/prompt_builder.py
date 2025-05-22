class PromptBuilder:
    @staticmethod
    def build_medical_prompt(question, medical_text, visual_reports=None):
        prompt = f"""Voici un dossier médical. Analyse-le et réponds à la question suivante :

QUESTION :
{question}

DOSSIER MEDICAL :
{medical_text}
"""
        if visual_reports:
            prompt += "\nRAPPORT VISUEL :\n" + str(visual_reports)
        return prompt