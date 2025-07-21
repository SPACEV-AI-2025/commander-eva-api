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
