# includeSummarySwt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

determines which nodes will appear vKronosDaySummary .  It’s based on linked_category_configuration

## Fields

| Field             | Type    | Description                                                                                                         |
|:------------------|:--------|:--------------------------------------------------------------------------------------------------------------------|
| includeSummarySwt | BOOLEAN | determines which nodes will appear vKronosDaySummary .  It’s based on linked_category_configuration                 |
| includeSummarySwt | BOOLEAN | a boolean that is based on the linked_category_configuration if true the org will be included and false it will not |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.
