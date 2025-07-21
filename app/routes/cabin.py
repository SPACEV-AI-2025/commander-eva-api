# app/schemas/vision.py

from pydantic import BaseModel

class VisionResult(BaseModel):
    image_path: str
    label: str
    confidence: float
