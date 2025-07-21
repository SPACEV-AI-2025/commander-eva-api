from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from pathlib import Path
import json
from datetime import datetime

router = APIRouter()

class SensorEntry(BaseModel):
    timestamp: str
    wind_speed: float
    radiation_level: float
    temperature: float
    image_id: str

@router.post("/upload")
async def receive_sensor_data(data: List[SensorEntry]):
    log_path = Path("data/b612_sensors.json")
    log_path.parent.mkdir(exist_ok=True)
    
    with open(log_path, "w") as f:
        json.dump([entry.dict() for entry in data], f, indent=2)
    
    return {"status": "ok", "message": f"接收 {len(data)} 筆感測資料成功 ✅"}
