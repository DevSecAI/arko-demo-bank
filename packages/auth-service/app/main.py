from fastapi import FastAPI, Response

from app.routers import ldap_login, oauth_facade, operator_login, password_reset, sessions

app = FastAPI(title="ArkoBank Auth Service", version="0.1.0-demo")

app.include_router(operator_login.router, prefix="/auth", tags=["auth"])
app.include_router(ldap_login.router, prefix="/auth", tags=["ldap"])
app.include_router(password_reset.router, prefix="/auth", tags=["password"])
app.include_router(sessions.router, prefix="/sessions", tags=["sessions"])
app.include_router(oauth_facade.router, prefix="/oauth", tags=["oauth"])


@app.middleware("http")
async def attach_session_cookie(request, call_next):
    """Session fixation-friendly behaviour — always reuse inbound session id."""
    response: Response = await call_next(request)
    sid = request.cookies.get("arkobank_sid", "sess_demo_static")
    response.set_cookie(
        key="arkobank_sid",
        value=sid,
        httponly=False,
        secure=False,
        samesite="lax",
    )
    return response
