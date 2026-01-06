# vHcaPayperiodProdEmpDrvdkpi

**Group:** Detail Dataset → Healthcare Productivity

Pay Period Productivity by Employee KPI provides derived kpi pay period work unit productivity and employee combinedm productive and non productive hours totals. Historical Reload Constraint: The historical reload capability of this pipeline is limited by the pay periods defined in vHcaWorkUnitPayPeriod. Specifically, data can be reloaded for a range spanning 26 pay periods in the past up to 5 pay periods in the future relative to the current pay period.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHcaPayperiodProdEmpDrvdkpi |
| Unique Identifier | partitionDate,workunitId |
| Source Pipeline | hcaPayperiodProdEmpDrvdkpi (CDC) |
| Scrubbing | hcaPayperiodProdEmpDrvdkpi |

## Columns

**Column count:** 52

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of the payroll detail - use to join to date dimension |  |  |
| startDate | DATE | Start Date of the pay period |  |  |
| endDate | DATE | End date of the pay period |  |  |
| personId | INT64 | The ID of the person referencing the People view |  |  |
| workunitId | INT64 | The ID of the work unit |  |  |
| orgjobId | INT64 | The ID of the org job referencing the businessStructure view |  |  |
| workgroupId | INT64 | The ID of the work group |  |  |
| hcaDrvdkpiCombTotpaidAgncyAmtPP | FLOAT | Pay Period Combined Agency Amount Total |  |  |
| hcaDrvdkpiCombTotpaidAgncyHrsPP | FLOAT | Pay Period Combined Agency Hours Total |  |  |
| hcaDrvdkpiCombTotpaidFltinAmtPP | FLOAT | Pay Period Combined Float In Amount Total |  |  |
| hcaDrvdkpiCombTotpaidFltinHrsPP | FLOAT | Pay Period Combined Float In Hours Total |  |  |
| hcaDrvdkpiCombTotpaidFtAmtPP | FLOAT | Pay Period Combined  Full Time Amount Total |  |  |
| hcaDrvdkpiCombTotpaidFtHrsPP | FLOAT | Pay Period Combined Full Time Hours Total |  |  |
| hcaDrvdkpiCombTotpaidIntagncyAmtPP | FLOAT | Pay Period Combined Internal Agency Amount Total |  |  |
| hcaDrvdkpiCombTotpaidIntagncyHrsPP | FLOAT | Pay Period Combined Internal Agency Hours Total |  |  |
| hcaDrvdkpiCombTotpaidPdiemAmtPP | FLOAT | Pay Period Combined Per Diem Amount Total |  |  |
| hcaDrvdkpiCombTotpaidPdiemHrsPP | FLOAT | Pay Period Combined Per Diem Hours Total |  |  |
| hcaDrvdkpiCombTotpaidPoolAmtPP | FLOAT | Pay Period Combined Pool Amount Total |  |  |
| hcaDrvdkpiCombTotpaidPoolHrsPP | FLOAT | Pay Period Combined Pool Hours Total |  |  |
| hcaDrvdkpiCombTotpaidPtAmtPP | FLOAT | Pay Period Combined Part Time Amount Total |  |  |
| hcaDrvdkpiCombTotpaidPtHrsPP | FLOAT | Pay Period Combined Part Time Hours Total |  |  |
| hcaDrvdkpiNpTotAgncyAmtPP | FLOAT | Pay Period Non-Productive Agency Amount Total |  |  |
| hcaDrvdkpiNpTotAgncyHrsPP | FLOAT | Pay Period Non-Productive Agency Hours Total |  |  |
| hcaDrvdkpiNpTotFltinAmtPP | FLOAT | Pay Period Non-Productive Float In Amount Total |  |  |
| hcaDrvdkpiNpTotFltinHrsPP | FLOAT | Pay Period Non-Productive Float In Hours Total |  |  |
| hcaDrvdkpiNpTotFtAmtPP | FLOAT | Pay Period Non-Productive Full Time Amount Total |  |  |
| hcaDrvdkpiNpTotFtHrsPP | FLOAT | Pay Period Non-Productive Full Time Hours Total |  |  |
| hcaDrvdkpiNpTotIntagncyAmtPP | FLOAT | Pay Period Non-Productive Internal Agency Amount Total |  |  |
| hcaDrvdkpiNpToIntagncyHrsPP | FLOAT | Pay Period Non-Productive Internal Agency Hours Total |  |  |
| hcaDrvdkpiNpTotPdiemAmtPP | FLOAT | Pay Period Non-Productive Per Diem Amount Total |  |  |
| hcaDrvdkpiNpTotPdiemHrsPP | FLOAT | Pay Period Non-Productive Per Diem Hours Total |  |  |
| hcaDrvdkpiNpTotPoolAmtPP | FLOAT | Pay Period Non-Productive Pool Amount Total |  |  |
| hcaDrvdkpiNpTotPoolHrsPP | FLOAT | Pay Period Non-Productive Pool Hours Total |  |  |
| hcaDrvdkpiNpTotPtAmtPP | FLOAT | Pay Period Non-Productive Part Time Amount Total |  |  |
| hcaDrvdkpiNpTotPtHrsPP | FLOAT | Pay Period Non-Productive Part Time Hours Total |  |  |
| hcaDrvdkpiProdTotAgncyAmtPP | FLOAT | Pay Period Productive Agency Amount Total |  |  |
| hcaDrvdkpiProdTotAgncyHrsPP | FLOAT | Pay Period Productive Agency Hours Total |  |  |
| hcaDrvdkpiProdTotFltinAmtPP | FLOAT | Pay Period Productive Float In Amount Total |  |  |
| hcaDrvdkpiProdTotFltinHrsPP | FLOAT | Pay Period Productive Float In Hours Total |  |  |
| hcaDrvdkpiProdTotFtAmtPP | FLOAT | Pay Period Productive Full Time Amount Total |  |  |
| hcaDrvdkpiProdTotFtHrsPP | FLOAT | Pay Period Productive Full Time Hours Total |  |  |
| hcaDrvdkpiProdTotIntagncyAmtPP | FLOAT | Pay Period Productive Internal Agency Amount Total |  |  |
| hcaDrvdkpiProdTotIntagncyHrsPP | FLOAT | Pay Period Productive Internal Agency Hours Total |  |  |
| hcaDrvdkpiProdTotPdiemAmtPP | FLOAT | Pay Period Productive Per Diem Amount Total |  |  |
| hcaDrvdkpiProdTotPoolAmtPP | FLOAT | Pay Period Productive Pool Amount Total |  |  |
| hcaDrvdkpiProdTotPoolHrsPP | FLOAT | Pay Period Productive Pool Hours Total |  |  |
| hcaDrvdkpiProdTotPtAmtPP | FLOAT | Pay Period Productive Part Time Amount Total |  |  |
| hcaDrvdkpiProdTotPtHrsPP | FLOAT | Pay Period Productive Part Time Hours Total |  |  |
| hcaDrvdkpiProdTotPdiemHrsPP | FLOAT | Pay Period Productive Per Diem Hours Total |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| hcaHomeWorkUnit | STRING | Is the employees home workunit true or false |  |  |
| hcaEmploymentStatus | STRING | Employment status of employee: Full time, Part time, Agency |  |  |
