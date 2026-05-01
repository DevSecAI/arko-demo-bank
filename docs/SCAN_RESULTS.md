# ARKO scan capture

Latest run completed successfully in Cursor (Arko extension). Drop exact counts from the
Arko sidebar or **Export Security Report** into the tables below when you want a
shareable snapshot for PRs or exec reviews.

## How to run the scan (Cursor)

ARKO does not ship a separate terminal CLI in this setup; analysis runs through the **Arko** extension ([DevSecAI](https://www.devsecai.io)).

1. Open this repo as the workspace folder in Cursor (**File → Open Folder…** → `Arko Demo Bank`).
2. Sign in if prompted (**Arko: Sign In** from the Command Palette).
3. Run **Arko: Run Security Scan** (`Cmd+Shift+P` → type `Arko Run Security Scan`).
4. When it finishes, use **Arko: Export Security Report** if you need HTML, or copy totals from the Arko sidebar / Problems panel into the tables below.

## Run metadata

- Scan status: **completed OK** (Cursor / Arko “Run Security Scan”)
- Scan date: **2026-05-01**
- Repository revision (this checkout): **`9ef8418`**
- ARKO version: _(paste from UI if displayed)_
- Rule pack / date: _(paste from export if shown)_

## Executive summary

- Total findings: _(paste from Arko)_
- Critical / high / medium / low: _(paste from Arko)_
- Hackability score (if shown): _(optional)_

## By category

| Category | Count |
|----------|------:|
| | |

## By framework

| Framework | Count |
|-----------|------:|
| | |

## Notes

- Link screenshot(s) or attach exported HTML from **Arko: Export Security Report**.
- Optional: attach `security-report-YYYY-MM-DD.html` path if stored outside the repo.

<!-- Last scan: completed in IDE 2026-05-01 -->
