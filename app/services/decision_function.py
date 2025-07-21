import os, json
from datetime import datetime
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def write_launch_json(status: str, reason: str):
    data = {
        "status": status,
        "reason": reason,
        "timestamp": datetime.now().astimezone().isoformat()
    }
    os.makedirs("data", exist_ok=True)
    with open("data/launch.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return data

def call_launch_decision(user_message: str):
    with open("data/b612_sensors.json", "r") as f:
        sensors = json.load(f)[0]
    with open("data/earth_weather_logs.json", "r") as f:
        weather = json.load(f)[-1]
    with open("data/vision_log.jsonl", "r") as f:
        vision = json.loads(list(f)[-1])

    system_prompt = f"""
你是 Commander EVA，一位執行太空任務的智慧助理。請根據以下環境資訊協助分析是否適合返航。
- 感測器資料：{sensors}
- 地球氣象（地點：{weather["location"]}）：{weather["weather"]}
- 視覺分析結果：{vision}
請根據上述資訊回答使用者的提問。
"""

    functions = [{
        "name": "write_launch_json",
        "description": "決定是否返航，並將結果寫入 launch.json",
        "parameters": {
            "type": "object",
            "properties": {
                "status": {
                    "type": "string",
                    "enum": ["launch", "standby"],
                    "description": "是否返航"
                },
                "reason": {
                    "type": "string",
                    "description": "判斷依據"
                }
            },
            "required": ["status", "reason"]
        }
    }]

    response = client.chat.completions.create(
        model="gpt-4-0613",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        functions=functions,
        function_call="auto"
    )

    choice = response.choices[0]
    if choice.finish_reason == "function_call":
        args = json.loads(choice.message.function_call.arguments)
        result = write_launch_json(**args)
        return result
    else:
        return {"status": "unknown", "reason": "無法判斷", "timestamp": datetime.now().isoformat()}
