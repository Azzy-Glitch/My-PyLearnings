import json
import os

import requests
from openai import OpenAI
from pydantic import BaseModel, Field

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_weather(latitude, longitude):
    """This is a publically available API that returns the weather for a given location."""
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    )
    data = response.json()
    return data["current"]

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current temperature for provided coordinates in celsius.",
            "parameters": {
                "type": "object",
                "properties": {
                    "latitude": {"type": "number"},
                    "longitude": {"type": "number"},
                },
                "required": ["latitude", "longitude"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    }
]


def call_function(name, args):
    if name == "get_weather":
        return get_weather(**args)


class WeatherResponse(BaseModel):
    temperature: float = Field(
        description="The current temperature in celsius for the given location."
    )
    response: str = Field(
        description="A natural language response to the user's question."
    )

while True:
    Query = input("ENTER THE NAME OF THE CITY: ")

    if Query.lower() in ["exit", "quit", "stop"]:
        print("Chat ended.")
        break

    system_prompt = "You are a helpful weather assistant."

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"What's the weather like in {Query} today?"},
   ]

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
        response_format={"type": "json_object"},
    )
    
    assistant_message = completion.choices[0].message
    messages.append(assistant_message)

    for tool_call in assistant_message.tool_calls or []:
        name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)
        result = call_function(name, args)
        messages.append(
            {"role": "tool", "tool_call_id": tool_call.id, "content": json.dumps(result)}
        )

    completion_2 = client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=messages,
        tools=tools,
        response_format=WeatherResponse,
    )

    final_response = completion_2.choices[0].message.parsed
    print(final_response.temperature)
    print(final_response.response)