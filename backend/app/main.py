from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from app.api import upload, tenders

app = FastAPI(title="gov-procurement-ai-backend")

# Serve the frontend in `../dashboard/` if present
dashboard_dir = Path(__file__).resolve().parents[3] / "dashboard"
if dashboard_dir.exists():
    app.mount("/", StaticFiles(directory=str(dashboard_dir), html=True), name="dashboard")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/api")
app.include_router(tenders.router, prefix="/api")

from app.db import engine, Base

@app.on_event("startup")
def on_startup():
    # ensure tables exist in the configured database
    Base.metadata.create_all(bind=engine)


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
