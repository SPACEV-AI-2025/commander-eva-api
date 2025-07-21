import os
import requests
from dotenv import load_dotenv

load_dotenv()

CWB_API_KEY = os.getenv("CWB_API_KEY")
CWB_API_URL = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"

def fetch_weather(location="臺北市"):
    if not CWB_API_KEY:
        raise ValueError("❌ 請在 .env 中設定 CWB_API_KEY")

    params = {
        "Authorization": CWB_API_KEY,
        "locationName": location
    }

    response = requests.get(CWB_API_URL, params=params)
    if response.status_code != 200:
        raise Exception(f"❌ CWB API 回傳錯誤: {response.status_code}")

    data = response.json()
    try:
        weather = data["records"]["location"][0]["weatherElement"]
        return {elem["elementName"]: elem["time"] for elem in weather}
    except Exception as e:
        raise Exception(f"❌ 資料解析錯誤: {e}")
