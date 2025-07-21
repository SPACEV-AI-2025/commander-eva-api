from fastapi import APIRouter, Query
from app.services.cwb_weather import fetch_weather

router = APIRouter()

@router.get("/weather")
def get_weather(location: str = Query("臺北市", description="城市名稱，例如：臺北市")):
    try:
        weather_data = fetch_weather(location)
        return {
            "location": location,
            "weather": weather_data
        }
    except Exception as e:
        return {"error": str(e)}
