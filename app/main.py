from fastapi import FastAPI
from app.routers import auth, users
from app.models import user, role, permission, token_blacklist 

app = FastAPI(title="Backend", version="1.0.0")

app.include_router(auth.router)
app.include_router(users.router)


@app.get("/health")
def health():
    return {"status": "ok"}