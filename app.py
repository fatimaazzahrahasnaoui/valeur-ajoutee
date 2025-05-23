from flask import Flask, request, render_template, jsonify
import os
from werkzeug.utils import secure_filename
from processor import process_medical_dossier
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Vérifie l'extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    if "pdf_file" not in request.files:
        return "Aucun fichier PDF envoyé", 400
    file = request.files["pdf_file"]
    question = request.form.get("question", "")

    if file.filename == "" or not allowed_file(file.filename):
        return "Fichier non valide", 400

    # Sauvegarde du fichier
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(file_path)

    try:
        result =process_medical_dossier(file_path, question)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
