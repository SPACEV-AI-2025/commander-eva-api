from fastapi import APIRouter, Query
from app.services.openai_hello import ask_gpt

router = APIRouter()

@router.get("/hello")
def gpt_hello(msg: str = Query("Hello, EVA")):
    try:
        answer = ask_gpt(msg)
        return {"question": msg, "answer": answer}
    except Exception as e:
        return {"error": str(e)}


# app/routes/gai.py
from fastapi import Request
from pydantic import BaseModel
import os
import json
from openai import OpenAI

router = APIRouter()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 輸入模型
class ChatRequest(BaseModel):
    message: str

# app/routes/gai.py
from fastapi import APIRouter, Request
from pydantic import BaseModel
import os
import json
from openai import OpenAI

router = APIRouter()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat_with_commander(req: ChatRequest):
    with open("data/b612_sensors.json", "r") as f:
        sensors = json.load(f)[0]

    with open("data/earth_weather_logs.json", "r") as f:
        weather = json.load(f)[-1]

    with open("data/vision_log.jsonl", "r") as f:
        last_line = list(f)[-1]
        vision = json.loads(last_line)

    with open("data/launch_window.json", "r") as f:
        launch = json.load(f)

    system_prompt = f"""
你是 Commander EVA，一位執行太空任務的智慧助理。請根據以下環境資訊協助分析是否適合返航：
- 感測器資料（b612）：{sensors}
- 地球氣象（地點：{weather["location"]}）：{weather["weather"]}
- 視覺分析結果：{vision}
- 發射視窗與太空氣象資料：{launch}

請根據上述資訊，盡可能給出準確、專業的建議。
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": req.message}
        ]
    )

    return {"reply": response.choices[0].message.content}
