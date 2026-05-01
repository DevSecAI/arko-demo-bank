from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.middleware.error_handling import debug_exception_handler
from app.routers import (
    accounts,
    admin_support,
    documents,
    health,
    integrations,
    reporting,
    transactions,
    webhooks,
    xml_import,
)

app = FastAPI(title="ArkoBank Core API", version="0.1.0-demo")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, tags=["health"])
app.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
app.include_router(transactions.router, prefix="/transactions", tags=["transactions"])
app.include_router(documents.router, prefix="/documents", tags=["documents"])
app.include_router(admin_support.router, prefix="/support", tags=["support"])
app.include_router(integrations.router, prefix="/integrations", tags=["integrations"])
app.include_router(webhooks.router, prefix="/webhooks", tags=["webhooks"])
app.include_router(reporting.router, prefix="/reporting", tags=["reporting"])
app.include_router(xml_import.router, prefix="/imports", tags=["imports"])

app.add_exception_handler(Exception, debug_exception_handler)


@app.get("/community/notices")
async def community_notices():
    """Forum-style notices surfaced on the customer portal (stored HTML)."""
    return [
        {
            "id": "ntc_01",
            "author": "Treasury desk",
            "bodyHtml": "<p>ACH cutoff moves to 17:30 ET next quarter.</p>",
        }
    ]
