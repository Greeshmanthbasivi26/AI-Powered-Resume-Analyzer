
# ... keep the rest of your code the same
import os
from flask import Flask, render_template, request
# ...
import fitz  # PyMuPDF
import docx
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)

# Function to extract text from PDF
def extract_text_from_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

# Function to extract text from DOCX
def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

# Function to preprocess text using spaCy
def preprocess_text(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct and not token.is_space]
    return " ".join(tokens)

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    if request.method == "POST":
        # Get uploaded resume file
        resume_file = request.files.get("resume")
        # Get job description text
        job_description = request.form.get("job_description")

        if resume_file and job_description:
            # Extract text based on file type
            if resume_file.filename.endswith(".pdf"):
                resume_text = extract_text_from_pdf(resume_file)
            elif resume_file.filename.endswith(".docx"):
                resume_text = extract_text_from_docx(resume_file)
            else:
                return "Unsupported file type", 400

            # Preprocess the texts
            processed_resume = preprocess_text(resume_text)
            processed_jd = preprocess_text(job_description)

            # Vectorize the texts using TF-IDF
            vectorizer = TfidfVectorizer()
            tfidf_matrix = vectorizer.fit_transform([processed_resume, processed_jd])

            # Calculate Cosine Similarity
            cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
            match_score = round(cosine_sim * 100)

            # Extract keywords for analysis
            resume_keywords = set(processed_resume.split())
            jd_keywords = set(processed_jd.split())

            matched_keywords = list(resume_keywords.intersection(jd_keywords))
            missing_keywords = list(jd_keywords.difference(resume_keywords))

            results = {
                "score": match_score,
                "matched_keywords": matched_keywords,
                "missing_keywords": missing_keywords
            }

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)