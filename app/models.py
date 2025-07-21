from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

class SensorData(BaseModel):
    timestamp: datetime
    wind_speed: float = Field(..., description="風速 m/s")
    radiation_level: float = Field(..., description="輻射 mSv/h")
    temperature: float = Field(..., description="溫度 °C")
    image_id: str

class SensorBatchUpload(BaseModel):
    data: List[SensorData]

class PerceptionResult(BaseModel):
    label: str         # flat / rough
    confidence: float  # 0~1

# commander-eva-api/api_server/models.py
from pydantic import BaseModel

class VisionResult(BaseModel):
    image_path: str
    label: str
    confidence: float