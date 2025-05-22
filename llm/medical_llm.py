from transformers import pipeline

class MedicalLLM:
    def __init__(self, model_name ="deepset/bert-base-cased-squad2"):  
        self.qa_pipeline = pipeline("question-answering", model=model_name)

    def answer_question(self, context, question):
        result = self.qa_pipeline(question=question, context=context)
        return result["answer"]
