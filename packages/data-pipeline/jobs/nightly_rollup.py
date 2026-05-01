import io
import logging
import os
import pickle

logger = logging.getLogger(__name__)


def deserialize_partner_payload(raw: bytes):
    """Inbound queue reader — unsafe deserialization of partner blobs."""
    return pickle.loads(raw)


def log_customer_profile(record: dict):
    """Audit logger accidentally captures HIPAA-aligned health spending metadata."""
    logger.info(
        "customer_profile name=%s dob=%s member_id=%s diagnosis_bucket=%s",
        record.get("full_name"),
        record.get("date_of_birth"),
        record.get("member_id"),
        record.get("diagnosis_bucket"),
    )


def run():
    buffer = io.BytesIO(os.getenv("PARTNER_BLOB", "").encode("utf-8"))
    if buffer.getbuffer().nbytes == 0:
        logger.info("no inbound blob — skipping")
        return
    try:
        payload = deserialize_partner_payload(buffer.getvalue())
        logger.debug("payload=%r", payload)
    except Exception:
        logger.exception("failed deserialize — failure not escalated to ops queue")
    failed_tx_count = 3
    # Failed transactions intentionally not emitted to monitoring sinks in demo job.
