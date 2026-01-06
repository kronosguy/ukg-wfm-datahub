# M_Schd_Post_Last_Early_Hrs

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Count of hours that the last schedule posting occurred prior to the posting deadline if the jobs/departments/sites is posted prior to the posting deadline. If the posting was late this will be null.

## Fields

| Field                      | Type   | Description                                                                                                                                                                                            |
|:---------------------------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| M_Schd_Post_Last_Early_Hrs | INT64  | Count of hours that the last schedule posting occurred prior to the posting deadline if the jobs/departments/sites is posted prior to the posting deadline. If the posting was late this will be null. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.
