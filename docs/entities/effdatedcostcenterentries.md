# effDatedCostCenterEntries

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

json with details of cost centers associated with a primary job account.
"List<CostCenterDataExtension>
CostCenterDataExtension :
costCenter
costCenterDescription
costCenterId
effectiveDate
expirationDate"

## Fields

| Field                     | Type   | Description                                                              |
|:--------------------------|:-------|:-------------------------------------------------------------------------|
| effDatedCostCenterEntries | STRING | json with details of cost centers associated with a primary job account. |
|                           |        | "List<CostCenterDataExtension>                                           |
|                           |        | CostCenterDataExtension :                                                |
|                           |        | costCenter                                                               |
|                           |        | costCenterDescription                                                    |
|                           |        | costCenterId                                                             |
|                           |        | effectiveDate                                                            |
|                           |        | expirationDate"                                                          |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.
