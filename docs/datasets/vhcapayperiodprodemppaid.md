# vHcaPayperiodProdEmpPaid

**Group:** Detail Dataset → Healthcare Productivity

Pay Period Productivity by Employee Paid provides paid pay period work unit productivity and employee worked hours totals and regular and supplemental labor detailsHistorical Reload Constraint: The historical reload capability of this pipeline is limited by the pay periods defined in vHcaWorkUnitPayPeriod. Specifically, data can be reloaded for a range spanning 26 pay periods in the past up to 5 pay periods in the future relative to the current pay period.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHcaPayperiodProdEmpPaid |
| Unique Identifier | partitionDate,personId,workUnitId |
| Source Pipeline | hcaPayperiodProdEmpPaid (CDC) |

## Columns

**Column count:** 32

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of the payroll detail - use to join to date dimension |  |  |
| startDate | DATE | Start Date of the pay period |  |  |
| endDate | DATE | End date of the pay period |  |  |
| personId | INT64 | The ID of the person referencing the People view |  |  |
| workunitId | INT64 | The ID of the work unit |  |  |
| orgjobId | INT64 | The ID of the org job referencing the businessStructure view |  |  |
| workgroupId | INT64 | The ID of the work group |  |  |
| hcaMetricOtHrsPP | FLOAT | Pay Period Overtime Hours |  |  |
| hcaMetricOtAmtPP | FLOAT | Pay Period Overtime Amount |  |  |
| hcaMetricPaidAgncyAmtPP | FLOAT | Pay Period Paid Agency Amount |  |  |
| hcaMetricPaidAgncyHrsPP | FLOAT | Pay Period Paid Agency Hours |  |  |
| hcaMetricPaidAmtPP | FLOAT | Pay Period Paid Amount |  |  |
| hcaMetricPaidFltinAmtPP | FLOAT | Pay Period Paid Float In Amount |  |  |
| hcaMetricPaidFltinHrsPP | FLOAT | Pay Period Paid Float In Hours |  |  |
| hcaMetricPaidFltoutAmtPP | FLOAT | Pay Period Paid Float Out Amount |  |  |
| hcaMetricPaidFltoutHrsPP | FLOAT | Pay Period Paid Float Out Hours |  |  |
| hcaMetricPaidFtAmtPP | FLOAT | Pay Period Paid Full Time Amount |  |  |
| hcaMetricPaidFtHrsPP | FLOAT | Pay Period Paid Full Time Hours |  |  |
| hcaMetricPaidHrsPP | FLOAT | Pay Period Paid Hours |  |  |
| hcaMetricPaidIntagncyAmtPP | FLOAT | Pay Period Paid Internal Agency Amount |  |  |
| hcaMetricPaidIntagncyHrsPP | FLOAT | Pay Period Paid Internal Agency Hours |  |  |
| hcaMetricPaidPdiemAmtPP | FLOAT | Pay Period Paid Per Diem Amount |  |  |
| hcaMetricPaidPdiemHrsPP | FLOAT | Pay Period Paid Per Diem Hours |  |  |
| hcaMetricPaidPoolAmtPP | FLOAT | Pay Period Paid Pool Amount |  |  |
| hcaMetricPaidPoolHrsPP | FLOAT | Pay Period Paid Pool Hours |  |  |
| hcaMetricPaidPtAmtPP | FLOAT | Pay Period Paid Part Time Amount |  |  |
| hcaMetricPaidPtHrsPP | FLOAT | Pay Period Paid Part Time Hours |  |  |
| hcaMetricPaidExtraptPtAmtPP | FLOAT | Pay Period Paid Extra Part Time Amount |  |  |
| hcaMetricPaidExtraptPtHrsPP | FLOAT | Pay Period Paid Extra Part Time Hours |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| hcaEmploymentStatus | STRING | Employment status of employee: Full time, Part time, Agency |  |  |
| hcaHomeWorkUnit | STRING | Is the employees home workunit true or false |  |  |
