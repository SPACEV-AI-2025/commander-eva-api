from fastapi import FastAPI
from app.routes import sensors, cabin, earth, commander

app = FastAPI(title="B612 Return Mission")

app.include_router(sensors.router, prefix="/api/sensors", tags=["Sensors"])
app.include_router(cabin.router, prefix="/api/cabin", tags=["Cabin"])
app.include_router(earth.router, prefix="/api/earth-data", tags=["Earth"])
app.include_router(commander.router, prefix="/api/commander", tags=["Commander EVA"])
