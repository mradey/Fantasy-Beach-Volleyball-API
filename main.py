from fastapi import FastAPI, WebSocket, Request

app = FastAPI()


@app.get("/health")
async def hanlde_health_check():
    return {
        "status": "ok"
    }


@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()

        # Process WebSocket data here
        await websocket.send_text(f"Message received: {data}")
