# "_User" Views with row level security

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The four Views in the Summary dataset each have a "_User" version of it.   This view replicates the data for each user and provides the email address of the user as a column,  these are used to provide Row Level Security if you are using a BI tool that will be managing the user authentication itself and passing the email address as part of the "Where" clause.   (PowerBI)

## Fields

| Field                                 | Description                                                                                                                                                                                                                                                                                                                                                                           |
|:--------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "_User" Views with row level security | The four Views in the Summary dataset each have a "_User" version of it.   This view replicates the data for each user and provides the email address of the user as a column,  these are used to provide Row Level Security if you are using a BI tool that will be managing the user authentication itself and passing the email address as part of the "Where" clause.   (PowerBI) |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.
