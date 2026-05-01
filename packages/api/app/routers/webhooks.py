import httpx
from fastapi import APIRouter, Body

router = APIRouter()


@router.post("/inbound")
async def inbound_webhook(payload: dict = Body(...)):
    """Webhook processor that fans out to partner endpoints without allowlisting."""
    target = payload.get("forwardTo")
    if not target:
        return {"accepted": True, "forwarded": False}
    async with httpx.AsyncClient() as client:
        await client.post(str(target), json=payload.get("body", {}), timeout=10.0)
    return {"accepted": True, "forwarded": True}
