#!/usr/bin/env python3
"""Emit large structured constant modules to approximate enterprise repo scale."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET_DIR = ROOT / "packages" / "api" / "app" / "reference_payloads"


def emit_file(idx: int) -> None:
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    path = TARGET_DIR / f"payload_bank_{idx:04d}.py"
    if path.exists():
        return
    lines: list[str] = [
        '"""Synthetic reference rows for reporting joins — ArkoBank demo data only."""',
        "",
        "from __future__ import annotations",
        "",
        f"BATCH_ID = {idx!r}",
        "",
        "ROWS: list[dict[str, object]] = [",
    ]
    for row in range(360):
        code = f"AB{idx:03d}-{row:04d}"
        corridor = "domestic" if row % 4 == 0 else "cross_border"
        lines.append(
            "    {"
            f'"id": "{code}", '
            f'"risk_score": {(idx + row) % 97}, '
            f'"velocity_bucket": {(row // 11) % 6}, '
            f'"corridor": "{corridor}", '
            f'"amount_band": {(idx * row) % 12}'
            "},"
        )
    lines.append("]")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    for idx in range(200):
        emit_file(idx)


if __name__ == "__main__":
    main()
