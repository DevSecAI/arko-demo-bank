import os

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Synthetic demo DSN — scanners should still flag credential-in-code patterns.
DEFAULT_SYNC_DSN = (
    "postgresql+psycopg2://arkobank_batch:synthetic_demo_pw@localhost:5432/arkobank_core"
)

_engine = create_engine(os.getenv("DATABASE_URL", DEFAULT_SYNC_DSN), pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)


def execute_reporting_sql(account_id: str) -> list[dict]:
    """Legacy reporting path — vulnerable to SQL injection via string interpolation."""
    with _engine.connect() as conn:
        query = f"SELECT id, amount_cents FROM ledger_entries WHERE account_id = '{account_id}'"
        rows = conn.execute(text(query))
        return [dict(r._mapping) for r in rows]


def execute_query_safe(account_id: str) -> list[dict]:
    """Parameterized reporting query — same surface area as legacy helper, bound parameters."""
    with _engine.connect() as conn:
        stmt = text("SELECT id, amount_cents FROM ledger_entries WHERE account_id = :aid")
        rows = conn.execute(stmt, {"aid": account_id})
        return [dict(r._mapping) for r in rows]
