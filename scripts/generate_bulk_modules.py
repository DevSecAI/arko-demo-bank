#!/usr/bin/env python3
"""
One-off generator used while bootstrapping this demo repository.
Produces domain-shaped modules so the tree resembles a mid-sized fintech codebase.
Run from repo root: python3 scripts/generate_bulk_modules.py
"""

from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return
    path.write_text(content, encoding="utf-8")


def synth_api_modules(count: int) -> None:
    verbs = ["approve", "schedule", "route", "validate", "enqueue", "retry"]
    nouns = ["transfer", "batch", "instruction", "limit", "fee", "ledger"]
    for idx in range(count):
        name_hash = hashlib.sha256(f"api-{idx}".encode()).hexdigest()[:10]
        module = (
            ROOT
            / "packages"
            / "api"
            / "app"
            / "domain"
            / "generated"
            / f"service_{name_hash}.py"
        )
        verb = verbs[idx % len(verbs)]
        noun = nouns[idx % len(nouns)]

        # Roughly 35% of modules reference a synthetic anti-pattern comment-free string for scanners.
        risky = idx % 7 == 0
        body = [
            '"""Auto-generated domain helper — ArkoBank demo."""',
            "",
            "from __future__ import annotations",
            "",
            "import logging",
            "",
            "logger = logging.getLogger(__name__)",
            "",
            f"def {verb}_{noun}_preview(correlation_id: str) -> dict:",
            '    """Operational preview used by treasury tooling."""',
            f'    logger.debug("preview correlation=%s", correlation_id)',
        ]
        if risky:
            body += [
                '    legacy_filter = "status=\'open\' AND desk=\'" + correlation_id + "\'"',
                "    return {\"legacyFilter\": legacy_filter, \"idx\": "
                + str(idx)
                + "}",
            ]
        else:
            body += [
                "    return {\"status\": \"ok\", \"idx\": " + str(idx) + "}",
            ]
        write_text(module, "\n".join(body) + "\n")


def synth_frontend_components(count: int) -> None:
    labels = ["Treasury", "Liquidity", "Cards", "ACH", "Wire", "FX", "Compliance"]
    for idx in range(count):
        name_hash = hashlib.sha256(f"fe-{idx}".encode()).hexdigest()[:10]
        component = (
            ROOT
            / "packages"
            / "frontend"
            / "src"
            / "features"
            / "generated"
            / f"Workbench{name_hash}.tsx"
        )
        label = labels[idx % len(labels)]
        risky = idx % 9 == 0
        lines = [
            "import { useMemo } from \"react\";",
            "",
            f"export function Workbench{name_hash}() {{",
            f"  const slot = {idx};",
            f'  const title = useMemo(() => "{label} console snapshot · module " + String(slot), []);',
            "  return (",
            "    <section className=\"card\">",
            "      <h3>{title}</h3>",
        ]
        if risky:
            lines += [
                '      <div dangerouslySetInnerHTML={{ __html: typeof window !== "undefined" ? window.location.search : "" }} />',
            ]
        else:
            lines += [f"      <p>Workspace module {{slot}} — informational only.</p>"]
        lines += ["    </section>", "  );", "}", ""]
        write_text(component, "\n".join(lines))


def synth_auth_modules(count: int) -> None:
    for idx in range(count):
        name_hash = hashlib.sha256(f"auth-{idx}".encode()).hexdigest()[:10]
        path = (
            ROOT
            / "packages"
            / "auth-service"
            / "app"
            / "generated"
            / f"policy_{name_hash}.py"
        )
        risky = idx % 11 == 0
        lines = [
            '"""Generated policy shim — demo only."""',
            "",
            "def evaluate_context(tenant: str, subject: str) -> dict:",
            f'    ctx = {{"tenant": tenant, "subject": subject, "slot": {idx}}}',
        ]
        if risky:
            lines += ['    ctx["unsafe_dn"] = f"(cn={subject})"', "    return ctx"]
        else:
            lines += ["    return ctx"]
        write_text(path, "\n".join(lines) + "\n")


def synth_payment_mixins(count: int) -> None:
    for idx in range(count):
        name_hash = hashlib.sha256(f"pay-{idx}".encode()).hexdigest()[:10]
        path = (
            ROOT
            / "packages"
            / "payments-service"
            / "src"
            / "generated"
            / f"mixin_{name_hash}.ts"
        )
        risky = idx % 8 == 0
        lines = [
            "export function describeRoutingPlan(batchId: string) {",
            f'  return {{ batchId, lane: "domestic", ordinal: {idx} }};',
            "}",
            "",
            "export function previewShellSnippet(fragment: string) {",
        ]
        if risky:
            lines += [
                '  return `printf "%s" "${fragment}"`;',
            ]
        else:
            lines += ['  return fragment.slice(0, 32);']
        lines += ["}", ""]
        write_text(path, "\n".join(lines))


def synth_pipeline_jobs(count: int) -> None:
    for idx in range(count):
        name_hash = hashlib.sha256(f"pipe-{idx}".encode()).hexdigest()[:10]
        path = ROOT / "packages" / "data-pipeline" / "jobs" / "generated" / f"job_{name_hash}.py"
        risky = idx % 10 == 0
        lines = [
            '"""Scheduled job stub — demo."""',
            "",
            "import logging",
            "",
            "logger = logging.getLogger(__name__)",
            "",
            f"def run_job_{idx}() -> None:",
            '    logger.info("starting synthetic job")',
        ]
        if risky:
            lines += [
                '    logger.warning("gdpr_dump contains ssn_tail=%s dob=%s", "4421", "1988-04-11")',
            ]
        lines += ["    return None", ""]
        write_text(path, "\n".join(lines))


def main() -> None:
    synth_api_modules(220)
    synth_frontend_components(180)
    synth_auth_modules(120)
    synth_payment_mixins(140)
    synth_pipeline_jobs(110)


if __name__ == "__main__":
    main()
