# vPayCode

**Group:** Detail Dataset → Pay Code/Period Detail Views

- Distinct list of all Paycodes (WFD Configuration).

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPayCode |
| Unique Identifier | payCodeId |
| Source Pipeline | getPayCode (DR) |

## Columns

**Column count:** 14

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| payCodeId | INT64 | Unique identifier for the pay code |  |  |
| payCodeName | STRING | Pay code name |  |  |
| payCodeShortName | STRING | The short name of the paycode. |  |  |
| payCodeType | STRING | Regular, Cascade, Combined |  |  |
| unit | STRING | HOUR, DAY, MONEY |  |  |
| combined | BOOLEAN | Indicates combine pay code |  |  |
| money | BOOLEAN | Indicates money pay code |  |  |
| totals | BOOLEAN | A Boolean indicator of whether or not the pay code tracks totals. |  |  |
| excusedAbsence | BOOLEAN | A Boolean indicator of whether or not the pay code tracks excused absences. |  |  |
| wageMultiplier | FLOAT64 | Indicates pay code multiplier of hours times base wage - 1 is regular, 1.5 is premium pay, etc |  |  |
| wageAddition | FLOAT64 | Pay code wage addition amount |  |  |
| checkAvailability | INT64 | A Boolean indicator of whether or not the paycode affects employee availability. 1 for yes, 0 for no. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| description | STRING | Pay code description |  |  |
