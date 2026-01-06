# vHcaMetricsDaily

**Group:** Summary Dataset → Healthcare Productivity Summary

- Materialized daily HCA metrics and attributes.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHcaMetricsDaily |
| Unique Identifier | partitionDate,workUnitId |
| Source Pipeline | hcaSummary(DR), hcaMetricsDaily (DR) |

## Columns

**Column count:** 210

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of daily productivity metric - use to join to date dimension |  |  |
| workunitId | INT64 | The ID of the work unit |  |  |
| M_Hcakpi_Prodreg_Hrs | FLOAT | Daily Regular Hours |  |  |
| M_Hcakpi_ProdHrsTgtPerVolWeighted_Pct | FLOAT | Daily Productive Amount Target/Unit Of Service |  |  |
| M_Hcakpi_ProdVar_Hrs | FLOAT | Daily Productive Hour Variance |  |  |
| M_Hcakpi_ProdTgtDef_Hrs | FLOAT | Daily Productive Hours Target - Default |  |  |
| M_Hcakpi_ProdTgtAlt_Hrs | FLOAT | Daily Productive Hours Target - Alternate |  |  |
| M_Hcakpi_ProdHrsPerVolWeighted_Pct | FLOAT | Daily Actual/Unit Of Service |  |  |
| M_Hcakpi_ProdHrsIdx_Pct | FLOAT | Daily Productivity Index |  |  |
| M_Hcakpi_ProdAdjustment_Hrs | FLOAT | Recommended Adjustment |  |  |
| M_Hcakpi_ProdVar_Amt | FLOAT | Daily Productive Amount Variance |  |  |
| M_Hcakpi_ProdTgtDef_Amt | FLOAT | Daily Productive Amount Target - Default |  |  |
| M_Hcakpi_ProdTgtAlt_Amt | FLOAT | Daily Productive Amount Target - Alternate |  |  |
| M_Hcakpi_ProdTgtPerVolWeightedDef_Pct | FLOAT | hcaDrvdkpiProdAmtTgtPerVolWeightedDef |  |  |
| M_Hcakpi_ProdTgtPerVolWeightedAlt_Pct | FLOAT | hcaDrvdkpiProdAmtTgtPerVolWeightedAlt |  |  |
| M_Hcakpi_ProdAmtIdx_Pct | FLOAT | hcaDrvdkpiProdAmtIdx |  |  |
| M_Hcakpi_PaidVar_Hrs | FLOAT | Daily Paid Hours Variance |  |  |
| M_Hcakpi_PaidTgtDef_Hrs | FLOAT | Daily Paid Hours Target - Default |  |  |
| M_Hcakpi_PaidTgtAlt_Hrs | FLOAT | Daily Paid Hours Target - Alternate |  |  |
| M_Hcakpi_PaidHrsTgtPerVolWeightedDef_Pct | FLOAT | Daily Paid Hours Target/Unit Of Service -Default |  |  |
| M_Hcakpi_PaidHrsTgtPerVolWeightedAlt_Pct | FLOAT | Daily Paid Hours Target/Unit Of Service - Alternate |  |  |
| M_Hcakpi_PaidVar_Amt | FLOAT | Daily Paid Amount Variance |  |  |
| M_Hcakpi_PaidFte_Hrs | FLOAT | Daily Paid FTEs |  |  |
| M_Hcakpi_PaidTgtDef_Amt | FLOAT | Daily Paid Amount Target - Default |  |  |
| M_Hcakpi_PaidTgtAlt_Amt | FLOAT | Daily Paid Amount Target - Alternate |  |  |
| M_Hcakpi_PaidAmtTgtPerVolWeightedDef_Pct | FLOAT | Daily Paid Amount Target/Unit Of Service - Default |  |  |
| M_Hcakpi_PaidAmtTgtPerVolWeightedAlt_Pct | FLOAT | Daily Paid Amount Target/Unit Of Service - Alternate |  |  |
| M_Hcakpi_VariableProdHrsPerVolWeightedDaily_Pct | FLOAT | Daily Variable Productive Hours Targets/Unit Of Service |  |  |
| M_Hca_PaidNp_Hrs | FLOAT | Daily Non Productive Hours |  |  |
| M_Hca_PaidNp_Amt | FLOAT | Daily Non Productive Amount |  |  |
| M_Hca_PaidOt_Hrs | FLOAT | Daily Overtime Hours |  |  |
| M_Hca_Paid_Amt | FLOAT | Daily Paid Amount |  |  |
| M_Hca_Paid_Hrs | FLOAT | Daily Paid Hours |  |  |
| M_Hca_PaidFltin_Amt | FLOAT | Daily Paid Float In Amount |  |  |
| M_Hca_PaidFltin_Hrs | FLOAT | Daily Paid Float In Hours |  |  |
| M_Hca_PaidFt_Amt | FLOAT | Daily Paid Full Time Amount |  |  |
| M_Hca_PaidFt_Hrs | FLOAT | Daily Paid Full Time Hours |  |  |
| M_Hca_PaidFltout_Amt | FLOAT | Daily Paid Float Out Amount |  |  |
| M_Hca_PaidFltout_Hrs | FLOAT | Daily Paid Float Out Hours |  |  |
| M_Hca_PaidPdiem_Amt | FLOAT | Daily Paid Per Diem Amount |  |  |
| M_Hca_PaidPdiem_Hrs | FLOAT | Daily Paid Per Diem Hours |  |  |
| M_Hca_PaidPool_Amt | FLOAT | Daily Paid Pool Amount |  |  |
| M_Hca_PaidPool_Hrs | FLOAT | Daily Paid Pool Hours |  |  |
| M_Hca_PaidPt_Amt | FLOAT | Daily Paid Part Time Amount |  |  |
| M_Hca_PaidPt_Hrs | FLOAT | Daily Paid Part Time Hours |  |  |
| M_Hca_ProdAgncy_Hrs | FLOAT | Daily Productive Agency Hours |  |  |
| M_Hca_ProdIntagency_Hrs | FLOAT | Daily Productive Internal Agency Hours |  |  |
| M_Hca_ProdFltin_Amt | FLOAT | Daily Productive Float In Amount |  |  |
| M_Hca_ProdFltin_Hrs | FLOAT | Daily Productive Float In Hours |  |  |
| M_Hca_ProdFltout_Amt | FLOAT | Daily Productive Float Out Amount |  |  |
| M_Hca_ProdFltout_Hrs | FLOAT | Daily Productive Float Out Hours |  |  |
| M_Hca_ProdFt_Amt | FLOAT | Daily Productive Full Time Amount |  |  |
| M_Hca_ProdFt_Hrs | FLOAT | Daily Productive Full Time Hours |  |  |
| M_Hca_Prod_Hrs | FLOAT | Daily Productive Hours |  |  |
| M_Hca_Prod_Amt | FLOAT | Daily Productive Amount |  |  |
| M_Hca_ProdPdiem_Amt | FLOAT | Daily Productive Per Diem Amount |  |  |
| M_Hca_ProdPdiem_Hrs | FLOAT | Daily Productive Per Diem Hours |  |  |
| M_Hca_ProdPool_Amt | FLOAT | Daily Productive Pool Amount |  |  |
| M_Hca_ProdPool_Hrs | FLOAT | Daily Productive Pool Hours |  |  |
| M_Hca_ProdPt_Amt | FLOAT | Daily Productive Part Time Amount |  |  |
| M_Hca_ProdPt_Hrs | FLOAT | Daily Productive Part Time Hours |  |  |
| M_Hca_TgtFixedPaidDef_Amt | FLOAT | Daily Fixed Paid Amount Target - Default |  |  |
| M_Hca_TgtFixedPaidAlt_Amt | FLOAT | Daily Fixed Paid Amount Target - Alternate |  |  |
| M_Hca_TgtFixedProdDef_Amt | FLOAT | Daily Fixed Productive Amount Target - Default |  |  |
| M_Hca_TgtFixedProdAlt_Amt | FLOAT | Daily Fixed Productive Amount Target - Alternate |  |  |
| M_Hca_TgtVariablePaidDef_Amt | FLOAT | Daily Variable Paid Amount Target - Default |  |  |
| M_Hca_TgtVariablePaidAlt_Amt | FLOAT | Daily Variable Paid Amount Target - Alternate |  |  |
| M_Hca_TgtVariablePaidDef_Hrs | FLOAT | Daily Variable Paid Hours Target - Default |  |  |
| M_Hca_TgtVariablePaidAlt_Hrs | FLOAT | Daily Variable Paid Hours Target - Alternate |  |  |
| M_Hca_TgtVariableProdDef_Amt | FLOAT | Daily Variable Productive Amount Target - Default |  |  |
| M_Hca_TgtVariableProdAlt_Amt | FLOAT | Daily Variable Productive Amount Target - Alternate |  |  |
| M_Hca_TgtVariableProdDef_Hrs | FLOAT | Daily Variable Productive Hours Target - Default |  |  |
| M_Hca_TgtVariableProdAlt_Hrs | FLOAT | Daily Variable Productive Hours Target - Alternate |  |  |
| M_Hcavol_VolWeighted_Hrs | FLOAT | Daily Weighted Volume |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| Date_dayOfWkNbr | INT64 | Day of Week |  |  |
| Date_dayOfMoNbr | INT64 | Day of Month |  |  |
| Date_dayOfQtrNbr | INT64 | Day of Quarter |  |  |
| Date_dayOfYrNbr | INT64 | Day of Year |  |  |
| Date_wkOfYrNbr | INT64 | Week of Year |  |  |
| Date_moOfYrNbr | INT64 | Month of Year |  |  |
| Date_qtrOfYrNbr | INT64 | Quarter of Year |  |  |
| Date_yrNbr | INT64 | Year |  |  |
| Date_dayNam | STRING | Day of Week i.e. Sunday, Monday |  |  |
| Date_moNam | STRING | Month Name |  |  |
| Date_qtrNam | STRING | Quarter Name |  |  |
| Date_yrMoNbr | INT64 | Year/Month |  |  |
| Date_lastDayOfWkSwt | BOOLEAN | Boolean indicator where or not this is Last Day of Week |  |  |
| Date_lastDayOfMoSwt | BOOLEAN | Boolean indicator where or not this is Last Day of Month |  |  |
| Date_lastDayOfQtrSwt | BOOLEAN | Boolean indicator where or not this is Last Day of Quarter |  |  |
| Date_lastDayOFYrSwt | BOOLEAN | Boolean indicator where or not this is Last Day of Year |  |  |
| Date_wkEndSwt | BOOLEAN | Boolean indicator where or not this is week end |  |  |
| Date_FsclDayOfWkNbr | INT64 | Fisccal Day of Week |  |  |
| Date_FsclDayOfMoNbr | INT64 | Fiscal Day of Month |  |  |
| Date_FsclDayOfQtrNbr | INT64 | Fiscal Day of Quarter |  |  |
| Date_FsclDayOfYrNbr | INT64 | Fiscal Day of Year |  |  |
| Date_FsclWkOfYrNbr | INT64 | Fiscal Week of Year |  |  |
| Date_FsclMoOfYrNbr | INT64 | Fiscal Month of Year |  |  |
| Date_FsclQtrOfYrNbr | INT64 | Fiscal Quarter of Year |  |  |
| Date_FsclYrNbr | INT64 | Fiscal Year Number |  |  |
| Date_FsclMoNam | STRING | Fiscal Month Name |  |  |
| Date_FsclQtrNam | STRING | Fiscal Quarter Name |  |  |
| Date_FsclYrMoNbr | STRING | Fiscal Year/Month |  |  |
| Date_FsclLastDayOfWkSwt | BOOLEAN | Boolean indicator where or not this is Fiscal Last Day of Week |  |  |
| Date_FsclLastDayOfMoSwt | BOOLEAN | Boolean indicator where or not this is Fiscal Last Day of Month |  |  |
| Date_FsclLastDayOfQtrSwt | BOOLEAN | Boolean indicator where or not this is Fiscal Last Day of Quarter |  |  |
| Date_FsclLastDayOfYrSwt | BOOLEAN | Boolean indicator where or not this is Fiscal Last Day of Year |  |  |
| stp_Today | BOOLEAN | Boolean indicator where or not this is Today |  |  |
| stp_Yesterday | BOOLEAN | Boolean indicator where or not this is Yesterday |  |  |
| stp_Last30Days | BOOLEAN | Boolean indicator where or not this is Last 30 Days |  |  |
| stp_Last13Weeks | BOOLEAN | Boolean indicator where or not this is Last 13 weeks |  |  |
| stp_LastMonth | BOOLEAN | Boolean indicator where or not this is Last Month |  |  |
| stp_LastQuarter | BOOLEAN | Boolean indicator where or not this is Last Quarter |  |  |
| stp_CurrentQuarter | BOOLEAN | Boolean indicator where or not this is Current Quarter |  |  |
| stp_CurrentMonth | BOOLEAN | Boolean indicator where or not this is Current Month |  |  |
| stp_NextQuarter | BOOLEAN | Boolean indicator where or not this is Next Quarter |  |  |
| stp_NextMonth | BOOLEAN | Boolean indicator where or not this is Next Month |  |  |
| stp_CurrentYear | BOOLEAN | Boolean indicator where or not this is Current Year |  |  |
| stp_LastYear | BOOLEAN | Boolean indicator where or not this is Last Year |  |  |
| stp_YTD | BOOLEAN | Boolean indicator where or not this is Year to Date |  |  |
| stp_QTD | BOOLEAN | Boolean indicator where or not this is Quarter to Date |  |  |
| stp_MTD | BOOLEAN | Boolean indicator where or not this is Month to Date |  |  |
| stp_WTD | BOOLEAN | Boolean indicator where or not this is Week to Date |  |  |
| stp_CurrentWeek | BOOLEAN | Boolean indicator where or not this is Current Week |  |  |
| stp_NextWeek | BOOLEAN | Boolean indicator where or not this is Next Week |  |  |
| stp_LastWeek | BOOLEAN | Boolean indicator where or not this is Last Week |  |  |
| stp_Last6MTD | BOOLEAN | Boolean indicator where or not this is Last 6 Months to Date |  |  |
| stp_TwoWeeksOut | BOOLEAN | Boolean indicator where or not this is 2 weeks out |  |  |
| stp_Last8Weeks | BOOLEAN | Boolean indicator where or not this is Last 8 Weeks |  |  |
| stp_MonthBeforeLast | BOOLEAN | Boolean indicator where or not this is Month before Last |  |  |
| stp_ThreeWeeksOut | BOOLEAN | Boolean indicator where or not this is 3 weeks out |  |  |
| stp_FsclLast13Weeks | BOOLEAN | Boolean indicator where or not this is Fiscal Last 13 weeks |  |  |
| stp_FsclLastMonth | BOOLEAN | Boolean indicator where or not this is Fiscal Last Month |  |  |
| stp_FsclLastQuarter | BOOLEAN | Boolean indicator where or not this is Fiscal Last Quarter |  |  |
| stp_FsclCurrentQuarter | BOOLEAN | Boolean indicator where or not this is Fiscal Current Quarter |  |  |
| stp_FsclCurrentMonth | BOOLEAN | Boolean indicator where or not this is Fiscal Curent Month |  |  |
| stp_FsclNextQuarter | BOOLEAN | Boolean indicator where or not this is Fiscal Next Quarter |  |  |
| stp_FsclNextMonth | BOOLEAN | Boolean indicator where or not this is Fiscal Next Month |  |  |
| stp_FsclCurrentYear | BOOLEAN | Boolean indicator where or not this is Fiscal Current Year |  |  |
| stp_FsclLastYear | BOOLEAN | Boolean indicator where or not this is Fiscal Last Year |  |  |
| stp_FsclYTD | BOOLEAN | Boolean indicator where or not this is Fiscal Year to Date |  |  |
| stp_FsclQTD | BOOLEAN | Boolean indicator where or not this is Fiscal Quarter to Date |  |  |
| stp_FsclMTD | BOOLEAN | Boolean indicator where or not this is Fiscal Month to Date |  |  |
| stp_FsclWTD | BOOLEAN | Boolean indicator where or not this is Fiscal Week to Date |  |  |
| stp_FsclCurrentWeek | BOOLEAN | Boolean indicator where or not this is Fiscal Current Week |  |  |
| stp_FsclNextWeek | BOOLEAN | Boolean indicator where or not this is Fiscal Next Week |  |  |
| stp_FsclLastWeek | BOOLEAN | Boolean indicator where or not this is Fiscal Last Week |  |  |
| stp_FsclLast6MTD | BOOLEAN | Boolean indicator where or not this is Fiscal Last 6 Month to Date |  |  |
| stp_FsclTwoWeeksOut | BOOLEAN | Boolean indicator where or not this is Fiscal Year 2 Weeks Out |  |  |
| stp_FsclLast8Weeks | BOOLEAN | Boolean indicator where or not this is Fiscal Last 8 weeks |  |  |
| stp_FsclMonthBeforeLast | BOOLEAN | Boolean indicator where or not this is Fiscal Month before Last |  |  |
| stp_FsclThreeWeeksOut | BOOLEAN | Boolean indicator where or not this is Fiscal Year 3 Weeks Out |  |  |
| PP_startDate | DATE | Pay Period Start Date |  |  |
| PP_endDate | DATE | Payperiod End Date |  |  |
| PP_payPeriod | STRING | Pay Period |  |  |
| PP_payPeriodOffset | INT64 | Pay Period Offset |  |  |
| WU_WorkUnitCode | STRING | Work Unit Code |  |  |
| WU_WorkUnitName | STRING | Work Unit Name |  |  |
| WU_CaregiverSwt | INT64 | Work Unit Caregiver Switch |  |  |
| WU_WorkWeekFTEHours | FLOAT | FTE Hours in Work Week |  |  |
| WU_ServiceLine | STRING | Work Unit Service Line |  |  |
| WU_UnitOfService | STRING | Work Unit Unit of Service |  |  |
| WU_PayRuleId | INT64 | The ID of a pay rule join with vPayRules |  |  |
| WU_PayRuleName | STRING | Pay Rule Name |  |  |
| WU_WorkUnitTypeId | INT64 | The ID of the work unit type |  |  |
| WU_WorkUnitTypeName | STRING | Work Unit Type Name |  |  |
| WU_WorkGroupId | INT64 | The ID of the work group |  |  |
| WU_WorkGroupName | STRING | Work Group Name |  |  |
| WU_WorkGroupCode | STRING | Work Group Code |  |  |
| procedureID | INT64 | The ID of the procedure |  |  |
| Hcavol_VolmetricPost_Date | DATE | Post Date |  |  |
| M_Hcavol_VolmetricRawVolume_Hrs | FLOAT | Raw volume provided by customer volume import integrations |  |  |
| M_Hcavol_VolmetricAllocatedVolume_Hrs | FLOAT | Weighted volume based on raw volume and weighting |  |  |
| Hcavol_CoreProcedureCode | STRING | Procedure Code |  |  |
| Hcavol_CoreProcedureDesc | STRING | Procedure Description |  |  |
| Hcavol_CorePatientType | STRING | Patient Type |  |  |
| BusWU_OrgId | INT64 |  |  |  |
| BusWU_OrgName | STRING |  |  |  |
| BusWU_OrgFullName | STRING |  |  |  |
| BusWU_OrgDescription | STRING |  |  |  |
| BusWU_OrgBreak0 | STRING |  |  |  |
| BusWU_OrgBreak1 | STRING |  |  |  |
| BusWU_OrgBreak2 | STRING |  |  |  |
| BusWU_OrgBreak3 | STRING |  |  |  |
| BusWU_OrgBreak4 | STRING |  |  |  |
| BusWU_OrgBreak5 | STRING |  |  |  |
| BusWU_OrgBreak6 | STRING |  |  |  |
| BusWU_OrgBreak7 | STRING |  |  |  |
| BusWU_OrgBreak8 | STRING |  |  |  |
| BusWU_OrgBreak9 | STRING |  |  |  |
| BusWU_OrgBreak10 | STRING |  |  |  |
| BusWU_OrgBreak11 | STRING |  |  |  |
| BusWU_OrgBreak12 | STRING |  |  |  |
| BusWU_OrgBreak13 | STRING |  |  |  |
| BusWU_OrgBreak14 | STRING |  |  |  |
| BusWU_OrgBreak15 | STRING |  |  |  |
| BusWU_OrgBreak16 | STRING |  |  |  |
| BusWU_OrgBreak17 | STRING |  |  |  |
| BusWU_OrgBreak18 | STRING |  |  |  |
| BusWU_OrgBreak19 | STRING |  |  |  |
| BusWU_OrgBreak20 | STRING |  |  |  |
| WU_OrgID_2 | INT64 |  |  |  |
| WU_OrgID_3 | INT64 |  |  |  |
| WU_OrgID_4 | INT64 |  |  |  |
| WU_OrgID_5 | INT64 |  |  |  |
| WU_OrgID_6 | INT64 |  |  |  |
| WU_OrgID_7 | INT64 |  |  |  |
| WU_OrgID_8 | INT64 |  |  |  |
| WU_OrgID_9 | INT64 |  |  |  |
| WU_OrgID_10 | INT64 |  |  |  |
