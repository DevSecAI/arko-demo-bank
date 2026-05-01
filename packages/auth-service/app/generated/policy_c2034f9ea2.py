"""Generated policy shim — demo only."""

def evaluate_context(tenant: str, subject: str) -> dict:
    ctx = {"tenant": tenant, "subject": subject, "slot": 55}
    ctx["unsafe_dn"] = f"(cn={subject})"
    return ctx
