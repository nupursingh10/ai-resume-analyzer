from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# ===============================
# Home Route (Frontend)
# ===============================
@app.route("/")
def home():
    return render_template("index.html")


# ===============================
# Analyze Route (POST)
# ===============================
@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        # check if file uploaded
        if "resume" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["resume"]

        if file.filename == "":
            return jsonify({"error": "Empty filename"}), 400

        # 🔹 TEMP: read file text (we will add AI next)
        resume_text = file.read().decode("utf-8", errors="ignore")

        # 🔹 Dummy response for now
        return jsonify({
            "status": "success",
            "message": "Resume received successfully",
            "length": len(resume_text)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ===============================
# Health Check (optional but pro)
# ===============================
@app.route("/health")
def health():
    return {"status": "ok"}


# ===============================
# Local Run (Render ignores this)
# ===============================
if __name__ == "__main__":
    app.run(debug=True)