from fastapi import FastAPI

app = FastAPI(title="User Service")


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok", "service": "user-service"}


@app.get("/users/{user_id}")
def get_user(user_id: str) -> dict:
    return {
        "id": user_id,
        "name": "Sample User",
        "email": "user@example.com",
    }
