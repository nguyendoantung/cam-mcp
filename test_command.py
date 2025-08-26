import os
from pprint import pprint

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

BASE_URL = "https://mkp-api.fptcloud.com"
API_KEY = os.getenv("AI_AGENT_TOKEN", "")
MODEL_NAME = "Qwen3-32B"


# response = client.chat.completions.create(
#     model=MODEL_NAME,
#     messages=[
#         {
#             "role": "user",
#             "context": "no thinking to output",
#             "content": "what is your name?",
#         },
#     ],
#     temperature=0.7,  # Controls randomness: 0.0 = deterministic, 1.0 = creative
#     top_p=0.9,  # Nucleus sampling: consider tokens with top_p probability mass
#     frequency_penalty=0.0,  # -2.0 to 2.0, positive values penalize repetition
#     presence_penalty=0.0,  # -2.0 to 2.0, positive values penalize talking about the same topics
#     stream=False,
#     max_completion_tokens=100,
# )

# pprint(response.to_dict())

# client = OpenAI()
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
# client = OpenAI(api_key=API_KEY) 

resp = client.responses.create(
    model=MODEL_NAME,
    tools=[
        {
            "type": "mcp",
            "server_label": "weather",
            "server_description": "A MCP Server for weather info",
            "server_url": "http://127.0.0.1:8000",
            "require_approval": "never",
        },
    ],
    input="What's the weather like in Ha Noi?",
)

print(resp.text)
