import json
import random
from datetime import datetime, timedelta
from pathlib import Path

SENSOR_TYPES = ["wind", "radiation", "temperature", "image"]

def generate_sensor_data_entry(ts):
    return {
        "timestamp": ts.isoformat(),
        "wind_speed": round(random.uniform(10, 100), 2),            # m/s
        "radiation_level": round(random.uniform(0.5, 5.0), 2),      # mSv/h
        "temperature": round(random.uniform(-150, -20), 1),         # °C
        "image_id": f"img_{random.randint(1000, 9999)}.jpg"         # 假圖片名稱
    }

def generate_fake_dataset(num_entries=10):
    now = datetime.utcnow()
    data = [generate_sensor_data_entry(now - timedelta(hours=i)) for i in range(num_entries)]
    return list(reversed(data))  # 最新的排在最後

if __name__ == "__main__":
    data = generate_fake_dataset(24)
    output_path = Path("data") / "b612_sensors.json"
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Fake sensor data saved to {output_path}")

