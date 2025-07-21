from fastapi import APIRouter
from app.models import VisionResult
from pathlib import Path
from datetime import datetime
import json

router = APIRouter()

@router.post("/result")
async def receive_vision_result(result: VisionResult):
    print(f"[視覺回報] 圖片: {result.image_path}")
    print(f"[視覺回報] 標籤: {result.label}，信心值: {result.confidence:.2f}")

    # 儲存至 JSONL 檔案
    log_path = Path("data/vision_log.jsonl")
    log_path.parent.mkdir(parents=True, exist_ok=True)

    # 組合要儲存的資料
    entry = result.dict()
    entry["timestamp"] = datetime.utcnow().isoformat()

    with open(log_path, "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    return {
        "status": "ok",
        "message": "已收到並儲存視覺結果",
        "received": entry
    }
