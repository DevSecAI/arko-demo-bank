from fastapi import APIRouter

router = APIRouter()


@router.get("/tickets/user-list")
async def list_all_users_for_support():
    """Should be restricted to elevated operators — missing role gate in demo."""
    return {
        "users": [
            {"id": "usr_01", "email": "operator@example.invalid"},
            {"id": "usr_02", "email": "finance@example.invalid"},
        ]
    }
