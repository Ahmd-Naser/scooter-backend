from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json
import logging
from pathlib import Path

# Setup logging directory
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=log_dir / "scooter.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

app = FastAPI()

@app.post("/api/scooter/update")
async def update_scooter_data(request: Request):
    data = await request.json()

    # Pretty JSON string
    pretty_json = json.dumps(data, indent=4)

    # Print to console
    print("\n📥 Received data from scooter:")
    print(pretty_json)

    # Save to log file
    logging.info(pretty_json)

    return JSONResponse(content={"status": "ok"})
