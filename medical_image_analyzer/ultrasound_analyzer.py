from ultralytics import YOLO

def analyze_ultrasound(image_path):
    # Charger un modèle YOLOv8 (pré-entraîné)
    model = YOLO("yolov8s.pt")  # ⚠️ remplacer par un modèle médical si disponible

    # Faire l'inférence sur l'image
    results = model(image_path, verbose=False)

    detected = []
    confidences = []

    # Parcourir les résultats
    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls_id = int(box.cls[0])
            label = r.names[cls_id]
            conf = float(box.conf[0])
            detected.append(label)
            confidences.append(conf)

    return {
        "detected_objects": detected,
        "confidence": confidences
    }
