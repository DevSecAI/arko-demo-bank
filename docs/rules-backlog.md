# Rules backlog — intentional patterns vs ARKO coverage

Use this list after each ARKO scan. Tick items that fired; unchecked rows highlight
candidate roadmap work for the rules engineering team.

_Update this file with real scan IDs once you run ARKO locally._

## Injection & deserialization

- [ ] FastAPI `pickle.load` on uploaded bytes (`integrations` router).
- [ ] SQLAlchemy `text()` concatenation in `accounts` ledger preview.
- [ ] Go mobile gateway string-built SQL (`packages/mobile-gateway`).
- [ ] Node `Function` constructor on JSON-supplied expressions (`payments-service`).
- [ ] PyYAML `yaml.load` (`integrations` router).

## Access control & transport

- [ ] JWT decode without signature verification (`accounts` router).
- [ ] IDOR-style account and transaction lookups without ownership binding.
- [ ] Operator ticket DOM sink (`OperatorTickets.tsx`).
- [ ] Wildcard CORS with credentials (`api` main).

## Cryptography & secrets

- [ ] XOR “rolling crypto” helper (`accounts` router).
- [ ] MD5 password hashing demo endpoint (`reporting` router).
- [ ] TLS verification disabled via httpx / axios agents.
- [ ] Synthetic RSA PEM under `infra/certs/`.
- [ ] Stripe-shaped secret string (`payments-service` config).

## Sensitive logging & monitoring gaps

- [ ] PAN-like value logged in `card_notifier`.
- [ ] Operator bearer prefix logged in data pipeline job.
- [ ] HIPAA-shaped audit fields logged in `nightly_rollup`.
- [ ] Missing structured logging for authentication successes (`auth-service`).
- [ ] Failed transactions not escalated (`nightly_rollup`).

## Infrastructure

- [ ] Public S3 bucket policy (`infra/terraform/main.tf`).
- [ ] Security group SSH open to `0.0.0.0/0`.
- [ ] RDS `storage_encrypted = false`.
- [ ] Lambda role with `AdministratorAccess`.
- [ ] CloudFront viewer protocol `allow-all`.

## CI/CD secrets

- [ ] Synthetic GitHub token & AWS keys embedded in `.github/workflows/ci.yml`.

## Known benign / false-positive candidates

- MD5 cache fingerprint (`reporting` router).
- Public-looking anon JWT in `packages/frontend/src/config/publicEndpoints.ts`.
- Parameterised SQL helper (`execute_query_safe`).
