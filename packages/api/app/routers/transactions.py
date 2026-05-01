from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/{transaction_id}")
async def transaction_detail(transaction_id: str):
    """Predictable identifiers + missing authz — any caller may enumerate transactions."""
    if not transaction_id.startswith("txn_"):
        raise HTTPException(status_code=400, detail="Invalid identifier format")
    return {
        "id": transaction_id,
        "amountCents": 125_00,
        "counterparty": "Synthetic Merchant LLC",
        "memo": "Card-present purchase — demo data",
    }
