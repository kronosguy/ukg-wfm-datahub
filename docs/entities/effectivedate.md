# effectiveDate

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

date when a specific accrual profile becomes effective.

## Fields

| Field         | Type   | Description                                                                                                                                                               |
|:--------------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| effectiveDate | DATE   | date when a specific accrual profile becomes effective.                                                                                                                   |
| effectiveDate | DATE   | date when a specific employment term becomes effective.                                                                                                                   |
| effectiveDate | DATE   | Effective date of a position full time equivalency                                                                                                                        |
| effectiveDate | DATE   | Effective date of a particular job transfer                                                                                                                               |
| effectiveDate | DATE   | id of that particular labor category                                                                                                                                      |
| effectiveDate | DATE   | Represents the end date of a of that particular timeframe.                                                                                                                |
| effectiveDate | DATE   | Start date from where the pay from schedules will start in an assignment                                                                                                  |
| effectiveDate | DATE   | date when a specific schedule group becomes effective.                                                                                                                    |
| effectiveDate | DATE   | id of the status of a position                                                                                                                                            |
| effectiveDate | DATE   | Labor Standard effective start date                                                                                                                                       |
| effectiveDate | DATE   | The effective start date                                                                                                                                                  |
| effectiveDate | DATE   | The effective date                                                                                                                                                        |
| effectiveDate | DATE   | Effective date of the current record (Should not be used for joins)                                                                                                       |
| effectiveDate | DATE   | Effective date of the current record (Should not be used for joins to prevent duplicates use filter like parttionDate >= effectiveDate and parttionDate < expirationDate) |
| effectiveDate | DATE   | The effective date of a generic job.                                                                                                                                      |
| effectiveDate | DATE   | The effective date of a node type in ISO_LOCAL_DATE format (YYYY-MM-DD).                                                                                                  |
| effectiveDate | DATE   | Effective Date                                                                                                                                                            |
| effectiveDate | DATE   | Date badge is effective                                                                                                                                                   |
| effectiveDate | DATE   | Date effective                                                                                                                                                            |
| effectiveDate | DATE   | Cost Center Effective Date                                                                                                                                                |
| effectiveDate | DATE   | Effective date of status                                                                                                                                                  |
| effectiveDate | DATE   | Effective date                                                                                                                                                            |
| effectiveDate | DATE   | Effective Date of Job Transfer                                                                                                                                            |
| effectiveDate | DATE   | Pay rule assignment effective date                                                                                                                                        |
| effectiveDate | DATE   | Primary job assignment effective date                                                                                                                                     |
| effectiveDate | DATE   | Assignent effective date                                                                                                                                                  |
| effectiveDate | DATE   | User account status effective date                                                                                                                                        |
| effectiveDate | DATE   | The effective date span of this pay rule version                                                                                                                          |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.
