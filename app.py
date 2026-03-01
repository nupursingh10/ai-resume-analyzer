from flask import Flask, render_template, request
import PyPDF2

app = Flask(__name__)

# simple skill database
skills_db = [
    "python", "java", "javascript", "sql",
    "machine learning", "html", "css",
    "react", "flask", "django"
]

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()

def analyze_resume(text):
    found_skills = []

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    score = min(len(found_skills) * 10, 100)
    missing_skills = list(set(skills_db) - set(found_skills))

    return score, found_skills, missing_skills

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["resume"]

        if file:
            text = extract_text_from_pdf(file)
            score, found, missing = analyze_resume(text)

            return render_template(
                "index.html",
                score=score,
                found=found,
                missing=missing
            )

    return render_template("index.html")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)