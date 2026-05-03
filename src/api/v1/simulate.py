from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from src.core.claude_service import stream_simulation

router = APIRouter(prefix="/simulate", tags=["simulate"])


class SimulationInput(BaseModel):
    company: str
    industry: str
    team_size: str
    tech_stack: str
    goals: str


@router.post("")
async def simulate(data: SimulationInput):
    async def generator():
        async for chunk in stream_simulation(data.model_dump()):
            yield chunk

    return StreamingResponse(generator(), media_type="text/plain; charset=utf-8")
