# vHcaDailyProductivityPaid

**Group:** Detail Dataset → Healthcare Productivity

Daily Productivity Paid provides work unit paid productivity data based on daily timekeeping totals, regular and supplemental labor details, and fixed and variable targets compared to actual hours and amounts. Historical Reload Constraint: The historical reload capability of this pipeline is limited by the pay periods defined in vHcaWorkUnitPayPeriod. Specifically, data can be reloaded for a range spanning 26 pay periods in the past up to 5 pay periods in the future relative to the current pay period.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHcaDailyProductivityPaid |
| Unique Identifier | partitionDate,workunitId |
| Source Pipeline | hcaDailyProductivityPaid |

## Columns

**Column count:** 39

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of daily productivity metric - use to join to date dimension |  |  |
| dailyDate | DATE | Represents apply date of daily productivity metric |  |  |
| workunitId | INT64 | The ID of the work unit |  |  |
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
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
