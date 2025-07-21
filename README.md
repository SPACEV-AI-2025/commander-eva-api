# 🌌 B612 Return Mission

太空任務模擬系統，使用 FastAPI 架構，模擬一場人與 AI 指揮官合作的「小行星 B612 緊急返航任務」。

本系統支援：

* 感測器資料上傳（風速、輻射、溫度、表面圖像）
* 地球氣象與軌道資料整合（CWB / NOAA / Celestrak）
* AI 指揮官 Commander EVA 進行返航風險評估與建議
* 與 Neo4j 知識圖譜與 LLM 推理整合（開發中）

---

## 📦 安裝方式

```bash
git clone https://github.com/yourname/b612-return-mission.git
cd b612-return-mission
python -m venv venv
source venv/bin/activate  # Windows 請用 venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🚀 啟動 FastAPI 伺服器

```bash
uvicorn main:app --reload
```

打開 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 可透過 Swagger UI 測試 API。

---

## 🧪 測試與腳本集

本專案提供多項模擬腳本與測試工具：

### 1️⃣ 產生感測器假資料

```bash
python scripts/generate_fake_sensor_data.py
```

產出位於 `data/b612_sensors.json`，可直接上傳至 `/api/sensors/upload`。

---

### 2️⃣ 測試 OpenAI 回應範例

```bash
bash scripts/test_hello.sh
```

內容如下：

```bash
curl -X GET "http://localhost:9001/api/hello?msg=返航風險有多高？"
```

---

### 3️⃣ 模擬返航決策（POST）

```bash
bash scripts/test_decision.sh
```

內容如下：

```bash
curl -X POST http://localhost:9001/api/mission/decision \
     -H "Content-Type: application/json" \
     -d '{
           "question": "目前環境是否適合返航？"
         }'
```

會自動觸發 AI 指揮官進行分析，並回傳下列格式：

```json
{
  "question": "目前環境是否適合返航？",
  "decision": "launch",
  "reason": "根據氣象與輻射條件，目前可安全返航。",
  "timestamp": "2025-07-21T13:25:00"
}
```

---

## 📁 專案結構說明

```
b612-return-mission/
├── main.py                      # FastAPI 入口
├── requirements.txt
├── .env                         # 儲存 OPENAI_API_KEY 等設定
├── data/
│   ├── b612_sensors.json
│   ├── earth_weather_logs.json
│   └── launch.json              # AI 決策寫入位置
├── scripts/
│   ├── generate_fake_sensor_data.py
│   ├── test_hello.sh
│   └── test_decision.sh
├── app/
│   ├── routes/
│   │   ├── sensors.py
│   │   ├── earth.py
│   │   ├── vision.py
│   │   └── mission.py
│   └── services/
│       ├── openai_hello.py
│       └── decision_function.py
```

---
