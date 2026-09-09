# AI Student Support Assistant

An AI-powered student support assistant that answers college-related questions using regulations, syllabus, FAQs and notices.

## Key Capabilities

- Retrieval Augmented Generation (RAG)
- AI Agent
- Tool Usage
- Conversation Memory
- College Document Search
- PDF Upload
- Student-friendly Answers
- Local LLM using Ollama

## Architecture

Student
  |
  v
Web Interface
  |
  v
Student Support Agent
  |
  +------ RAG
  |
  +------ Tools
  |
  +------ Memory
  |
  v
Ollama LLM
  |
  v
Student Answer

## Technologies

Python, Flask, Ollama, ChromaDB, Sentence Transformers, SQLite, HTML, CSS

## Installation

Create a virtual environment:

    python -m venv venv

Activate it on Windows:

    venv\Scripts\activate

Install packages:

    pip install -r requirements.txt

## Ollama

Install Ollama and download the model:

    ollama pull llama3.2

Start Ollama:

    ollama run llama3.2

## Run

    python app.py

Open:

    http://127.0.0.1:5000

## Usage

1. Upload college PDF documents such as regulations, syllabus, FAQs or notices.
2. The system extracts the text.
3. Text is divided into chunks.
4. Sentence Transformer creates embeddings.
5. ChromaDB stores the document information.
6. Student asks a question.
7. Relevant information is retrieved.
8. Previous conversations are retrieved from SQLite memory.
9. Tools provide additional information when needed.
10. Ollama generates the final answer.
11. The conversation is saved to memory.

## Example Questions

- What is the minimum attendance requirement?
- What are the examination regulations?
- What subjects are included in semester 5?
- What are the rules for internal marks?
- What documents are required?

## Important

Do not upload private college documents, generated databases, ChromaDB data, virtual environments, or API keys to GitHub.
