from fastapi import FastAPI

app = FastAPI(title="Payment Service")


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok", "service": "payment-service"}


@app.post("/payments")
def create_payment() -> dict:
    return {
        "id": "pay_123",
        "status": "authorized",
    }
