# vHcaPayperiodProdEmpProd

**Group:** Detail Dataset → Healthcare Productivity

Pay Period Productivity by Employee Productive provides productive pay period work unit productivity and employee worked hours totals and regular and supplemental labor details. Historical Reload Constraint: The historical reload capability of this pipeline is limited by the pay periods defined in vHcaWorkUnitPayPeriod. Specifically, data can be reloaded for a range spanning 26 pay periods in the past up to 5 pay periods in the future relative to the current pay period.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHcaPayperiodProdEmpProd |
| Unique Identifier | partitionDate,personId,workUnitId |
| Source Pipeline | hcaPayperiodProdEmpProd (CDC) |

## Columns

**Column count:** 64

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of the payroll detail - use to join to date dimension |  |  |
| startDate | DATE | Start Date of the pay period |  |  |
| endDate | DATE | End date of the pay period |  |  |
| personId | INT64 | The ID of the person referencing the People view |  |  |
| workunitId | INT64 | The ID of the work unit |  |  |
| orgjobId | INT64 | The ID of the org job referencing the businessStructure view |  |  |
| workgroupId | INT64 | The ID of the work group |  |  |
| hcaMetricProdAgncyAmtPP | FLOAT | Pay Period Productive Agency Amount |  |  |
| hcaMetricProdAgncyHrsPP | FLOAT | Pay Period Productive Agency Hours |  |  |
| hcaMetricProdAmtPP | FLOAT | Pay Period Productive Amount |  |  |
| hcaMetricProdHrsPP | FLOAT | Pay Period Productive Hours |  |  |
| hcaMetricProdIntagncyAmtPP | FLOAT | Pay Period Productive Internal Agency Amount |  |  |
| hcaMetricProdIntagncyHrsPP | FLOAT | Pay Period Productive Internal Agency Hours |  |  |
| hcaMetricProdOtAgncyAmtPP | FLOAT | Pay Period  Productive Overtime Agency Amount |  |  |
| hcaMetricProdOtAgncyHrsPP | FLOAT | Pay Period  Productive Overtime Agency Hours |  |  |
| hcaMetricProdOtFltinAmtPP | FLOAT | Pay Period Productive Overtime Float In Amount |  |  |
| hcaMetricProdOtFltinHrsPP | FLOAT | Pay Period Productive Overtime Float In Hours |  |  |
| hcaMetricProdOtFltoutAmtPP | FLOAT | Pay Period Productive Overtime Float Out Amount |  |  |
| hcaMetricProdOtFltoutHrsPP | FLOAT | Pay Period Productive Overtime Float Out Hours |  |  |
| hcaMetricProdOtFtAmtPP | FLOAT | Pay Period Productive Overtime Full Time Amount |  |  |
| hcaMetricProdOtFtHrsPP | FLOAT | Pay Period Productive Overtime Full Time Hours |  |  |
| hcaMetricProdOthIntagncyAmtPP | FLOAT | Pay Period Productive Other Internal Agency Amount |  |  |
| hcaMetricProdOthIntagncyHrsPP | FLOAT | Pay Period Productive Other Internal Agency Hours |  |  |
| hcaMetricProdOthPdiemAmtPP | FLOAT | Pay Period  Productive Other Pdiem Amount |  |  |
| hcaMetricProdOthPdiemHrsPP | FLOAT | Pay Period  Productive Other Pdiem Hours |  |  |
| hcaMetricProdOthPoolAmtPP | FLOAT | Pay Period  Productive Other Pool Amount |  |  |
| hcaMetricProdOthPoolHrsPP | FLOAT | Pay Period  Productive Other Pool Hours |  |  |
| hcaMetricProdOthPtAmtPP | FLOAT | Pay Period Productive Other Part Time Amount |  |  |
| hcaMetricProdOthPtHrsPP | FLOAT | Pay Period Productive Other Part Time Hours |  |  |
| hcaMetricProdOtIntagncyAmtPP | FLOAT | Pay Period Productive Overtime Internal Agency Amount |  |  |
| hcaMetricProdOtIntagncyHrsPP | FLOAT | Pay Period Productive Overtime Internal Agency Hours |  |  |
| hcaMetricProdOtPdiemAmtPP | FLOAT | Pay Period  Productive Overtime Pdiem Amount |  |  |
| hcaMetricProdOtPdiemHrsPP | FLOAT | Pay Period  Productive Overtime Pdiem Hours |  |  |
| hcaMetricProdOtPoolAmtPP | FLOAT | Pay Period  Productive Overtime Pool Amount |  |  |
| hcaMetricProdOtPoolHrsPP | FLOAT | Pay Period  Productive Overtime Pool Hours |  |  |
| hcaMetricProdOtPtAmtPP | FLOAT | Pay Period Productive Overtime Part Time Amount |  |  |
| hcaMetricProdOtPtHrsPP | FLOAT | Pay Period Productive Overtime Part Time Hours |  |  |
| hcaMetricProdOthAgncyAmtPP | FLOAT | Pay Period  Productive Other Agency Amount |  |  |
| hcaMetricProdOthAgncyHrsPP | FLOAT | Pay Period  Productive Other Agency Hours |  |  |
| hcaMetricProdOthFltinAmtPP | FLOAT | Pay Period Productive Other Float In Amount |  |  |
| hcaMetricProdOthFltinHrsPP | FLOAT | Pay Period Productive Other Float In Hours |  |  |
| hcaMetricProdOthFltoutAmtPP | FLOAT | Pay Period Productive Other Float Out Amount |  |  |
| hcaMetricProdOthFltoutHrsPP | FLOAT | Pay Period Productive Other Float Out Hours |  |  |
| hcaMetricProdOthFtAmtPP | FLOAT | Pay Period Productive Other Full Time Amount |  |  |
| hcaMetricProdOthFtHrsPP | FLOAT | Pay Period Productive Other Full Time Hours |  |  |
| hcaMetricProdRegAgncyAmtPP | FLOAT | Pay Period  Productive Other Agency Amount |  |  |
| hcaMetricProdRegAgncyHrsPP | FLOAT | Pay Period  Productive Other Agency Hours |  |  |
| hcaMetricProdRegFltinAmtPP | FLOAT | Pay Period Productive Other Float In Amount |  |  |
| hcaMetricProdRegFltinHrsPP | FLOAT | Pay Period Productive Other Float In Hours |  |  |
| hcaMetricProdRegFltoutAmtPP | FLOAT | Pay Period Productive Other Float Out Amount |  |  |
| hcaMetricProdRegFltoutHrsPP | FLOAT | Pay Period Productive Other Float Out Hours |  |  |
| hcaMetricProdRegFtAmtPP | FLOAT | Pay Period Productive Other Full Time Amount |  |  |
| hcaMetricProdRegFtHrsPP | FLOAT | Pay Period Productive Other Full Time Hours |  |  |
| hcaMetricProdRegIntagncyAmtPP | FLOAT | Pay Period Productive Other Internal Agency Amount |  |  |
| hcaMetricProdRegIntagncyHrsPP | FLOAT | Pay Period Productive Other Internal Agency Hours |  |  |
| hcaMetricProdRegPdiemHAmtPP | FLOAT | Pay Period  Productive Other Pdiem Amount |  |  |
| hcaMetricProdRegPdiemHrsPP | FLOAT | Pay Period  Productive Other Pdiem Hours |  |  |
| hcaMetricProdRegPoolAmtPP | FLOAT | Pay Period  Productive Other Pool Amount |  |  |
| hcaMetricProdRegPoolHrsPP | FLOAT | Pay Period  Productive Other Pool Hours |  |  |
| hcaMetricProdRegPtAmtPP | FLOAT | Pay Period Productive Other Part Time Amount |  |  |
| hcaMetricProdRegPtHrsPP | FLOAT | Pay Period Productive Other Part Time Hours |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| hcaEmploymentStatus | STRING | Employment status of employee: Full time, Part time, Agency |  |  |
| hcaHomeWorkUnit | STRING | Is the employees home workunit true or false |  |  |
