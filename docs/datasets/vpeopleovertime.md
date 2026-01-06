# vPeopleOvertime

**Group:** Detail Dataset → People Detail Views

- Effective Dated - Personal Overtime Rule Assignments. Dimensions Source Person > Timekeeper > Overriding Personal Rule

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleOvertime |
| Unique Identifier | personId, personalOvertimeAmountTypeId, effectiveDate, expirationDate, overtimeLevel |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 14

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personalOvertimeAmountType | STRING | Personal Overtime Amount type |  |  |
| stopOvertimeSwt | BOOLEAN | Stop overtime switch |  |  |
| useScheduleSwt | BOOLEAN | Use schedule switch |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| personalOvertimeRuleDisplayName | STRING | Personal Overtime Rule display name |  |  |
| personalOvertimeAmountTypeId | INT64 | Personal Overtime Amount type ID |  |  |
| minimumAmount | STRING | Minimum amount |  |  |
| amount | STRING | Overtime Amount |  |  |
| overtimeType | STRING | Overtime type |  |  |
| overtimeTypeId | INT64 | Overtime type ID |  |  |
| overtimeLevel | INT64 | Overtime Level |  |  |
| expirationDate | DATE | Expiration Date |  |  |
| effectiveDate | DATE | Effective Date |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
