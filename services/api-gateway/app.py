from fastapi import FastAPI

app = FastAPI(title="API Gateway")


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok", "service": "api-gateway"}


@app.get("/")
def index() -> dict:
    return {
        "message": "API Gateway for the e-commerce platform",
        "routes": [
            "/users/{user_id}",
            "/products",
            "/carts/{user_id}",
            "/orders/{order_id}",
            "/payments",
            "/notifications",
        ],
    }
