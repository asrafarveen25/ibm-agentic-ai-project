import chromadb

from rag.embeddings import create_embedding
from rag.document_loader import split_text

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection(name="college_knowledge")

def add_documents(text, source):
    chunks = split_text(text)
    for index, chunk in enumerate(chunks):
        embedding = create_embedding(chunk)
        collection.add(
            ids=[f"{source}_{index}"],
            documents=[chunk],
            embeddings=[embedding],
            metadatas=[{"source": source}]
        )

def retrieve_information(question):
    if collection.count() == 0:
        return ""

    question_embedding = create_embedding(question)
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=min(4, collection.count())
    )

    documents = results.get("documents", [])
    if not documents:
        return ""

    return "\n\n".join(documents[0])
