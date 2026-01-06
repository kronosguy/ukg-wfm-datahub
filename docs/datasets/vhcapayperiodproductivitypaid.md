# vHcaPayperiodProductivityPaid

**Group:** Detail Dataset → Healthcare Productivity

Pay Period Productivity Paid provides pay period work unit productivity, regular and supplemental labor details, and fixed and variable targets compared to actual hours and amounts. Historical Reload Constraint: The historical reload capability of this pipeline is limited by the pay periods defined in vHcaWorkUnitPayPeriod. Specifically, data can be reloaded for a range spanning 26 pay periods in the past up to 5 pay periods in the future relative to the current pay period.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHcaPayperiodProductivityPaid |
| Unique Identifier | partitionDate,workunitId |
| Source Pipeline | hcaPayperiodProductivityPaid (CDC) |

## Columns

**Column count:** 58

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of the payroll detail - use to join to date dimension |  |  |
| startDate | DATE | Start Date of the pay period |  |  |
| endDate | DATE | End date of the pay period |  |  |
| workunitId | INT64 | The ID of the work unit |  |  |
| hcaTgtHcafixedMetricPaidAmtPPdef | FLOAT | Pay Period Fixed Paid Amount Target - Default |  |  |
| hcaTgtHcafixedMetricPaidAmtPPalt | FLOAT | Pay Period Fixed Paid Amount Target - Alternate |  |  |
| hcaTgtHcafixedMetricPaidHrsPPdef | FLOAT | Pay Period Fixed Paid Hours Target - Default |  |  |
| hcaTgtHcafixedMetricPaidHrsPP | FLOAT | Pay Period Fixed Paid Hours Target - Alternate |  |  |
| hcaTgtHcaVariableMetricPaidAmtPPdef | FLOAT | Pay Period Variable Paid Amount Target - Default |  |  |
| hcaTgtHcaVariableMetricPaidAmtPPalt | FLOAT | Pay Period Variable Paid Amount Target - Alternate |  |  |
| hcaTgtHcaVariableMetricPaidHrsPPdef | FLOAT | Pay Period Variable Paid Hours Target - Default |  |  |
| hcaTgtHcaVariableMetricPaidHrsPPalt | FLOAT | Pay Period Variable Paid Hours Target - Alternate |  |  |
| hcaDrvdkpiPaidAmtTgtPerVolWeightedPPDef | FLOAT | Pay Period Paid Amount Target/Unit Of Service - Default |  |  |
| hcaDrvdkpiPaidAmtTgtPerVolWeightedPPAlt | FLOAT | Pay Period Paid Amount Target/Unit Of Service - Alternate |  |  |
| hcaDrvdkpiPaidAmtTgtPPDef | FLOAT | Pay Period Paid Amount Target - Default |  |  |
| hcaDrvdkpiPaidAmtTgtPPAlt | FLOAT | Pay Period Paid Amount Target - Alternate |  |  |
| hcaDrvdkpiPaidAmtVarPP | FLOAT | Pay Period Paid Amount Variance |  |  |
| hcaDrvdkpiPaidGrandTotAmtPP | FLOAT | Pay Period Paid Grand Total Amount |  |  |
| hcaDrvdkpiPaidGrandTotFtePP | FLOAT | Pay Period Paid FTEs Total |  |  |
| hcaDrvdkpiPaidGrandTotHrsPP | FLOAT | Pay Period Paid Grand Total Hours |  |  |
| hcaDrvdkpiPaidHrsFtePP | FLOAT | Pay Period Paid FTEs |  |  |
| hcaDrvdkpiPaidHrsTgtPerVolWeightedPPDef | FLOAT | Pay Period Paid Hours Target/Unit Of Service - Default |  |  |
| hcaDrvdkpiPaidHrsTgtPerVolWeightedPPAlt | FLOAT | Pay Period Paid Hours Target/Unit Of Service - Alternate |  |  |
| hcaDrvdkpiPaidHrsTgtPPDef | FLOAT | Pay Period Paid Hours Target - Default |  |  |
| hcaDrvdkpiPaidHrsTgtPPAlt | FLOAT | Pay Period Paid Hours Target - Alternate |  |  |
| hcaDrvdkpiPaidHrsVarPP | FLOAT | Pay Period Paid Hours Variance |  |  |
| hcaDrvdkpiPaidRegFtxotAmtPP | FLOAT | Pay Period Regular Paid Full Time Amount |  |  |
| hcaDrvdkpiPaidRegFtxotFtePP | FLOAT | Pay Period Regular Paid Full Time FTEs |  |  |
| hcaDrvdkpiPaidRegFtxotHrsPP | FLOAT | Pay Period Regular Paid Full Time Hours |  |  |
| hcaDrvdkpiPaidRegPtxotAmtPP | FLOAT | Pay Period Regular Paid Part Time Amount |  |  |
| hcaDrvdkpiPaidRegTotxotAmtPP | FLOAT | Pay Period Regular Paid Total Amount |  |  |
| hcaDrvdkpiPaidRegTotxotFtePP | FLOAT | Pay Period Regular Paid Total FTEs |  |  |
| hcaDrvdkpiPaidRegPtxotFtePP | FLOAT | Pay Period Regular Paid Part Time FTEs |  |  |
| hcaDrvdkpiPaidRegPtxotHrsPP | FLOAT | Pay Period Regular Paid Part Time Hours |  |  |
| hcaDrvdkpiPaidRegTotxotHrsPP | FLOAT | Pay Period Regular Paid Total Hours |  |  |
| hcaDrvdkpiPaidSupAgncyFtePP | FLOAT | Pay Period Supplemental Paid Agency FTEs |  |  |
| hcaDrvdkpiPaidSupExtraptFtePP | FLOAT | Pay Period Supplemental Paid Extra Part Time FTEs |  |  |
| hcaDrvdkpiPaidSupFltinxotAmtPP | FLOAT | Pay Period Supplemental Paid Float In Amount |  |  |
| hcaDrvdkpiPaidFltinxotFtePP | FLOAT | Pay Period Supplemental Paid Float In FTEs |  |  |
| hcaDrvdkpiPaidSupFltinxotHrsPP | FLOAT | Pay Period Supplemental Paid Float In Hours |  |  |
| hcaDrvdkpiPaidSupFltoutFtePP | FLOAT | Pay Period Supplemental Paid Float Out FTEs |  |  |
| hcaDrvdkpiPaidSupIntagncyxotAmtPP | FLOAT | Pay Period Supplemental Paid Internal Agency Amount |  |  |
| hcaDrvdkpiPaidSupIntagncyxotFtePP | FLOAT | Pay Period Supplemental Paid Internal Agency FTEs |  |  |
| hcaDrvdkpiPaidSupIntagncyxotHrsPP | FLOAT | Pay Period Supplemental Paid Internal Agency Hours |  |  |
| hcaDrvdkpiPaidSupOtxagncyAmtPP | FLOAT | Pay Period Supplemental Paid Overtime Amount |  |  |
| hcaDrvdkpiPaidSupOtxagncyFtePP | FLOAT | Pay Period Supplemental Paid Overtime FTEs |  |  |
| hcaDrvdkpiPaidSupOtxagncyHrsPP | FLOAT | Pay Period Supplemental Paid Overtime Hours |  |  |
| hcaDrvdkpiPaidSupPdiemxotAmtPP | FLOAT | Pay Period Supplemental Paid Per Diem Amount |  |  |
| hcaDrvdkpiPaidSupPdiemxotFtePP | FLOAT | Pay Period Supplemental Paid Per Diem FTEs |  |  |
| hcaDrvdkpiPaidSupPdiemxotHrsPP | FLOAT | Pay Period Supplemental Paid Per Diem Hours |  |  |
| hcaDrvdkpiPaidSupPoolxotAmtPP | FLOAT | Pay Period Supplemental Paid Pool Amount |  |  |
| hcaDrvdkpiPaidSupTotHrsPP | FLOAT | Pay Period Supplemental Paid Total Hours |  |  |
| hcaDrvdkpiPaidSupPoolxotFtePP | FLOAT | Pay Period Supplemental Paid Pool FTEs |  |  |
| hcaDrvdkpiPaidSupTotAmtPP | FLOAT | Pay Period Supplemental Paid Total Amount |  |  |
| hcaDrvdkpiPaidSupTotFtePP | FLOAT | Pay Period Supplemental Paid Total FTEs |  |  |
| hcaDrvdkpiPaidSupPoolxotHrsPP | FLOAT | Pay Period Supplemental Paid Pool Hours |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| WU_WorkGroupId | INT64 | The ID of the work group |  |  |
