# expirationDate

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

date when a specific accrual profile expires.

## Fields

| Field          | Type   | Description                                                                                                                                                                |
|:---------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| expirationDate | DATE   | date when a specific accrual profile expires.                                                                                                                              |
| expirationDate | DATE   | date when a specific employment term expires.                                                                                                                              |
| expirationDate | DATE   | Employee standard hours of a position full time equivalency                                                                                                                |
| expirationDate | DATE   | Expiration date of a particular job transfer                                                                                                                               |
| expirationDate | DATE   | Business structure (org) ID associated with a job account                                                                                                                  |
| expirationDate | DATE   | Represents whether a particular position is primary in that time range.                                                                                                    |
| expirationDate | DATE   | End date from where the pay from schedules will end in an assignment                                                                                                       |
| expirationDate | DATE   | date when a specific schedule group expires.                                                                                                                               |
| expirationDate | DATE   | Represents the end date of a of that particular timeframe.                                                                                                                 |
| expirationDate | DATE   | Labor Standard effective end date                                                                                                                                          |
| expirationDate | DATE   | The effective end date                                                                                                                                                     |
| expirationDate | DATE   | Expiration date of the current record (Should not be used for joins)                                                                                                       |
| expirationDate | DATE   | Expiration date of the current record (Should not be used for joins to prevent duplicates use filter like parttionDate >= effectiveDate and parttionDate < expirationDate) |
| expirationDate | DATE   | The expiration date of a generic job.                                                                                                                                      |
| expirationDate | DATE   | The expiration date of a node type in ISO_LOCAL_DATE format (YYYY-MM-DD).                                                                                                  |
| expirationDate | DATE   | Expiration date                                                                                                                                                            |
| expirationDate | DATE   | Expiration Date                                                                                                                                                            |
| expirationDate | DATE   | Date badge expires                                                                                                                                                         |
| expirationDate | DATE   | Date expires                                                                                                                                                               |
| expirationDate | DATE   | Cost Center Expiration Date                                                                                                                                                |
| expirationDate | DATE   | Expiration Date of Job Transfer                                                                                                                                            |
| expirationDate | DATE   | Pay rule assignment expiration date                                                                                                                                        |
| expirationDate | DATE   | Primary job assignment expiration date                                                                                                                                     |
| expirationDate | DATE   | Assignment expiration date                                                                                                                                                 |
| expirationDate | DATE   | User account status expiration date                                                                                                                                        |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.
