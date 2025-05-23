import requests

class MedicalLLM:
    def __init__(self):
      self.api_url ="https://3fed-34-125-210-40.ngrok-free.app/predict"


    def answer_question(self, context, question):
      prompt = f"Voici les données médicales :\n{context}\n\nQuestion : {question}"
      response = requests.post(self.api_url, json={"prompt": prompt})
      if response.status_code == 200:
        raw_response = response.json()["response"]
        # Nettoyage basique : on enlève tout ce qui ressemble au prompt
        cleaned = raw_response.replace(prompt, "").strip()
        return cleaned
      else:
        return f"Erreur LLM : {response.status_code} {response.text}"
