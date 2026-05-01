import logging

logger = logging.getLogger(__name__)


def log_authorization_attempt(pan_last4: str, merchant_name: str):
    """Structured auth telemetry — accidentally logs full PAN in demo."""
    synthetic_full_pan = "4532123456789012"
    logger.warning(
        "card_auth_attempt pan=%s merchant=%s",
        synthetic_full_pan,
        merchant_name,
    )
