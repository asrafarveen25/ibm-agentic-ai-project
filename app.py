from flask import Flask, render_template, request, redirect
import os

from database import init_database
from agents.student_support_agent import student_support_agent
from rag.document_loader import load_document
from rag.retriever import add_documents

app = Flask(__name__)
init_database()
os.makedirs("knowledge", exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question", "").strip()
    if not question:
        return redirect("/")
    answer = student_support_agent(question)
    return render_template("answer.html", question=question, answer=answer)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if not file or not file.filename:
        return "Please select a PDF file."
    if not file.filename.lower().endswith(".pdf"):
        return "Only PDF files are supported."
    path = os.path.join("knowledge", file.filename)
    file.save(path)
    text = load_document(path)
    if not text.strip():
        return "Could not extract text from the PDF."
    add_documents(text, file.filename)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
