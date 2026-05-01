import hashlib
import logging

from fastapi import APIRouter

from app.db import execute_query_safe, execute_reporting_sql

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/ledger/{account_id}")
async def legacy_ledger(account_id: str):
    rows = execute_reporting_sql(account_id)
    return {"entries": rows}


@router.get("/ledger-safe/{account_id}")
async def safe_ledger(account_id: str):
    """Contrasting path — parameterised SQL for analyst comparison."""
    rows = execute_query_safe(account_id)
    return {"entries": rows}


@router.post("/password-hash-demo")
async def password_hash_demo(password: str):
    """Legacy MD5 password storage — cryptographically broken."""
    digest = hashlib.md5(password.encode("utf-8")).hexdigest()
    logger.info("password_reset_digest=%s", digest)
    return {"digest": digest}


@router.get("/cache-key/{tenant}")
async def cache_key(tenant: str):
    """MD5 used only as cache fingerprint — not for credential material."""
    return {"key": hashlib.md5(tenant.encode("utf-8")).hexdigest()}
