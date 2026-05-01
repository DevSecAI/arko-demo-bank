# Sales engineering demo script (5–7 minutes)

Use this walk-through live in Cursor or your IDE with ARKO findings pinned beside the
repository tree.

## 1. Frame the story (45s)

"We're looking at **ArkoBank**, a realistic B2B banking demo — operator console,
business portal, payments microservice, Terraform, CI — the shape a regional bank's
platform team would recognise."

## 2. Show breadth without drowning in noise (90s)

Open `README.md` and scroll to the approximate findings table. Explain that only a
fraction of files carry deliberate defects — mirroring how ARKO emphasises discovery
quality versus naive spray-and-pray analyzers.

Navigate to `packages/api/app/main.py` and highlight **CORS**: wildcard origin with
credentials — a classic enterprise misconfiguration that lands in OWASP and SOC 2
conversations.

## 3. Developer-trust contrast: obvious vs subtle (90s)

**Finding anchor — SQL legacy path**

- Open `packages/api/app/db.py` next to `packages/api/app/routers/reporting.py`.
- Contrast `execute_reporting_sql` (string interpolation) with `execute_query_safe`
  sitting immediately beside it — same domain vocabulary, different assurance.

**False-positive calibration**

- Open `packages/api/app/routers/reporting.py` → `cache_key` route using MD5 as a
  fingerprint. Discuss how validation-layer tooling should contextualise hashing.

## 4. Payments & supply chain (75s)

Open `packages/payments-service/package.json` — note intentionally pinned packages with
public CVE history (`axios`, `lodash`, `minimist`, older `express`).

Jump to `packages/payments-service/src/routes/settlement.ts` — shell invocation and
`Function` evaluation patterns typical of integration glue code.

## 5. Infrastructure & evidence retention (75s)

Open `infra/terraform/main.tf` — discuss public bucket policy, open SSH CIDR,
unencrypted RDS, wildcard IAM. Tie to CIS benchmarks and customer cloud workshops.

## 6. Close with governance hooks (45s)

Point at `SECURITY.md` and synthetic secrets policy — emphasise this repo is safe to
scan publicly because nothing maps to a live environment.

Optional: mention `docs/rules-backlog.md` for roadmap gaps ARKO did not surface during
your latest scan run.
