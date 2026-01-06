# vHcaPayrollJobs

**Group:** Detail Dataset → Healthcare Productivity

One row for each payroll job.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHcaPayrollJobs |
| Unique Identifier | payrollJobsId |
| Source Pipeline | hcaPayrollJobs (DR) |

## Columns

**Column count:** 9

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| payrollJobsId | INT64 | The ID of  Payroll Jobs |  |  |
| laborCategoryEntryName | STRING | Labor Category Entry Name |  |  |
| laborCategoryEntryId | INT64 | The ID of the Labor Category Entry |  |  |
| genericJobId | INT64 | The ID of the generic job |  |  |
| genericJobName | STRING | Generic Job Name |  |  |
| payrollSourceId | INT64 | The ID of  payroll status |  |  |
| payrollSourceName | STRING | Payroll source name |  |  |
| deleteSwitch | INT64 | Is deleted switch |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
