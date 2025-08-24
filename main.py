import os
from flask import Flask, render_template, request
import PyPDF2
import pyttsx3


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
AUDIO_FOLDER = "static/audio"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "pdf" not in request.files:
            return "No file uploaded", 400
        file = request.files["pdf"]
        if file.filename == "":
            return "No file selected", 400

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        content = ""
        with open(filepath, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    content += text + "\n"
        audio_file = os.path.splitext(file.filename)[0] + ".mp3"
        audio_path = os.path.join(AUDIO_FOLDER, audio_file)

        engine = pyttsx3.init()
        engine.save_to_file(content, audio_path)
        engine.runAndWait()

        return render_template("uploaded.html",text = content,name = file.filename,audio_file=audio_file)

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
