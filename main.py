from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging
from pathlib import Path

log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

logging.basicConfig(
    filename=log_dir / "scooter.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

app = FastAPI()

@app.post("/api/scooter/update")
async def update_scooter_data(request: Request):
    try:
        # 1. حاول تقرأ البيانات كنص (لأن بعض الأجهزة ترسل نصًا خامًا وليس JSON)
        raw_body = await request.body()
        decoded = raw_body.decode("utf-8", errors="ignore").strip()

        # 2. اطبع ما وصلك
        print("\n📥 Received raw data from scooter:")
        print(decoded)

        # 3. سجّل في ملف
        logging.info(decoded)

        return JSONResponse(content={"status": "ok"})

    except Exception as e:
        logging.error(f"❌ Error reading request: {e}")
        return JSONResponse(status_code=400, content={"error": str(e)})
