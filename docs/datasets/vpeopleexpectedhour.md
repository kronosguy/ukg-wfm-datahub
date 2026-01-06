# vPeopleExpectedHour

**Group:** Detail Dataset → People Detail Views

- Non-Effective Dated - Expected Hours by Type (Daily, Weekly, Payperiod)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleExpectedHour |
| Unique Identifier | personId,timePeriodTypeId |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 5

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| timePeriodTypeId | INT64 | Time period type ID |  |  |
| timePeriodType | STRING | Time period type - week, day, etc |  |  |
| expectedHoursQuantity | FLOAT64 | Expected hours quantity |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
