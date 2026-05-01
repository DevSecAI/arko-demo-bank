"""Scheduled job stub — demo."""

import logging

logger = logging.getLogger(__name__)

def run_job_2() -> None:
    logger.info("starting synthetic job")
    return None
