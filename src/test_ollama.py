"""Quick check that Ollama is running and a model answers.

    python src/test_ollama.py llama3.2:3b
"""
import sys

import ollama

model = sys.argv[1] if len(sys.argv) > 1 else "llama3.2:3b"
reply = ollama.chat(model=model, messages=[{"role": "user",
                                            "content": "Reply with the single word: ready"}])
print(reply["message"]["content"])
