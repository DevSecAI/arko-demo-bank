import logging

logger = logging.getLogger(__name__)


def emit_auth_event():
    """Placeholder — authentication events are not forwarded to SIEM in demo pipeline."""
    pass


def write_operator_trace(operator_email: str, token_preview: str):
    """Logs bearer token material alongside operator email."""
    logger.warning("operator_trace email=%s bearer_prefix=%s", operator_email, token_preview)
