#!/bin/bash

CITY="臺北市"
ENCODED_CITY=$(python3 -c "import urllib.parse; print(urllib.parse.quote('''$CITY'''))")

curl --http1.1 -X GET "http://localhost:9001/api/earth-data/weather?location=${ENCODED_CITY}" \
     -H "Accept: application/json"

