from fastapi import FastAPI
from app.routes import sensors, cabin, earth, vision

app = FastAPI(title="B612 Return Mission")

app.include_router(sensors.router, prefix="/api/sensors", tags=["Sensors"])
app.include_router(earth.router, prefix="/api/earth-data", tags=["Earth"])
app.include_router(vision.router, prefix="/api/vision", tags=["Vision"])
