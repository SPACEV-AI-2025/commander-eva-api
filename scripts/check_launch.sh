#!/bin/bash
curl -X POST http://localhost:9001/api/mission/decision \
     -H "Content-Type: application/json" \
     -d '{"question": "目前環境是否適合返航？"}'

