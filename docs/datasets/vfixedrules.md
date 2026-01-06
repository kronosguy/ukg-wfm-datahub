# vFixedRules

**Group:** Detail Dataset → Timekeeping Setup

- Fixed rules identify constant pay policies that are assigned to employees, such as pay periods, day divides, and the Hours belong to option

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vFixedRules |
| Unique Identifier | fixedRulesId |
| Source Pipeline | fixedRules (DR) |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| fixedRulesName | STRING | The name of a fixed rule. |  |  |
| payPeriodType | STRING | The type of a pay period associated with a fixed rule. |  |  |
| dayDivide | TIME | The time of day which divides one day from another in ISO_LOCAL_TIME format (HH:mm:ss.SSS). |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| fixedRulesId | INT64 | The ID of a fixed rule. |  |  |
| referencedDay | INT64 | The reference day associated with fixed rule |  |  |
| applyToDate | STRING | Fixed rule apply date |  |  |
