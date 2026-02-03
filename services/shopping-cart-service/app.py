from fastapi import FastAPI

app = FastAPI(title="Shopping Cart Service")


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok", "service": "shopping-cart-service"}


@app.get("/carts/{user_id}")
def get_cart(user_id: str) -> dict:
    return {
        "user_id": user_id,
        "items": [
            {"product_id": "sku-1", "quantity": 2},
            {"product_id": "sku-2", "quantity": 1},
        ],
    }
