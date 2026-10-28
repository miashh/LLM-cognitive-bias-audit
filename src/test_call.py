"""Step 1 check: confirms your API key and environment work.

Run from the project folder:  python src/test_call.py
"""
from dotenv import load_dotenv
import anthropic

load_dotenv()  # reads ANTHROPIC_API_KEY from your .env file

# Cheap, fast model for testing. Check the current model name in the
# Anthropic Console docs if you get a "model not found" error.
MODEL = "claude-haiku-5-5"

client = anthropic.Anthropic()
response = client.messages.create(
    model=MODEL,
    max_tokens=20,
    messages=[{"role": "user", "content": "Reply with the single word: ready"}],
)
print(response.content[0].text)
