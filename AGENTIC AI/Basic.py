from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env")

client = Groq(api_key=api_key)

print("AI Chat Started (type 'exit' to stop)\n")

while True:
    query = input("You: ")

    # Exit condition
    if query.lower() in ["exit", "quit", "stop"]:
        print("Chat ended.")
        break

    try:
        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "user", "content": query}
            ],
            temperature=1,
            max_completion_tokens=800,
            top_p=1,
            stream=True
        )

        print("AI: ", end="")

        for chunk in completion:
            print(chunk.choices[0].delta.content or "", end="")

        print("\n")

    except Exception as e:
        print("\nError:", e)