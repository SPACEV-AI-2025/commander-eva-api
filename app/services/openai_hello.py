import os
from openai import OpenAI

# 使用新版 SDK 建構 Client（自動抓環境變數 OPENAI_API_KEY）
client = OpenAI()

def ask_gpt(message: str = "Hello, OpenAI!") -> str:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()
