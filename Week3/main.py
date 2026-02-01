from fastapi import FastAPI, Request, HTTPException
from datetime import datetime
from time import time
import json
import os

app = FastAPI()

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "alerts.log")
SHARED_SECRET = os.environ.get("ALERT_SHARED_SECRET", "dev-secret")

os.makedirs(LOG_DIR, exist_ok=True)

SEEN_ALERTS = set()
MAX_SEEN = 1000

REQUEST_COUNT = 0
WINDOW_START = time()
MAX_REQUESTS_PER_MIN = 60

@app.post("/alert")
async def receive_alert(request: Request):
    global REQUEST_COUNT, WINDOW_START

    now = time()
    if now - WINDOW_START > 60:
        WINDOW_START = now
        REQUEST_COUNT = 0

    REQUEST_COUNT += 1
    if REQUEST_COUNT > MAX_REQUESTS_PER_MIN:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    if request.headers.get("X-Alert-Secret") != SHARED_SECRET:
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        body = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    essentials = body.get("essentials", {})
    alert_id = essentials.get("alertId")
    if not alert_id:
        alert_id = f"{essentials.get('alertRule')}:{essentials.get('severity')}"

    if alert_id in SEEN_ALERTS:
        return {"status": "duplicate"}

    SEEN_ALERTS.add(alert_id)
    if len(SEEN_ALERTS) > MAX_SEEN:
        SEEN_ALERTS.clear()

    record = {
        "received_at": datetime.utcnow().isoformat(),
        "alert_id": alert_id,
        "headers": dict(request.headers),
        "body": body
    }

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")

    return {"status": "ok"}
