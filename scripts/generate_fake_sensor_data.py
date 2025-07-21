import json
import random
import requests
from datetime import datetime, timedelta

SERVER_URL = "http://localhost:9001/api/sensors/upload"  # 改成你的實際 URL

def generate_sensor_data_entry(ts):
    return {
        "timestamp": ts.isoformat(),
        "wind_speed": round(random.uniform(10, 100), 2),
        "radiation_level": round(random.uniform(0.5, 5.0), 2),
        "temperature": round(random.uniform(-150, -20), 1),
        "image_id": f"img_{random.randint(1000, 9999)}.jpg"
    }

def generate_fake_dataset(num_entries=10):
    now = datetime.utcnow()
    return [generate_sensor_data_entry(now - timedelta(hours=i)) for i in range(num_entries)]

if __name__ == "__main__":
    data = generate_fake_dataset(24)
    try:
        res = requests.post(SERVER_URL, json=data)
        res.raise_for_status()
        print("✅ Server 回應:", res.json())
    except Exception as e:
        print("❌ 上傳失敗:", e)

