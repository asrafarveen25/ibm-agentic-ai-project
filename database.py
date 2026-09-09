import sqlite3

DATABASE = "student_memory.db"

def get_connection():
    return sqlite3.connect(DATABASE)

def init_database():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    connection.commit()
    connection.close()

def save_conversation(question, answer):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO conversations (question, answer) VALUES (?, ?)",
        (question, answer)
    )
    connection.commit()
    connection.close()

def get_previous_conversations(limit=5):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT question, answer
        FROM conversations
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))
    conversations = cursor.fetchall()
    connection.close()
    return conversations
