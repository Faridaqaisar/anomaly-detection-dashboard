# 📉 Real-Time Anomaly Detection Dashboard

A live-updating dashboard that streams simulated sensor data, flags anomalies using Isolation Forest, and lets users adjust detection sensitivity in real time — built with WebSockets for genuine live data streaming.

## Tech Stack
FastAPI, WebSockets, scikit-learn (Isolation Forest), hand-coded HTML/Canvas frontend (no charting library)

## Features
- Live sensor data simulation with occasional injected anomalies
- Isolation Forest model trained on normal readings
- Real-time WebSocket streaming (server pushes new readings every second)
- Hand-coded canvas chart, scrolling live as new data arrives
- Adjustable sensitivity slider — changes detection threshold live, without restarting the server

## Running Locally

**Backend:**
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

**Frontend:**
Open `frontend/index.html` directly in your browser (no server needed — it's a plain HTML file that connects via WebSocket to the backend running on `localhost:8000`).

## Project Structure
anomaly-dashboard/
├── backend/
│ ├── main.py # WebSocket server
│ ├── model.py # Isolation Forest + data simulator
│ └── requirements.txt
└── frontend/
└── index.html # Canvas chart + WebSocket client


## Why This Design
This project demonstrates real-time, bidirectional communication (WebSockets) rather than typical request-response APIs — the server continuously pushes new predictions without the client needing to ask, and the client can send sensitivity updates back at any time without breaking the connection.
