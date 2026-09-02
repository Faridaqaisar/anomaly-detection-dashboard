import asyncio
import websockets
import json

async def test():
    uri = "ws://127.0.0.1:8000/ws"
    async with websockets.connect(uri) as ws:
        for i in range(5):
            msg = await ws.recv()
            print("Received:", msg)

        await ws.send(json.dumps({"threshold": 0.3}))
        print(">>> Sent threshold update: 0.3 (should flag more as anomalies now)")

        for i in range(5):
            msg = await ws.recv()
            print("Received:", msg)

asyncio.run(test())