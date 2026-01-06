# vHcaEmploymentStatus

**Group:** Detail Dataset → Healthcare Productivity

One row for each employment status.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHcaEmploymentStatus |
| Unique Identifier | employmentStatusId |
| Source Pipeline | hcaEmploymentStatus (DR) |

## Columns

**Column count:** 10

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| employmentStatusId | INT64 | The ID of  Employment Status |  |  |
| laborTypeName | STRING | Labor Type Name |  |  |
| laborTypeId | INT64 | The ID of  Labor Type |  |  |
| payrollStatusId | INT64 | The ID of  Payroll Status |  |  |
| payrollStatusCode | STRING | Payroll Status Code |  |  |
| payrollStatusDesc | STRING | Payroll Status Description |  |  |
| payrollSourceId | INT64 | The ID of  payroll status |  |  |
| payrollSourceName | STRING | Payroll source name |  |  |
| deleteSwitch | INT64 | Is deleted switch |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
