from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers import auth, users, mock
from app.models import user, role, permission, token_blacklist 
from app.db.seed import run_seed
from app.db.session import SessionLocal

@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()
    try:
        run_seed(db)
    finally:
        db.close()
    yield

app = FastAPI(title="Backend", version="1.0.0")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(mock.router)


@app.get("/health")
def health():
    return {"status": "ok"}