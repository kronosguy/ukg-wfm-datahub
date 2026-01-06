# Redaction Policy (Public Repo)

This repo is meant to be safe to share publicly.

## Never publish
- tenant-specific dataset/schema names
- internal URLs/hostnames
- keys/tokens/secrets
- PII (names, emails, phone numbers, addresses, IDs)

## Entity pages must be “metadata-only”
Allowed:
- entity/view names
- field names and descriptions
- conceptual wrapper/pipeline/domain references (non-tenant)

Not allowed:
- sample row values
- extracts that include employee identifiers