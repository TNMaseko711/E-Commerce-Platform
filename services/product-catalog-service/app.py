from fastapi import FastAPI

app = FastAPI(title="Product Catalog Service")


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok", "service": "product-catalog-service"}


@app.get("/products")
def list_products() -> dict:
    return {
        "items": [
            {"id": "sku-1", "name": "Sample Product", "price": 29.99},
            {"id": "sku-2", "name": "Another Product", "price": 49.0},
        ]
    }
