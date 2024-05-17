"""Health Check

    Returns:
        json: simple health
"""
from fastapi import APIRouter

router = APIRouter()

@router.post("/health")
async def health():
    """Health Check"""
    return {"ping": "pong"}
