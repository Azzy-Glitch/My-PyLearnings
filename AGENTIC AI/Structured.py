import os

from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

while True:
    query = input("You: ")

    # Exit condition
    if query.lower() in ["exit", "quit", "stop"]:
        print("Chat ended.")
        break

    completion = client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Extract the event information."},
            {"role": "user", "content": query},
        ],
        response_format=CalendarEvent,
    )

    event = completion.choices[0].message.parsed
    print(event.name)
    print(event.date)
    print(event.participants)