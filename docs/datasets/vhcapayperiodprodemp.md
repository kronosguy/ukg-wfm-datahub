# vHcaPayperiodProdEmp

**Group:** Detail Dataset → Healthcare Productivity

Pay Period Productivity by Employee KPI provides derived kpi pay period work unit productivity and employee worked hours totals and regular and supplemental labor details.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHcaPayperiodProdEmp |
| Unique Identifier | partitionDate,personId,workUnitId |
| Source Pipeline | hcaPayperiodProdEmpDrvdkpi (CDC) |

## Columns

**Column count:** 192

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| workunitId | INT64 | The ID of the work unit |  |  |
| partitionDate | DATE | Represents apply date of the payroll detail - use to join to date dimension |  |  |
| startDate | DATE | Start Date of the pay period |  |  |
| endDate | DATE | End date of the pay period |  |  |
| personId | INT64 | The ID of the person referencing the People view |  |  |
| orgjobId | INT64 | The ID of the org job referencing the businessStructure view |  |  |
| workgroupId | INT64 | The ID of the work group |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
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
| hcaMetricProdOtIntagncyAmtPP | FLOAT | Pay Period Productive Other Internal Agency Amount |  |  |
| hcaMetricProdOtIntagncyHrsPP | FLOAT | Pay Period Productive Other Internal Agency Hours |  |  |
| hcaMetricProdOtPdiemAmtPP | FLOAT | Pay Period  Productive Other Pdiem Amount |  |  |
| hcaMetricProdOtPdiemHrsPP | FLOAT | Pay Period  Productive Other Pdiem Hours |  |  |
| hcaMetricProdOtPoolAmtPP | FLOAT | Pay Period  Productive Other Pool Amount |  |  |
| hcaMetricProdOtPoolHrsPP | FLOAT | Pay Period  Productive Other Pool Hours |  |  |
| hcaMetricProdOtPtAmtPP | FLOAT | Pay Period Productive Other Part Time Amount |  |  |
| hcaMetricProdOtPtHrsPP | FLOAT | Pay Period Productive Other Part Time Hours |  |  |
| hcaMetricProdOthAgncyAmtPP | FLOAT | Pay Period Productive Overtime Internal Agency Amount |  |  |
| hcaMetricProdOthAgncyHrsPP | FLOAT | Pay Period Productive Overtime Internal Agency Hours |  |  |
| hcaMetricProdOthFltinAmtPP | FLOAT | Pay Period  Productive Overtime Pdiem Amount |  |  |
| hcaMetricProdOthFltinHrsPP | FLOAT | Pay Period  Productive Overtime Pdiem Hours |  |  |
| hcaMetricProdOthFltoutAmtPP | FLOAT | Pay Period  Productive Overtime Pool Amount |  |  |
| hcaMetricProdOthFltoutHrsPP | FLOAT | Pay Period  Productive Overtime Pool Hours |  |  |
| hcaMetricProdOthFtAmtPP | FLOAT | Pay Period Productive Overtime Part Time Amount |  |  |
| hcaMetricProdOthFtHrsPP | FLOAT | Pay Period Productive Overtime Part Time Hours |  |  |
| hcaMetricProdOthIntagncyAmtPP | FLOAT | Pay Period  Productive Other Agency Amount |  |  |
| hcaMetricProdOthIntagncyHrsPP | FLOAT | Pay Period  Productive Other Agency Hours |  |  |
| hcaMetricProdOthPdiemAmtPP | FLOAT | Pay Period Productive Other Float In Amount |  |  |
| hcaMetricProdOthPdiemHrsPP | FLOAT | Pay Period Productive Other Float In Hours |  |  |
| hcaMetricProdOthPoolAmtPP | FLOAT | Pay Period Productive Other Float Out Amount |  |  |
| hcaMetricProdOthPoolHrsPP | FLOAT | Pay Period Productive Other Float Out Hours |  |  |
| hcaMetricProdOthPtAmtPP | FLOAT | Pay Period Productive Other Full Time Amount |  |  |
| hcaMetricProdOthPtHrsPP | FLOAT | Pay Period Productive Other Full Time Hours |  |  |
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
| hcaMetricNpRnpPdiemAmtPP | FLOAT | Pay Period Non Productive Per Diem Amount |  |  |
| hcaMetricNpRnpPdiemHrsPP | FLOAT | Pay Period Non Productive Per Diem Hours |  |  |
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
| hcaEmploymentStatus | STRING | Employment status of employee: Full time, Part time, Agency |  |  |
| hcaHomeWorkUnit | STRING | Is the employees home workunit true or false |  |  |
