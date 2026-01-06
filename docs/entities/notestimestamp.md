# notesTimestamp

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The date time stamp of the note

## Fields

| Field          | Type      | Description                                                                                     |
|:---------------|:----------|:------------------------------------------------------------------------------------------------|
| notesTimestamp | TIMESTAMP | The date time stamp of the note                                                                 |
| notesTimestamp | DATETIME  | The date and time when the note was created or modified; in ISO_LOCAL_DATE format (YYYY-MM-DD). |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.
