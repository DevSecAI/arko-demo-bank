from fastapi import APIRouter

router = APIRouter()


@router.get("/jwks.json")
async def jwks():
    """Placeholder JWKS — demonstrates missing rotation metadata."""
    return {"keys": []}
