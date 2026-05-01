# ArkoBank — ARKO Demo Repository

ArkoBank is a **fictional** B2B digital banking platform demo: business current
accounts, card issuing, payments, and a developer API. This repository is built to
look like a mid-sized fintech codebase while embedding **intentional** security
anti-patterns for **ARKO** scanning, sales demos, and security education.

**This is not production software.** Do not deploy it or connect it to real money,
identity, or customer data. See [SECURITY.md](./SECURITY.md).

## Who this is for

- Enterprise sales / solutions engineering (CISO-facing demos)
- Security content (walkthroughs, conference talks)
- Customer onboarding (“clone, scan, compare to your SDLC”)
- Internal regression testing for static-analysis rules

## Repository layout

| Area | Stack |
|------|--------|
| `packages/frontend` | React 18, TypeScript, Vite — operator dashboard & customer portal |
| `packages/api` | FastAPI — core banking API |
| `packages/auth-service` | FastAPI — JWT, OAuth-shaped flows, MFA |
| `packages/payments-service` | Node.js + TypeScript — card & gateway integration |
| `packages/data-pipeline` | Python — reporting ETL jobs |
| `packages/mobile-gateway` | Go — thin mobile BFF |
| `infra/terraform` | AWS-shaped IaC |
| `infra/kubernetes` | Helm-style manifests |
| `.github/workflows` | CI/CD pipelines |

Architecture overview: [docs/architecture.md](./docs/architecture.md).  
API surface (representative): [docs/api.md](./docs/api.md).

## Licence

MIT — see [LICENSE](./LICENSE).

## How to scan with ARKO

1. Clone this repository locally or open it in your IDE with the ARKO integration.
2. Run an ARKO repository scan against the workspace root (`arko-demo-bank`).
3. Review findings by category and framework mapping in the ARKO UI or exported report.

**Note:** Dependency versions are pinned to include known CVEs on purpose for
software-composition demos. Do not `npm install` / `pip install` these stacks into
production systems without upgrading.

## Repository scale (authoring snapshot)

Measured locally with tooling that skips `node_modules`, build artifacts under `dist/`,
and binary blobs:

- **~1,050** text/source files
- **~87k** lines of code and configuration (excluding vendored dependencies)

Re-run your own metrics before publishing if you add packages.

## Approximate findings preview (illustrative)

Counts vary by ARKO version and rule set. The table below is a **planning
estimate** for what this demo is designed to surface; replace with your actual
scan summary after running ARKO (see [docs/SCAN_RESULTS.md](./docs/SCAN_RESULTS.md)).

| Category | Approx. findings |
|----------|-------------------|
| Injection (SQL, command, LDAP, XSS, path traversal, XXE) | 25–45 |
| Broken access control & identity | 18–30 |
| Cryptography & secrets | 22–38 |
| Authentication & session management | 12–22 |
| Sensitive logging & PCI/GDPR-style data handling | 15–28 |
| Insecure deserialization | 6–12 |
| SSRF | 6–10 |
| Vulnerable / outdated components (SCA) | 10–25 |
| Logging, monitoring, operational gaps | 8–18 |
| Infrastructure & IaC misconfigurations | 20–40 |

## Demo script

See [docs/demo-script.md](./docs/demo-script.md) for a 5–7 minute SE walkthrough.

## Rules backlog (embedded vs detected)

See [docs/rules-backlog.md](./docs/rules-backlog.md) for intentional patterns that
may not yet appear in ARKO output — useful for roadmap prioritisation.

## Publishing on GitHub

Target organisation in the brief is **`Arko-DevSecAI-Prod`**. This checkout was built
under a local workspace; **confirm whether you want the public repo under that org or a
personal account** before the first push. After you run an ARKO scan, paste the summary
into `docs/SCAN_RESULTS.md` and attach it to your PR description.

## Trademark notice

“ArkoBank” is a fictional name. This demo is not affiliated with any real
financial institution.
