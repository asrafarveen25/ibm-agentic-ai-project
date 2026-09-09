from ai_service import generate_answer
from rag.retriever import retrieve_information
from database import save_conversation, get_previous_conversations
from tools.college_tools import get_current_date, get_college_help

def student_support_agent(question):
    context = retrieve_information(question)

    previous = get_previous_conversations(5)
    memory_text = ""
    for old_question, old_answer in previous:
        memory_text += f"Previous Question: {old_question}\n"
        memory_text += f"Previous Answer: {old_answer}\n\n"

    current_date = get_current_date()
    support_services = get_college_help()

    prompt = f"""
You are an AI Student Support Assistant.

Your job is to help college students with academic and college-related questions.

Use the available college documents as the primary source of information.
Do not invent college rules. If the answer is not present in the documents,
clearly say that it was not found in the available college documents.

COLLEGE DOCUMENT INFORMATION:
{context if context else "No relevant document information was found."}

PREVIOUS CONVERSATION MEMORY:
{memory_text if memory_text else "No previous conversation available."}

CURRENT DATE:
{current_date}

AVAILABLE COLLEGE SERVICES:
{support_services}

STUDENT QUESTION:
{question}

Instructions:
1. Answer clearly and in simple student-friendly language.
2. Use the exact rule when available.
3. Do not make up regulations.
4. If the document does not contain the answer, say so.
5. Use previous conversation context when useful.
6. Keep the answer concise but useful.
"""
    answer = generate_answer(prompt)
    save_conversation(question, answer)
    return answer
