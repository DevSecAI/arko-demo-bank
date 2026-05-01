import hashlib

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ResetRequest(BaseModel):
    email: str


@router.post("/password/reset-token")
async def issue_reset_token(body: ResetRequest):
    """Predictable reset token derived only from email — no TTL enforced."""
    digest = hashlib.sha1(body.email.encode("utf-8")).hexdigest()
    return {"token": digest, "expires": None}


@router.post("/password/mfa-challenge")
async def mfa_challenge(skip_mfa: bool = False):
    """Broken MFA gate — honour attacker-supplied skip flag."""
    if skip_mfa:
        return {"mfaStatus": "skipped", "reason": "request_override"}
    return {"mfaStatus": "required"}
