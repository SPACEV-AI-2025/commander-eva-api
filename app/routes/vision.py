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

    # 確保資料夾存在
    log_path = Path("data/vision_log.jsonl")
    log_path.parent.mkdir(parents=True, exist_ok=True)

    # 加上 timestamp
    entry = result.dict()
    entry["timestamp"] = datetime.utcnow().isoformat()

    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        print(f"✅ 寫入成功：{log_path}")
    except Exception as e:
        print(f"❌ 寫入失敗：{e}")

    return {
        "status": "ok",
        "message": "已收到並嘗試儲存視覺結果",
        "received": entry
    }
