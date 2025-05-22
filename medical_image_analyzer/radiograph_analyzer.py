# medical_image_analyzer/radiograph_analyzer.py

from torchvision import models, transforms
from PIL import Image
import torch

# Les 14 maladies possibles dans CheXpert
labels = [
    "No Finding", "Enlarged Cardiomediastinum", "Cardiomegaly", "Lung Opacity",
    "Lung Lesion", "Edema", "Consolidation", "Pneumonia", "Atelectasis",
    "Pneumothorax", "Pleural Effusion", "Pleural Other", "Fracture", "Support Devices"
]

def analyze_chest_xray(image_path):
    # Charger l'image
    image = Image.open(image_path).convert("RGB")

    # Prétraitement pour DenseNet121
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],  # Standard ImageNet
            std=[0.229, 0.224, 0.225]
        )
    ])
    image = transform(image).unsqueeze(0)  # Ajoute une dimension batch

    # Charger le modèle DenseNet121
    model = models.densenet121(pretrained=True)
    model.classifier = torch.nn.Linear(1024, 14)  # Adapter à CheXpert
    model.eval()  # Mode prédiction

    # ⚠️ Ce modèle est pré-entraîné sur ImageNet, PAS sur CheXpert
    # Pour de vraies prédictions médicales, tu dois charger un modèle entraîné sur CheXpert

    with torch.no_grad():
        outputs = model(image)
        probs = torch.sigmoid(outputs[0])  # Activation pour classification multi-label
        index = torch.argmax(probs).item()  # Trouve la maladie la plus probable

    return {
        "pathology": labels[index],
        "confidence": float(probs[index]),
        "type": "Chest X-Ray"
    }
