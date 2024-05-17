"""Health Check

    Returns:
        json: simple health
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health():
    """Health Check"""
    return {"ping": "pong"}
