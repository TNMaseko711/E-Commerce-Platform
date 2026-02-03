from fastapi import FastAPI

app = FastAPI(title="Order Service")


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok", "service": "order-service"}


@app.get("/orders/{order_id}")
def get_order(order_id: str) -> dict:
    return {
        "id": order_id,
        "status": "processing",
        "total": 78.99,
    }
