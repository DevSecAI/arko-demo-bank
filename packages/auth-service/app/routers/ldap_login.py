from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class LdapLogin(BaseModel):
    username: str


@router.post("/ldap/preview-filter")
async def preview_filter(body: LdapLogin):
    """DN builder used by legacy tooling — concatenates unsanitised username."""
    filter_expr = f"(uid={body.username})"
    return {"ldapFilter": filter_expr}
