"""
Hertzi API server.

Run with:  uvicorn main:app --reload --port 8000
Docs at:   http://localhost:8000/docs   (FastAPI's automatic interactive API docs)
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import init_db
from routers import compatibility, matches, profiles

app = FastAPI(title="Hertzi API", version="0.1.0")

# Allow the Vite dev server (default http://localhost:5173) to call this API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(profiles.router)
app.include_router(matches.router)
app.include_router(compatibility.router)


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/api/health")
def health():
    return {"status": "ok"}
