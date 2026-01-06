# vHcaDailyProductivity

**Group:** Detail Dataset → Healthcare Productivity

Daily Productivity Paid and Productive provides work unit paid productivity data based on daily timekeeping totals, regular and supplemental labor details, and fixed and variable targets compared to actual hours and amounts. (This is a combination of views vHcaDailyProductivityPaid + vHcaDailyProductivityProd)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHcaDailyProductivity |
| Unique Identifier | partitionDate,workunitId |
| Source Pipeline |  |

## Columns

**Column count:** 76

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of daily productivity metric - use to join to date dimension |  |  |
| dailyDate | DATE | Represents apply date of daily productivity metric |  |  |
| workunitID | INT64 | The ID of the work unit |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
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
| hcaMetricPaidAmt | FLOAT | Daily Paid Amount |  |  |
| hcaMetricPaidHrs | FLOAT | Daily Paid Hours |  |  |
| hcaMetricPaidFltinAmt | FLOAT | Daily Paid Float In Amount |  |  |
| hcaMetricPaidFltinHrs | FLOAT | Daily Paid Float In Hours |  |  |
| hcaMetricPaidFtAmt | FLOAT | Daily Paid Full Time Amount |  |  |
| hcaMetricPaidFtHrs | FLOAT | Daily Paid Full Time Hours |  |  |
| hcaMetricPaidFltoutAmt | FLOAT | Daily Paid Float Out Amount |  |  |
| hcaMetricPaidFltoutHrs | FLOAT | Daily Paid Float Out Hours |  |  |
| hcaMetricPaidPdiemAmt | FLOAT | Daily Paid Per Diem Amount |  |  |
| hcaMetricPaidPdiemHrs | FLOAT | Daily Paid Per Diem Hours |  |  |
| hcaMetricPaidPoolAmt | FLOAT | Daily Paid Pool Amount |  |  |
| hcaMetricPaidPoolHrs | FLOAT | Daily Paid Pool Hours |  |  |
| hcaMetricPaidPtAmt | FLOAT | Daily Paid Part Time Amount |  |  |
| hcaMetricPaidPtHrs | FLOAT | Daily Paid Part Time Hours |  |  |
| hcaTgtHcavariableMetricPaidAmtDef | FLOAT | Daily Variable Paid Amount Target - Default |  |  |
| hcaTgtHcavariableMetricPaidAmtAlt | FLOAT | Daily Variable Paid Amount Target - Alternate |  |  |
| hcaTgtHcavariableMetricPaidHrsDef | FLOAT | Daily Variable Paid Hours Target - Default |  |  |
| hcaTgtHcavariableMetricPaidHrsAlt | FLOAT | Daily Variable Paid Hours Target - Alternate |  |  |
| hcaTgtHcafixedMetricPaidAmtDef | FLOAT | Daily Fixed Paid Amount Target - Default |  |  |
| hcaTgtHcafixedMetricPaidAmtAlt | FLOAT | Daily Fixed Paid Amount Target - Alternate |  |  |
| hcaDrvdkpiPaidHrsVar | FLOAT | Daily Paid Hours Variance |  |  |
| hcaDrvdkpiPaidHrsTgtDef | FLOAT | Daily Paid Hours Target - Default |  |  |
| hcaDrvdkpiPaidHrsTgtAlt | FLOAT | Daily Paid Hours Target - Alternate |  |  |
| hcaDrvdkpiPaidHrsTgtPerVolWeightedDef | FLOAT | Daily Paid Hours Target/Unit Of Service -Default |  |  |
| hcaDrvdkpiPaidHrsTgtPerVolWeightedAlt | FLOAT | Daily Paid Hours Target/Unit Of Service - Alternate |  |  |
| hcaDrvdkpiPaidAmtVar | FLOAT | Daily Paid Amount Variance |  |  |
| hcaDrvdkpiPaidHrsFte | FLOAT | Daily Paid FTEs |  |  |
| hcaDrvdkpiPaidAmtTgtDef | FLOAT | Daily Paid Amount Target - Default |  |  |
| hcaDrvdkpiPaidAmtTgtAlt | FLOAT | Daily Paid Amount Target - Alternate |  |  |
| hcaDrvdkpiPaidAmtTgtPerVolWeightedDef | FLOAT | Daily Paid Amount Target/Unit Of Service - Default |  |  |
| hcaDrvdkpiPaidAmtTgtPerVolWeightedAlt | FLOAT | Daily Paid Amount Target/Unit Of Service - Alternate |  |  |
| hcaMetricPaidNpHrs | FLOAT | Daily Non Productive Hours |  |  |
| hcaMetricPaidNpAmt | FLOAT | Daily Non Productive Amount |  |  |
| hcaMetricPaidOtHrs | FLOAT | Daily Overtime Hours |  |  |
| hcaMetricVolWeighted | FLOAT | Daily Weighted Volume |  |  |
