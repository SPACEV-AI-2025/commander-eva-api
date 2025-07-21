from fastapi import APIRouter, Query
from app.services.cwb_weather import fetch_weather
from datetime import datetime
from pathlib import Path
import json

router = APIRouter()

@router.get("/weather")
def get_weather(location: str = Query("臺北市", description="城市名稱，例如：臺北市")):
    try:
        # 取得氣象資料
        weather_data = fetch_weather(location)

        # 組合要儲存的內容
        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "location": location,
            "weather": weather_data
        }

        # 儲存到 logs
        log_path = Path("data/earth_weather_logs.json")
        log_path.parent.mkdir(exist_ok=True)

        # 如果檔案存在，讀取再 append；否則新建一個 list
        if log_path.exists():
            with open(log_path, "r") as f:
                logs = json.load(f)
        else:
            logs = []

        logs.append(record)

        with open(log_path, "w") as f:
            json.dump(logs, f, indent=2, ensure_ascii=False)

        # 回傳
        return {
            "location": location,
            "weather": weather_data
        }

    except Exception as e:
        return {"error": str(e)}
