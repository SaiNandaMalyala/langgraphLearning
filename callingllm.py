import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

google_api_key = os.getenv('GOOGLE_API_KEY')

if google_api_key:
    print(f"Google API Key exists and begins {google_api_key[:2]}")
else:
    print("Google API Key not set (and this is optional)")

messages = [
    {"role": "system", "content": "Answer only with the question. No explanation."},
    {"role": "user", "content": "Create a challenging question to evaluate LLM intelligence."}
]

gemini = OpenAI(api_key=google_api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
model_name = "gemini-2.5-flash"

response = gemini.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content

print(answer)


