# orgId

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Unique ID of Business Structure location - joins to Business Structure Dimension

## Fields

| Field   | Type    | Description                                                                                                                                                                                                      |
|:--------|:--------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| orgId   | INT64   | Unique ID of Business Structure location - joins to Business Structure Dimension                                                                                                                                 |
| orgId   | INT64   | Org ID of the approved worked job                                                                                                                                                                                |
| orgId   | INT64   | orgID for which the change occured                                                                                                                                                                               |
| orgId   | INT64   | orgId  for which the change occured                                                                                                                                                                              |
| orgId   | DATE    | The date for which a record transaction was made                                                                                                                                                                 |
| orgId   | INT64   | orgId for which the change occured                                                                                                                                                                               |
| orgId   | INT64   | Business structure org id                                                                                                                                                                                        |
| orgId   | INT64   | The ID of the location from the businessStructure view.                                                                                                                                                          |
| orgId   | INT64   | Organization Identifier                                                                                                                                                                                          |
| orgId   | INTEGER | Organization Identifier                                                                                                                                                                                          |
| orgId   | INT64   | Primary Key (  Mimics behavior from ORG_IDS_ID in WFAN) DOES NOT contain all previous versions of the org path which are currently active.  - Should be used for all joins to detail fact Views.                 |
| orgId   | INT64   | Unique identifier of Primary Business Structure location                                                                                                                                                         |
| orgId   | INT64   | The organization id associated with the generic location                                                                                                                                                         |
| orgId   | INT64   | Self related orgId                                                                                                                                                                                               |
| orgId   | INT64   | The orgId for the posted job                                                                                                                                                                                     |
| orgId   | INTEGER | The orgId for the posted job                                                                                                                                                                                     |
| orgId   | STRING  | Unique ID of Business Structure location - joins to Business Structure Dimension                                                                                                                                 |
| orgId   | INT64   | Unique ID of Business Structure location - joins to Business Structure Dimension Note: If the punch is associated with a work transfer this value is populated and represents the org the work is transferred to |
| orgId   | INT64   | Unique identifier of Primary Business Structure location of the employee associated with the transaction - Joins to Business Structure dimensions                                                                |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.
