# vHcaPayrollDetail

**Group:** Detail Dataset → Healthcare Productivity

Payroll Detail provides employee hours and amounts based on the payroll import, and paycode and paid job details for each employee and pay period.  Historical Reload Constraint: The historical reload capability of this pipeline is limited by the pay periods defined in vHcaWorkUnitPayPeriod. Specifically, data can be reloaded for a range spanning 26 pay periods in the past up to 5 pay periods in the future relative to the current pay period.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHcaPayrollDetail |
| Unique Identifier | partitionDate,personId,workunitId |
| Source Pipeline | hcaPayrollDetail (CDC) |

## Columns

**Column count:** 15

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of the payroll detail - use to join to date dimension |  |  |
| startDate | DATE | Start Date of the pay period |  |  |
| endDate | DATE | End date of the pay period |  |  |
| personId | INT64 | The ID of the person referencing the People view |  |  |
| workunitId | INT64 | The ID of the work unit |  |  |
| orgjobId | INT64 | The ID of the org job referencing the businessStructure view |  |  |
| hcaMetricsRawPayrollJob | STRING | Payroll Paid Job |  |  |
| hcaMetricsRawPayrollPaidHours | FLOAT | Payroll Hours |  |  |
| hcaMetricsRawPayrollAmount | FLOAT | Payroll Amount | PII |  |
| hcaMetricsRawEmploymentStatus | STRING | Payroll Employment Status |  |  |
| hcaMetricsRawPaycodeName | STRING | Payroll Paycode Name |  |  |
| hcaMetricsRawStandardHours | FLOAT | Payroll Standard Hours |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| hcaEmploymentStatus | STRING | Employment status of employee: Full time, Part time, Agency |  |  |
| hcaHomeWorkUnit | STRING | Is the employees home workunit true or false |  |  |
