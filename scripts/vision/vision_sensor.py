import sys
import numpy as np
from PIL import Image
from keras.layers import TFSMLayer
import requests
# from commander_eva_api.api_server.models import VisionResult  # 若無法 import 就改用 dict 傳送
import json

# 模型與標籤檔案
MODEL_PATH = "model.savedmodel"
LABEL_PATH = "labels.txt"
API_URL = "http://localhost:9001/api/vision/result"

# 載入模型
model = TFSMLayer(MODEL_PATH, call_endpoint="serving_default")

# 載入 labels
with open(LABEL_PATH, "r") as f:
    labels = [line.strip() for line in f.readlines()]

def classify(image_path: str):
    img = Image.open(image_path).convert("RGB").resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0).astype(np.float32)

    output = model(img_array)
    if isinstance(output, dict):
        output_tensor = list(output.values())[0]
    else:
        output_tensor = output

    prediction = output_tensor.numpy()[0]
    index = int(np.argmax(prediction))
    label = labels[index]
    confidence = float(prediction[index])

    # 顯示結果
    print(f"✅ 圖片：{image_path}")
    print(f"📌 預測結果：{label}")
    print(f"📊 信心值：{confidence:.2f}")

    # 傳送至 FastAPI
    payload = {
        "image_path": image_path,
        "label": label,
        "confidence": confidence
    }

    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        print("🚀 成功上傳到 API：", response.json())
    except Exception as e:
        print("❌ 上傳失敗：", e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❗ 請提供圖檔路徑，例如：python vision_sensor.py data/images/flat.png")
        sys.exit(1)

    image_path = sys.argv[1]
    classify(image_path)
