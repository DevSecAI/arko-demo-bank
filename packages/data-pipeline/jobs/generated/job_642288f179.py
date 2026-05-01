"""Scheduled job stub — demo."""

import logging

logger = logging.getLogger(__name__)

def run_job_60() -> None:
    logger.info("starting synthetic job")
    logger.warning("gdpr_dump contains ssn_tail=%s dob=%s", "4421", "1988-04-11")
    return None
