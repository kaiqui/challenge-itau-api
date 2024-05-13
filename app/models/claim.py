from pydantic import BaseModel, Field
from pydantic import ValidationError
import jwt
from jwt.exceptions import InvalidTokenError
try:
    from app.utils.environment import Environment
except ModuleNotFoundError:
    from utils.environment import Environment

class JWTClaims(BaseModel):
    Name: str = Field(..., max_length=256, pattern="^[^\d]+$")
    Role: str = Field(..., pattern="^(Admin|Member|External)$")
    Seed: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

    @staticmethod
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    @classmethod
    def validate_jwt(cls, token: str) -> bool:
        try:
            env = Environment("JWT_SECRET")
            secret = env.get("JWT_SECRET")
            decoded_token = jwt.decode(token, secret, algorithms=["HS256"])
            jwt_claims = cls.from_dict(decoded_token)
            if (
                len(decoded_token.keys()) == 3 and
                cls.is_prime(jwt_claims.Seed) and
                len(jwt_claims.Name) <= 256
            ):
                return True
        except (InvalidTokenError, ValidationError):
            pass
        return False
