# version

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Unix timestamp that logs the date/time of change

## Fields

| Field   | Type    | Description                                                                                              |
|:--------|:--------|:---------------------------------------------------------------------------------------------------------|
| version | INT64   | Unix timestamp that logs the date/time of change                                                         |
| version | INT64   | The version of a labor forecast limit.                                                                   |
| version | INT64   | The version of a labor standard.                                                                         |
| version | INT64   | The version of a labor task to allow support for optimistic locking.                                     |
| version | INT64   | The version of a Volume Driver.                                                                          |
| version | INTEGER | The current version of a volume driver action. ** not used by Data Hub                                   |
| version | INT64   | The version of hours of operation                                                                        |
| version | INT64   | The current version of the entity. This is used to ensure that an entity is not updated with stale data. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.
