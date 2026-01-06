# vHcaPayperiodProdEmpNonProd

**Group:** Detail Dataset → Healthcare Productivity

Pay Period Productivity by Employee Non Productive provides non-productive pay period work unit productivity and employee worked hours totals and regular and supplemental labor details. (This is a combination of views vHcaPayperiodProdEmpDrvdkpi + vHcaPayperiodProdEmpNonProd + vHcaPayperiodProdEmpPaid +	vHcaPayperiodProdEmpProd) Historical Reload Constraint: The historical reload capability of this pipeline is limited by the pay periods defined in vHcaWorkUnitPayPeriod. Specifically, data can be reloaded for a range spanning 26 pay periods in the past up to 5 pay periods in the future relative to the current pay period.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHcaPayperiodProdEmpNonProd |
| Unique Identifier | partitionDate,personId,workUnitId |
| Source Pipeline | hcaPayperiodProdEmpNonProd (CDC) |

## Columns

**Column count:** 74

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of the payroll detail - use to join to date dimension |  |  |
| startDate | DATE | Start Date of the pay period |  |  |
| endDate | DATE | End date of the pay period |  |  |
| personId | INT64 | The ID of the person referencing the People view |  |  |
| workunitId | INT64 | The ID of the work unit |  |  |
| orgjobId | INT64 | The ID of the org job referencing the businessStructure view |  |  |
| workgroupId | INT64 | The ID of the work group |  |  |
| hcaMetricNpAmtPP | FLOAT | Pay Period Non Productive Amount |  |  |
| hcaMetricNpHrsPP | FLOAT | Pay Period Non Productive Hours |  |  |
| hcaMetricNpOthAgncyAmtPP | FLOAT | Pay Period Non Productive Other Agency Amount |  |  |
| hcaMetricNpOthAgncyHrsPP | FLOAT | Pay Period Non Productive Other Agency Hours |  |  |
| hcaMetricNpOthFltinAmtPP | FLOAT | Pay Period Non Productive Other Float In Amount |  |  |
| hcaMetricNpOthFltinHrsPP | FLOAT | Pay Period Non Productive Other Float In Hours |  |  |
| hcaMetricNpOthFltoutAmtPP | FLOAT | Pay Period Non Productive Other Float Out Amount |  |  |
| hcaMetricNpOthFltoutHrsPP | FLOAT | Pay Period Non Productive Other Float Out Hours |  |  |
| hcaMetricNpOthFtAmtPP | FLOAT | Pay Period Non Productive Other Full Time Amount |  |  |
| hcaMetricNpFtHrsPP | FLOAT | Pay Period Non Productive Other Full Time Hours |  |  |
| hcaMetricNpOthPdiemAmtPP | FLOAT | Pay Period Non Productive Other Pdiem Amount |  |  |
| hcaMetricNpOthPdiemHrsPP | FLOAT | Pay Period Non Productive Other Pdiem Hours |  |  |
| hcaMetricNpOthPoolAmtPP | FLOAT | Pay Period Non Productive Other Pool Amount |  |  |
| hcaMetricNpOthPoolHrsPP | FLOAT | Pay Period Non Productive Other Pool Hours |  |  |
| hcaMetricNpOthPtAmtPP | FLOAT | Pay Period Non Productive Other Part Time Amount |  |  |
| hcaMetricNpOthPtHrsPP | FLOAT | Pay Period Non Productive Other Part Time Hours |  |  |
| hcaMetricNpRnpAgncyAmtPP | FLOAT | Pay Period Non Productive Agency Amount |  |  |
| hcaMetricNpRnpAgncyHrsPP | FLOAT | Pay Period Non Productive Agency Hours |  |  |
| hcaMetricNpRnpFltinAmtPP | FLOAT | Pay Period Non Productive Float In Amount |  |  |
| hcaMetricNpRnpFltinHrsPP | FLOAT | Pay Period Non Productive Float In Hours |  |  |
| hcaMetricNpRnpFltoutAmtPP | FLOAT | Pay Period Non Productive Float Out Amount |  |  |
| hcaMetricNpRnpFltoutHrsPP | FLOAT | Pay Period Non Productive Float Out Hours |  |  |
| hcaMetricNpRnpFtAmtPP | FLOAT | Pay Period Non Productive Full Time Amount |  |  |
| hcaMetricNpRnpFtHrsPP | FLOAT | Pay Period Non Productive Full Time Hours |  |  |
| hcaMetricNpRnpIntagncyAmtPP | FLOAT | Pay Period Non Productive Internal Agency Amount |  |  |
| hcaMetricNpRnpIntagncyHrsPP | FLOAT | Pay Period Non Productive Internal Agency Hours |  |  |
| hcaMetricNpRnpPdiemAmtPP | FLOAT | Pay Period Non Productive Pdiem Amount |  |  |
| hcaMetricNpRnpPdiemHrsPP | FLOAT | Pay Period Non Productive Pdiem Hours |  |  |
| hcaMetricNpRnpPoolAmtPP | FLOAT | Pay Period Non Productive Pool Amount |  |  |
| hcaMetricNpRnpPoolHrsPP | FLOAT | Pay Period Non Productive Pool Hours |  |  |
| hcaMetricNpRnpPtAmtPP | FLOAT | Pay Period Non Productive Part Time Amount |  |  |
| hcaMetricNpRnpPtHrsPP | FLOAT | Pay Period Non Productive Part Time Hours |  |  |
| hcaMetricNpRnp1AgncyAmtPP | FLOAT | Pay Period Non Productive1 Agency Amount |  |  |
| hcaMetricNpRnp1AgncyHrsPP | FLOAT | Pay Period Non Productive1 Agency Hours |  |  |
| hcaMetricNpRnp1FltinAmtPP | FLOAT | Pay Period Non Productive1 Float In Amount |  |  |
| hcaMetricNpRnp1FltinHrsPP | FLOAT | Pay Period Non Productive1 Float In Hours |  |  |
| hcaMetricNpRnp1FltoutAmtPP | FLOAT | Pay Period Non Productive1 Float Out Amount |  |  |
| hcaMetricNpRnp1FltoutHrsPP | FLOAT | Pay Period Non Productive1 Float Out Hours |  |  |
| hcaMetricNpRnp1FtAmtPP | FLOAT | Pay Period Non Productive1 Full Time Amount |  |  |
| hcaMetricNpRnp1FtHrsPP | FLOAT | Pay Period Non Productive1 Full Time Hours |  |  |
| hcaMetricNpRnp1IntagncyAmtPP | FLOAT | Pay Period Non Productive1 Internal Agency Amount |  |  |
| hcaMetricNpRnp1IntagncyHrsPP | FLOAT | Pay Period Non Productive1 Internal Agency Hours |  |  |
| hcaMetricNpRnp1PdiemAmtPP | FLOAT | Pay Period Non Productive1 Pdiem Amount |  |  |
| hcaMetricNpRnp1PdiemHrsPP | FLOAT | Pay Period Non Productive1 Pdiem Hours |  |  |
| hcaMetricNpRnp1PoolAmtPP | FLOAT | Pay Period Non Productive1 Pool Amount |  |  |
| hcaMetricNpRnp1PoolHrsPP | FLOAT | Pay Period Non Productive1 Pool Hours |  |  |
| hcaMetricNpRnp1PtAmtPP | FLOAT | Pay Period Non Productive1 Part Time Amount |  |  |
| hcaMetricNpRnp1PtHrsPP | FLOAT | Pay Period Non Productive1 Part Time Hours |  |  |
| hcaMetricNpRnp2AgncyAmtPP | FLOAT | Pay Period Non Productive2 Agency Amount |  |  |
| hcaMetricNpRnp2AgncyHrsPP | FLOAT | Pay Period Non Productive2 Agency Hours |  |  |
| hcaMetricNpRnp2FltinAmtPP | FLOAT | Pay Period Non Productive2 Float In Amount |  |  |
| hcaMetricNpRnp2FltinHrsPP | FLOAT | Pay Period Non Productive2 Float In Hours |  |  |
| hcaMetricNpRnp2FltoutAmtPP | FLOAT | Pay Period Non Productive2 Float Out Amount |  |  |
| hcaMetricNpRnp2FltoutHrsPP | FLOAT | Pay Period Non Productive2 Float Out Hours |  |  |
| hcaMetricNpRnp2FtAmtPP | FLOAT | Pay Period Non Productive2 Full Time Amount |  |  |
| hcaMetricNpRnp2FtHrsPP | FLOAT | Pay Period Non Productive2 Full Time Hours |  |  |
| hcaMetricNpRnp2IntagncyAmtPP | FLOAT | Pay Period Non Productive2 Internal Agency Amount |  |  |
| hcaMetricNpRnp2IntagncyHrsPP | FLOAT | Pay Period Non Productive2 Internal Agency Hours |  |  |
| hcaMetricNpRnp2PoolAmtPP | FLOAT | Pay Period Non Productive2 Pool Amount |  |  |
| hcaMetricNpRnp2PoolHrsPP | FLOAT | Pay Period Non Productive2 Pool Hours |  |  |
| hcaMetricNpRnp2PtAmtPP | FLOAT | Pay Period Non Productive2 Part Time Amount |  |  |
| hcaMetricNpRnp2PtHrsPP | FLOAT | Pay Period Non Productive2 Part Time Hours |  |  |
| hcaMetricNpRnp2PdiemAmtPP | FLOAT | Pay Period Non Productive2 Pdiem Amount |  |  |
| hcaMetricRnp2PdiemHrsPP | FLOAT | Pay Period Non Productive2 Pdiem Hours |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| hcaEmploymentStatus | STRING | Employment status of employee: Full time, Part time, Agency |  |  |
| hcaHomeWorkUnit | STRING | Is the employees home workunit true or false |  |  |
