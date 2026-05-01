# ArkoBank architecture (demo)

ArkoBank is organised as a modular platform with clear separation between customer
channels, operator tooling, and payment processing.

```mermaid
flowchart LR
  subgraph Clients
    Portal[Business portal]
    Mobile[Mobile apps]
    Ops[Operator console]
  end

  subgraph Edge
    GW[Mobile gateway Go]
    CDN[CloudFront]
  end

  subgraph Core
    API[FastAPI core]
    AUTH[Auth service]
    PAY[Payments Node service]
  end

  subgraph Data
    PG[(PostgreSQL)]
    ETL[Python pipelines]
    ART[S3 artifacts]
  end

  Portal --> API
  Ops --> API
  Mobile --> GW --> API
  API --> AUTH
  API --> PAY
  API --> PG
  PAY --> PG
  ETL --> PG
  API --> ART
  CDN --> ART
```

## Runtime boundaries

- **Core API** orchestrates accounts, documents, community surfaces, and integrations.
- **Auth service** issues bearer tokens and performs directory lookups for operators.
- **Payments service** executes capture/settlement routines against card rails proxies.
- **Data pipeline** consolidates ledger extracts for regulatory reporting packs.

This document describes the fictional demo system only; deployment topology is not
maintained for production use.
