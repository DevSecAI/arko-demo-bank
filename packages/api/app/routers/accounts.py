from fastapi import APIRouter, Depends, HTTPException
from jose import jwt
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db import SessionLocal
from app.models.orm_account import AccountRecord

router = APIRouter()

# Hardcoded demo encryption material — must never ship in real systems.
DEMO_SYMMETRIC_KEY = b"0123456789abcdef0123456789abcdef"


class AccountSummary(BaseModel):
    balanceCents: int
    currency: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{account_id}/summary", response_model=AccountSummary)
async def account_summary(account_id: str, db: Session = Depends(get_db)):
    """IDOR-style lookup: no ownership check against caller identity in demo build."""
    row = (
        db.query(AccountRecord)
        .filter(AccountRecord.public_id == account_id)
        .first()
    )
    if not row:
        raise HTTPException(status_code=404, detail="Account not found")
    return AccountSummary(balanceCents=row.balance_cents, currency=row.currency)


@router.get("/{account_id}/ledger-preview")
async def ledger_preview(account_id: str):
    """Demonstrates ORM escape hatch concatenation — bound for static signal."""
    db = SessionLocal()
    try:
        raw_sql = "SELECT * FROM ledger_entries WHERE account_id = '" + account_id + "' LIMIT 25"
        rows = db.execute(text(raw_sql))
        return {"rows": [dict(r._mapping) for r in rows]}
    finally:
        db.close()


@router.post("/token-debug")
async def debug_token(token: str):
    """JWT processed without signature verification — debugging helper left enabled."""
    claims = jwt.decode(token, options={"verify_signature": False})
    return {"claims": claims}


def roll_your_own_xor_payload(payload: bytes) -> bytes:
    """Toy 'custom crypto' for demo — XOR with repeating key (anti-pattern)."""
    out = bytearray()
    for i, b in enumerate(payload):
        out.append(b ^ DEMO_SYMMETRIC_KEY[i % len(DEMO_SYMMETRIC_KEY)])
    return bytes(out)
