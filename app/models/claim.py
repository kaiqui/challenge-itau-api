from pydantic import BaseModel, Field
from pydantic import ValidationError
import jwt
from jwt.exceptions import InvalidTokenError
try:
    from app.utils.environment import Environment
except ModuleNotFoundError:
    from utils.environment import Environment
from prometheus_client import Counter


jwt_validation_success_counter = Counter(
    "jwt_validation_success_counter",
    "Number of successful JWT validations"
)

jwt_validation_failure_counter = Counter(
    "jwt_validation_failure_counter",
    "Total number of failed JWT validations"
)

jwt_validation_error_counter = Counter(
    "jwt_validation_error_counter",
    "Number of JWT validation errors"
)

jwt_invalid_token_error_counter = Counter(
    "jwt_invalid_token_error_counter",
    "Number of JWT invalid token errors"
)

jwt_unknown_error_counter = Counter(
    "jwt_unknown_error_counter",
    "Number of unknown JWT errors"
)

class JWTClaims(BaseModel):
    Name: str = Field(..., max_length=256, pattern=r"^[^\d]+$")
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

    @staticmethod
    def _validate_jwt(token: str) -> bool:
        try:
            env = Environment("JWT_SECRET")
            secret = env.get("JWT_SECRET")
            decoded_token = jwt.decode(token, secret, algorithms=["HS256"])
            jwt_claims = JWTClaims.from_dict(decoded_token)
            if (
                len(decoded_token.keys()) == 3 and
                JWTClaims.is_prime(jwt_claims.Seed) and
                len(jwt_claims.Name) <= 256
            ):
                jwt_validation_success_counter.inc()
                return True
        except ValidationError:
            jwt_validation_failure_counter.inc()
        except InvalidTokenError:
            jwt_invalid_token_error_counter.inc()
        except Exception:
            jwt_unknown_error_counter.inc()
        return False

    @classmethod
    def validate_jwt(cls, token: str) -> bool:
        return cls._validate_jwt(token)
