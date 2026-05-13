# VillaTerras Calculator Runtime Architecture

## Administrative Record

Current repository has transitioned from a generic Streamlit template toward an expandable commercial real estate financial intelligence runtime.

## Runtime Layers

### Layer 1 — Presentation Runtime
- Streamlit UI Runtime
- Sidebar Input Runtime
- Metrics Dashboard Runtime
- Chart Rendering Runtime

### Layer 2 — Financial Runtime
- NOI Runtime
- Cap Rate Runtime
- Debt Service Runtime
- Cash Flow Runtime
- ROI Runtime
- Future IRR Runtime
- Future DSCR Runtime

### Layer 3 — AI Runtime
- AI Advisory Runtime
- Property Question Runtime
- Market Research Runtime
- GPT Integration Runtime

### Layer 4 — Registry Runtime
Planned:
- VillaSchema Runtime
- Property Registry Runtime
- Investor Registry Runtime
- Deal Registry Runtime
- Lead Registry Runtime

### Layer 5 — Intelligence Runtime
Planned:
- GIS Runtime
- Market Signal Runtime
- Lease Intelligence Runtime
- Broker Intelligence Runtime
- Portfolio Intelligence Runtime

## Current Technical Debt

- monolithic frontend runtime
- deprecated OpenAI SDK
- no environment validation
- no Docker runtime
- no persistence layer
- no authentication
- no REST runtime
- no test framework
- no CI/CD governance
- no modular calculator engine

## Required Future Runtime Modules

### calculators/
- irr_runtime.py
- dscr_runtime.py
- equity_multiple_runtime.py
- waterfall_runtime.py
- lease_runtime.py

### ai/
- advisory_runtime.py
- market_research_runtime.py
- lease_ai_runtime.py

### schemas/
- property_schema.py
- investment_schema.py
- lease_schema.py

### governance/
- audit_runtime.py
- validation_runtime.py
- deployment_runtime.py

### deployment/
- Dockerfile
- docker-compose.yml
- github-actions.yml

## Runtime Objective

Convert the current Streamlit prototype into a scalable CRE intelligence runtime capable of:
- underwriting
- portfolio analytics
- market intelligence
- AI-assisted advisory
- GIS analytics
- investor reporting
- acquisition scoring
- enterprise CRE workflows
