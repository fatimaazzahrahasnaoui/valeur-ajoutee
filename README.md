## 🧠 Présentation du Projet(partie mn lprojet )

Ce projet a pour objectif d’**extraire, analyser et interpréter automatiquement les contenus médicaux présents dans des dossiers PDF**, notamment :

- Le texte médical brut
- Les images intégrées (radiographies, IRM, échographies…)
- Les pages scannées avec OCR structuré (via **Donut**)

Le système est conçu selon une **architecture modulaire et sophistiquée**, permettant une évolutivité facile et une maintenance claire.

---

## 📦 Structure du Projet

```
medical_ocr_project/
│
├── pdf_extractor/                 # Extraction du contenu PDF
│   ├── text_extractor.py          # Extraction du texte brut
│   ├── image_extractor.py         # Extraction des images intégrées
│   └── scanned_page_processor.py  # OCR avec Donut sur pages scannées
│
├── medical_image_analyzer/        # Analyse des images médicales visuelles
│   ├── image_type_detector.py     # Détecte le type d'image via les commentaires du PDF
│   ├── radiograph_analyzer.py     # Analyse des radiographies (ex: CheXNeXt)
│   ├── mri_segmenter.py           # IRM cérébrale (ex: U-Net / nnUNet)
│   └── ultrasound_analyzer.py     # Échographies (ex: YOLOv8)
│
├── cleaner/                       # Nettoyage léger du texte extrait
│   └── text_cleaner.py
│
├── prompter/                      # Construction du prompt pour LLM
│   └── prompt_builder.py
│
├── llm/                           # Interface avec un LLM spécialisé
│   └── medical_llm.py
│
├── response_formatter/            # Formatte la réponse finale
│   └── json_formatter.py
│
├── main.py                        # Orchestrateur principal
└── requirements.txt               # Dépendances Python
```

---

## 🚀 Fonctionnalités Principales

### 1. 🔍 Extraction Multi-Niveaux du Contenu PDF
- Extraction du texte brut avec `PyMuPDF` ou `pdfplumber`
- Extraction des images intégrées
- Détection et traitement des pages scannées avec **Donut (HuggingFace)**

### 2. 🧹 Nettoyage Léger du Texte
- Suppression des espaces multiples
- Correction basique des caractères spéciaux
- Préparation pour utilisation par un LLM

### 3. 💬 Construction du Prompt Structuré
- Génération d’un prompt combinant :
  - La question utilisateur
  - Le texte nettoyé
  - Des rapports visuels (si applicable)

### 4. 🧠 Interaction avec LLM Finetuné Médical
- Utilisation d’un modèle spécialisé en médecine (ex: Dr-BERT)
- Réponse intelligente à la question posée

### 5. 🩻 Analyse des Images Médicales (Optionnelle mais intégrée)
- Détection du type d’image (radio / IRM / échographie) via les commentaires du PDF
- Analyse spécifique selon le type d’image :
  - Radiographies : CheXNeXt
  - IRM : nnUNet
  - Échographies : YOLOv8

### 6. 📥 Format Final de la Réponse
- Retour au format JSON structuré
- Facilement exploitable dans une interface ou API

---

## 🛠️ Dépendances Requises

```bash
pip install PyMuPDF pdfplumber transformers torch pillow regex chexpert nnunet ultralytics
```

> ⚠️ Note : Certains modules comme `nnunet` ou `chexpert` nécessitent des installations supplémentaires ou Docker.

---

## 🧪 Exemple d'Utilisation

```bash
python main.py
```

Le script analyse le fichier `dossier.pdf` et répond à la question :

> "Quels sont mes antécédents médicaux ?"

La réponse est retournée sous forme de JSON structuré :

```json
{
  "reponse": "Vous souffrez d’une hypertension chronique...",
  "metadata": {
    "prompt_used": "..."
  }
}
```

---

## 📌 Technologies Utilisées

| Module | Outils |
|--------|--------|
| PDF Extraction | `PyMuPDF`, `pdfplumber` |
| OCR Structuré | `Donut (HuggingFace)` |
| Nettoyage du texte | `regex` |
| Analyse des images | `CheXNeXt`, `nnUNet`, `YOLOv8` |
| LLM Médical | `Dr-BERT`, `transformers` |
| Format de sortie | `JSON` |

---

## 📁 Organisation des Modules

| Module | Rôle |
|--------|------|
| `pdf_extractor/` | Extraction du texte et des images |
| `cleaner/` | Nettoyage léger du texte |
| `prompter/` | Génération du prompt pour LLM |
| `llm/` | Appel au LLM spécialisé |
| `medical_image_analyzer/` | Analyse des images médicales |
| `response_formatter/` | Formatage final de la réponse |



## ✅ Recommandations

- Utilisez un environnement virtuel (`venv` ou `conda`)
- Activez les longs chemins Windows si nécessaire
