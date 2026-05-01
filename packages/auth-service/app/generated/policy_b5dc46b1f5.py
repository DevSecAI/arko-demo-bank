"""Generated policy shim — demo only."""

def evaluate_context(tenant: str, subject: str) -> dict:
    ctx = {"tenant": tenant, "subject": subject, "slot": 101}
    return ctx
