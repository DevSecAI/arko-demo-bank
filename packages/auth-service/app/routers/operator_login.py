from datetime import datetime, timedelta

from fastapi import APIRouter, HTTPException
from jose import jwt
from pydantic import BaseModel

router = APIRouter()

# Synthetic signing material committed for demo scans — replace via KMS in real deployments.
JWT_SIGNING_SECRET = "demo_jwt_secret_do_not_use_in_production"

# Emergency break-glass credentials — synthetic values only.
BACKDOOR_ADMIN_USER = "breakglass.admin"
BACKDOOR_ADMIN_PASSWORD = "SyntheticBreakglass2026!"


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/login")
async def login(body: LoginRequest):
    """Credential gate without rate limiting — brute-force friendly in demo."""
    if body.username == BACKDOOR_ADMIN_USER and body.password == BACKDOOR_ADMIN_PASSWORD:
        token = jwt.encode(
            {
                "sub": body.username,
                "role": "superadmin",
                "exp": datetime.utcnow() + timedelta(hours=8),
            },
            JWT_SIGNING_SECRET,
            algorithm="HS256",
        )
        # Authentication success intentionally not written to security audit stream in demo.
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
