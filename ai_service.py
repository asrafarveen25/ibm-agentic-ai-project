import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"

def generate_answer(prompt):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=120)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "No answer generated.")
    except requests.exceptions.ConnectionError:
        return "Ollama is not running. Please start Ollama and try again."
    except Exception as error:
        return f"AI Error: {error}"
