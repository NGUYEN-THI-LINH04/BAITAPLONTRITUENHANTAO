import json
import os
from datetime import datetime
from flask import Flask, render_template, request,redirect
from src.predict import predict_image
from werkzeug.utils import secure_filename

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static/uploads")
HISTORY_FILE = os.path.join(BASE_DIR, "history.json")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ======================
# LOAD HISTORY
# ======================
def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


# ======================
# SAVE HISTORY
# ======================
def save_history(history):
    # đảm bảo JSON serializable
    for h in history:
        h["confidence"] = float(h["confidence"])

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)


# ======================
# INDEX PAGE
# ======================
@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    history = load_history()

    if request.method == "POST":
        files = request.files.getlist("images")

        for file in files:
            if file.filename == "":
                continue

            filename = secure_filename(file.filename)
            path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(path)

            label, confidence = predict_image(path)

            item = {
                "filename": filename,
                "label": label,
                "confidence": round(float(confidence), 2),
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            results.append(item)
            history.append(item)



        save_history(history)

    # 🔥 TRUYỀN CẢ RESULTS + HISTORY
    return render_template(
        "index.html",
        results=results,
        history=history
    )


# ======================
# HISTORY PAGE
# ======================
@app.route("/history")
def history_page():
    history = load_history()
    return render_template("history.html", history=history)

@app.route("/delete/<int:index>", methods=["POST"])
def delete_history(index):
    history = load_history()

    if 0 <= index < len(history):
        # xóa ảnh trong uploads
        filename = history[index]["filename"]
        img_path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.exists(img_path):
            os.remove(img_path)

        # xóa trong history
        history.pop(index)
        save_history(history)

    return redirect("/history")


if __name__ == "__main__":
    app.run(debug=True)
