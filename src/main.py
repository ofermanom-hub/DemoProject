from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from src.api.v1.auth import router as auth_router
from src.api.v1.users import router as users_router
from src.api.v1.simulate import router as simulate_router

app = FastAPI(title="Enterprise Onboarding Simulator", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_PREFIX = "/api/v1"
app.include_router(auth_router, prefix=API_PREFIX)
app.include_router(users_router, prefix=API_PREFIX)
app.include_router(simulate_router, prefix=API_PREFIX)

app.mount("/static", StaticFiles(directory="frontend"), name="static")


@app.get("/")
async def serve_frontend() -> FileResponse:
    return FileResponse("frontend/index.html")


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}
