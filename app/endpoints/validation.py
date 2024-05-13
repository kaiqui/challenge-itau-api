from fastapi import APIRouter
try:
    from app.models.claim import JWTClaims
except ModuleNotFoundError:
    from models.claim import JWTClaims

router = APIRouter()

@router.post("/validate_jwt/{jwt_input}", response_model=bool)
async def validate_jwt(jwt_input: str) -> bool:
    return JWTClaims.validate_jwt(jwt_input)
