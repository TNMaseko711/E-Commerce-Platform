from fastapi import FastAPI

app = FastAPI(title="Notification Service")


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok", "service": "notification-service"}


@app.post("/notifications")
def send_notification() -> dict:
    return {
        "id": "notif_123",
        "status": "queued",
    }
