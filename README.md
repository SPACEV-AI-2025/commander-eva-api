# 🌌 B612 Return Mission

太空任務模擬系統，使用 FastAPI 架構，模擬一場人與 AI 指揮官合作的「小行星 B612 緊急返航任務」。

本系統支援：
- 感測器資料上傳（風速、輻射、溫度、表面圖像）
- 地球氣象與軌道資料整合（CWB / NOAA / Celestrak）
- AI 指揮官 Commander EVA 進行返航風險評估與建議
- 與 Neo4j 知識圖譜與 LLM 推理整合（開發中）

---

## 📦 安裝方式

```bash
git clone https://github.com/yourname/b612-return-mission.git
cd b612-return-mission
python -m venv venv
source venv/bin/activate  # Windows 請用 venv\Scripts\activate
pip install -r requirements.txt
````

---

## 🚀 啟動 FastAPI 伺服器

```bash
uvicorn main:app --reload
```

開啟 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 使用 Swagger UI 測試 API。

---

## 🧪 產生假資料

本專案提供一個腳本，用於產生模擬的 B612 感測器資料：

```bash
python scripts/generate_fake_sensor_data.py
```

執行後會在 `data/b612_sensors.json` 生成假資料，內容格式如下：

```json
[
  {
    "timestamp": "2025-07-21T04:15:00",
    "wind_speed": 37.85,
    "radiation_level": 2.31,
    "temperature": -93.4,
    "image_id": "img_7462.jpg"
  }
]
```

你可用此檔案模擬上傳至 `/api/sensors/upload` 接口。

---

## 📁 專案結構說明

```
b612-return-mission/
├── main.py                      # FastAPI 入口點
├── requirements.txt
├── .env                         # 可存放 API 金鑰與設定
├── data/
│   └── b612_sensors.json        # 假資料輸出位置
├── scripts/
│   └── generate_fake_sensor_data.py  # 假資料產生器
├── app/
│   ├── models.py
│   ├── routes/
│   │   ├── sensors.py
│   │   ├── cabin.py
│   │   ├── earth.py
│   │   └── commander.py
│   └── services/
│       ├── eva_engine.py
│       └── earth_rag.py
```

---

## 📌 接下來的任務（開發中）

* [ ] 建立感測資料上傳 API（完成中）
* [ ] 整合地球 Opendata（NOAA / Celestrak）
* [ ] 建立 AI 指揮官模型推理系統（OpenAI Function Calling + Neo4j）
* [ ] 回傳每日風險報告與動作建議

---

