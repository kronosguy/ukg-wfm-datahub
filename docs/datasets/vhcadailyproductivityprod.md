# vHcaDailyProductivityProd

**Group:** Detail Dataset → Healthcare Productivity

Daily Productivity Productive provides work unit productive productivity data based on daily timekeeping totals, regular and supplemental labor details, and fixed and variable targets compared to actual hours and amounts. Historical Reload Constraint: The historical reload capability of this pipeline is limited by the pay periods defined in vHcaWorkUnitPayPeriod. Specifically, data can be reloaded for a range spanning 26 pay periods in the past up to 5 pay periods in the future relative to the current pay period.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHcaDailyProductivityProd |
| Unique Identifier | partitionDate,workunitId |
| Source Pipeline | hcaDailyProductivityProd (CDC) |

## Columns

**Column count:** 41

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of daily productivity metric - use to join to date dimension |  |  |
| dailyDate | DATE | Represents apply date of daily productivity metric |  |  |
| workunitId | INT64 | The ID of the work unit |  |  |
| hcaDrvdkpiProdRegHrs | FLOAT | Daily Regular Hours |  |  |
| hcaDrvdkpiProdHrsTgtPerVolWeighted | FLOAT | Daily Productive Amount Target/Unit Of Service |  |  |
| hcaDrvdkpiProdHrsVar | FLOAT | Daily Productive Hour Variance |  |  |
| hcaDrvdkpiProdHrsTgtDef | FLOAT | Daily Productive Hours Target - Default |  |  |
| hcaDrvdkpiProdHrsTgtAlt | FLOAT | Daily Productive Hours Target - Alternate |  |  |
| hcaDrvdkpiProdHrsPerVolWeighted | FLOAT | Daily Actual/Unit Of Service |  |  |
| hcaDrvdkpiProdHrsIdx | FLOAT | Daily Productivity Index |  |  |
| hcaDrvdkpiProdHrsAdjustment | FLOAT | Recommended Adjustment |  |  |
| hcaDrvdkpiProdAmtVar | FLOAT | Daily Productive Amount Variance |  |  |
| hcaDrvdkpiProdAmtTgtDef | FLOAT | Daily Productive Amount Target - Default |  |  |
| hcaDrvdkpiProdAmtTgtAlt | FLOAT | Daily Productive Amount Target - Alternate |  |  |
| hcaDrvdkpiProdAmtTgtPerVolWeightedDef | FLOAT | Daily Productive Amount Target/Unit Of Service - Default |  |  |
| hcaDrvdkpiProdAmtTgtPerVolWeightedAlt | FLOAT | Daily Productive Amount Target/Unit Of Service - Alternate |  |  |
| hcaDrvdkpiProdAmtIdx | FLOAT | Daily Productivity Amount Index |  |  |
| hcaDrvdkpiHcavariableMetricProdHrsPerVolWeightedDaily | FLOAT | Daily Variable Productive Hours Targets/Unit Of Service |  |  |
| hcaTgtHcafixedMetricProdAmtDef | FLOAT | Daily Fixed Productive Amount Target - Default |  |  |
| hcaTgtHcafixedMetricProdAmtAlt | FLOAT | Daily Fixed Productive Amount Target - Alternate |  |  |
| hcaTgtHcavariableMetricProdAmtDef | FLOAT | Daily Variable Productive Amount Target - Default |  |  |
| hcaTgtHcavariableMetricProdAmtAlt | FLOAT | Daily Variable Productive Amount Target - Alternate |  |  |
| hcaTgtHcavariableMetricProdHrsDef | FLOAT | Daily Variable Productive Hours Target - Default |  |  |
| hcaTgtHcavariableMetricProdHrsAlt | FLOAT | Daily Variable Productive Hours Target - Alternate |  |  |
| hcaMetricProdAgncyHrs | FLOAT | Daily Productive Agency Hours |  |  |
| hcaMetricProdIntagencyHrs | FLOAT | Daily Productive Internal Agency Hours |  |  |
| hcaMetricProdFltinAmt | FLOAT | Daily Productive Float In Amount |  |  |
| hcaMetricProdFltinHrs | FLOAT | Daily Productive Float In Hours |  |  |
| hcaMetricProdFltoutAmt | FLOAT | Daily Productive Float Out Amount |  |  |
| hcaMetricProdFltoutHrs | FLOAT | Daily Productive Float Out Hours |  |  |
| hcaMetricProdFtAmt | FLOAT | Daily Productive Full Time Amount |  |  |
| hcaMetricProdFtHrs | FLOAT | Daily Productive Full Time Hours |  |  |
| hcaMetricProdHrs | FLOAT | Daily Productive Hours |  |  |
| hcaMetricProdAmt | FLOAT | Daily Productive Amount |  |  |
| hcaMetricProdPdiemAmt | FLOAT | Daily Productive Per Diem Amount |  |  |
| hcaMetricProdPdiemHrs | FLOAT | Daily Productive Per Diem Hours |  |  |
| hcaMetricProdPoolAmt | FLOAT | Daily Productive Pool Amount |  |  |
| hcaMetricProdPoolHrs | FLOAT | Daily Productive Pool Hours |  |  |
| hcaMetricProdPtAmt | FLOAT | Daily Productive Part Time Amount |  |  |
| hcaMetricProdPtHrs | FLOAT | Daily Productive Part Time Hours |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
