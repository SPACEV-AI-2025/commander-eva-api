import json
import requests
from pathlib import Path

API_URL = "http://127.0.0.1:9001/api/sensors/upload"
DATA_FILE = Path("data/b612_sensors.json")

if not DATA_FILE.exists():
    raise FileNotFoundError(f"找不到假資料檔案：{DATA_FILE}")

with open(DATA_FILE) as f:
    sensor_data = json.load(f)

payload = {
    "data": sensor_data
}

response = requests.post(API_URL, json=payload)

if response.status_code == 200:
    print("✅ 假資料成功上傳至 API")
    print(response.json())
else:
    print(f"❌ 上傳失敗，狀態碼：{response.status_code}")
    print(response.text)
