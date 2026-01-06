# vPeopleApprover

**Group:** Detail Dataset → People Detail Views

- Non-Effective Dated - Hierarchy of Approval (Data still needs validation)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleApprover |
| Unique Identifier | personId |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| personNumber | STRING | person number | PII |  |
| orderNumber | INT64 | order number |  |  |
| fullName | STRING | Full name | PII | Random Name |
| employeeId | INT64 | employee ID |  |  |
| dueDateAmt | INT64 | Due date amount |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
