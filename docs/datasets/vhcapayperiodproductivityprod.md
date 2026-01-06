# vHcaPayperiodProductivityProd

**Group:** Detail Dataset → Healthcare Productivity

Pay Period Productivity Productive provides pay period work unit productivity, regular and supplemental labor details, and fixed and variable targets compared to actual hours and amounts. Historical Reload Constraint: The historical reload capability of this pipeline is limited by the pay periods defined in vHcaWorkUnitPayPeriod. Specifically, data can be reloaded for a range spanning 26 pay periods in the past up to 5 pay periods in the future relative to the current pay period.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHcaPayperiodProductivityProd |
| Unique Identifier | partitionDate,workunitId |
| Source Pipeline | hcaPayperiodProductivityProd (CDC) |

## Columns

**Column count:** 31

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of the payroll detail - use to join to date dimension |  |  |
| startDate | DATE | Start Date of the pay period |  |  |
| endDate | DATE | End date of the pay period |  |  |
| workunitId | INT64 | The ID of the work unit |  |  |
| hcaDrvdkpiProdAmtIdxPP | FLOAT | Pay Period Productivity Amount Index |  |  |
| hcaDrvdkpiProdAmtTgtPerVolWeightedPPdef | FLOAT | Pay Period Productive Amount Target/Unit Of Service |  |  |
| hcaDrvdkpiProdAmtTgtPerVolWeightedPPalt | FLOAT | Pay Period Productive Amount Target/Unit Of Service |  |  |
| hcaDrvdkpiProdAmtTgtPPdef | FLOAT | Pay Period Productive Amount Target - Default |  |  |
| hcaDrvdkpiProdAmtTgtPPalt | FLOAT | Pay Period Productive Amount Target - Alternate |  |  |
| hcaDrvdkpiProdAmtVarPP | FLOAT | Pay Period Productive Amount Variance |  |  |
| hcaDrvdkpiProdHrsFtePP | FLOAT | Pay Period Productive Hours FTEs |  |  |
| hcaDrvdkpiProdHrsIdxPP | FLOAT | Pay Period Productivity Index |  |  |
| hcaDrvdkpiProdHrsPerVolWeightedPP | FLOAT | Pay Period Productive Hours/Unit Of Service |  |  |
| hcaDrvdkpiProdHrsTgtPerVolWeightedPPdef | FLOAT | Pay Period Productive Hours Target/Unit Of Service |  |  |
| hcaDrvdkpiProdHrsTgtPerVolWeightedPPalt | FLOAT | Pay Period Productive Hours Target/Unit Of Service |  |  |
| hcaDrvdkpiProdHrsTgtPPdef | FLOAT | Pay Period Productive Hours Target - Default |  |  |
| hcaDrvdkpiProdHrsTgtPPalt | FLOAT | Pay Period Productive Hours Target - Alternate |  |  |
| hcaDrvdkpiProdHrsVarCostPP | FLOAT | Estimated Cost |  |  |
| hcaDrvdkpiProdHrsVarPP | FLOAT | Pay Period Productive Hours Variance |  |  |
| hcaDrvdkpiProdAmtPerVolWeighted | FLOAT | Pay Period Productive Cost/Unit Of Service |  |  |
| hcaDrvdkpiProdHRSVarPerVolWeighted | FLOAT | Pay Period Productive Hours Variance/Unit Of Service |  |  |
| hcaTgtHcafixedMetricProdAmtPP | FLOAT | Pay Period Fixed Prod Amount Target - Alternate |  |  |
| hcaTgtHcafixedMetricProdHrsPPdef | FLOAT | Pay Period Fixed Prod Hours Target - Default |  |  |
| hcaTgtHcafixedMetricProdHrsPPalt | FLOAT | Pay Period Fixed Prod Hours Target - Alternate |  |  |
| hcaTgtHcaVariableMetricProdAmtPPdef | FLOAT | Pay Period Variable Prod Amount Target - Default |  |  |
| hcaTgtHcaVariableMetricProdAmtPPalt | FLOAT | Pay Period Variable Prod Amount Target - Default |  |  |
| hcaTgtHcaVariableMetricProdHrsPPdef | FLOAT | Pay Period Variable Prod Hours Target - Default |  |  |
| hcaTgtHcaVariableMetricProdHrsPPalt | FLOAT | Pay Period Variable Prod Hours Target - Alternate |  |  |
| hcaDrvdkpiHcavariableMetricProdHrsPerVolWrightedPP | FLOAT | Pay Period Variable Productive Hours Targets/Unit Of Service |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| WU_WorkGroupId | INT64 | The ID of the work group |  |  |
