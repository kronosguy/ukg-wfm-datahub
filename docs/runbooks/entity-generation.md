# Runbook: Entity Doc Generation (Public-Safe)

## Goal
Generate entity documentation from a Data Dictionary workbook without committing sensitive source files.

## Rules
- Do not commit the Excel workbook to a public repo.
- Do not publish tenant-specific dataset/schema names.
- Do not include sample employee data or any PII.

## Steps
1) Get the dictionary workbook (local, OneDrive, SharePoint, etc.)
2) Run:

```bash
python tools/generate_entities.py --dictionary /path/to/dictionary.xlsx --out docs/entities
