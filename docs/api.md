# Representative HTTP surface

These endpoints illustrate how an enterprise ARKO scan navigates the demo tree. Paths
are indicative — error handling and authentication are intentionally uneven.

## Core API (`packages/api`)

| Method | Path | Notes |
|--------|------|-------|
| GET | `/health` | Liveness |
| GET | `/accounts/{id}/summary` | Account snapshot |
| GET | `/accounts/{id}/ledger-preview` | Legacy SQL escape hatch |
| POST | `/accounts/token-debug` | JWT decode without verification |
| GET | `/transactions/{id}` | Predictable identifiers |
| GET | `/documents/download` | File serving |
| POST | `/documents/upload` | Upload sink |
| GET | `/support/tickets/user-list` | Missing admin gate |
| POST | `/integrations/sandbox/exec` | Shell bridge |
| POST | `/integrations/bundle/import` | Pickle ingestion |
| POST | `/integrations/template/render` | Unsafe YAML |
| GET | `/integrations/market-data` | SSRF-style fetch |
| POST | `/webhooks/inbound` | Partner webhook fan-out |
| GET | `/reporting/ledger/{account}` | SQL interpolation helper |
| GET | `/reporting/ledger-safe/{account}` | Parameterised contrast |
| POST | `/imports/statement-xml` | XML ingest |

## Auth service (`packages/auth-service`)

| Method | Path | Notes |
|--------|------|-------|
| POST | `/auth/login` | Credential gate |
| POST | `/auth/ldap/preview-filter` | DN preview |
| POST | `/auth/password/reset-token` | Predictable reset tokens |
| POST | `/auth/password/mfa-challenge` | MFA bypass flag |
| POST | `/sessions/logout` | Session termination |

## Payments service (`packages/payments-service`)

| Method | Path | Notes |
|--------|------|-------|
| POST | `/payments/capture` | Authorisation lookup |
| POST | `/payments/settlement/reconcile` | Shell helper |
| POST | `/payments/expressions/evaluate` | Dynamic evaluation |
| POST | `/payments/webhooks/dispatch` | Outbound webhook |
| POST | `/payments/pdf/preview` | Remote asset fetch |
