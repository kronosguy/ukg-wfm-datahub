# vHcaEmployee

**Group:** Detail Dataset → Healthcare Productivity

Provides employee status and home work unit employee and pay period.  Historical Reload Constraint: The historical reload capability of this pipeline is limited by the pay periods defined in vHcaWorkUnitPayPeriod. Specifically, data can be reloaded for a range spanning 26 pay periods in the past up to 5 pay periods in the future relative to the current pay period.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHcaEmployee |
| Unique Identifier |  |
| Source Pipeline | hcaEmployee (CDC) |

## Columns

**Column count:** 8

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of the payroll detail - use to join to date dimension |  |  |
| startDate | DATE | Start Date of the pay period |  |  |
| endDate | DATE | End date of the pay period |  |  |
| personId | INT64 | The ID of the person referencing the People view |  |  |
| workunitId | INT64 | The ID of the work unit |  |  |
| orgjobId | INT64 | The ID of the org job referencing the businessStructure view |  |  |
| hcaEmploymentStatus | STRING | Employment status of employee: Full time, Part time, Agency |  |  |
| hcaHomeWorkUnit | STRING | Is the employees home workunit true or false |  |  |
