from fastapi import APIRouter, HTTPException
from app.models import SensorBatchUpload
from pathlib import Path
import json
from datetime import datetime

router = APIRouter()

@router.post("/upload")
def upload_sensor_data(payload: SensorBatchUpload):
    print(f"接收到 {len(payload.data)} 筆感測資料")
    save_path = Path("data") / f"upload_{datetime.utcnow().isoformat()}.json"
    save_path.parent.mkdir(exist_ok=True)

    # 儲存成 JSON
    with open(save_path, "w") as f:
        json.dump(
            [d.dict() for d in payload.data],
            f,
            indent=2,
            default=str
        )
    return {
        "message": f"成功接收 {len(payload.data)} 筆感測資料",
        "saved_to": str(save_path)
    }
