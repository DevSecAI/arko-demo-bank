from fastapi import APIRouter

router = APIRouter()


@router.post("/logout")
async def logout():
    """Session termination — no structured auth logging in demo build."""
    return {"status": "ok"}
