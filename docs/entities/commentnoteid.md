# commentNoteId

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Schedule Audit Comment Note ID

## Fields

| Field         | Type   | Description                                |
|:--------------|:-------|:-------------------------------------------|
| commentNoteId | INT64  | Schedule Audit Comment Note ID             |
| commentNoteId | INT64  | The ID for the comment and attached notes. |
| commentNoteId | INT64  | Schedule leave edit comment note ID        |
| commentNoteId | INT64  | Schedule open shift comment note ID        |
| commentNoteId | INT64  | The ID for the note.                       |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.
