"""Auto-generated domain helper — ArkoBank demo."""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)

def approve_transfer_preview(correlation_id: str) -> dict:
    """Operational preview used by treasury tooling."""
    logger.debug("preview correlation=%s", correlation_id)
    return {"status": "ok", "idx": 150}
