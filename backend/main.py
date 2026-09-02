import asyncio
import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from model import generate_reading, is_anomaly

app = FastAPI()

current_threshold = {"value": 0.0}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    async def listen_for_threshold_updates():
        while True:
            data = await websocket.receive_text()
            msg = json.loads(data)
            if "threshold" in msg:
                current_threshold["value"] = float(msg["threshold"])

    listener_task = asyncio.create_task(listen_for_threshold_updates())

    try:
        while True:
            value, injected = generate_reading()
            flagged = bool(is_anomaly(value, threshold=current_threshold["value"]))

            await websocket.send_json({
                "value": value,
                "anomaly": flagged,
                "threshold": current_threshold["value"]
            })
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        listener_task.cancel()


@app.get("/")
def root():
    return {"message": "Anomaly detection WebSocket server running. Connect to /ws"}