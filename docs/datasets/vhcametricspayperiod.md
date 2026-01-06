# vHcaMetricsPayPeriod

**Group:** Summary Dataset → Healthcare Productivity Summary

- Materialized pay period HCA metrics and attributes.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHcaMetricsPayPeriod |
| Unique Identifier | partitionDate,workUnitId |
| Source Pipeline | hcaSummary(DR), hcaMetricsPayPeriod (DR) |

## Columns

**Column count:** 550

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of the payroll detail - use to join to date dimension |  |  |
| workunitId | INT64 | The ID of the work unit |  |  |
| startDate | DATE | Start Date of the pay period |  |  |
| endDate | DATE | End date of the pay period |  |  |
| personId | INT64 | The ID of the person referencing the People view |  |  |
| orgjobId | INT64 | The ID of the org job referencing the businessStructure view |  |  |
| workgroupId | INT64 | The ID of the work group |  |  |
| M_Hca_TgtFixedPaidDef_Amt | FLOAT | Pay Period Fixed Paid Amount Target - Default |  |  |
| M_Hca_TgtFixedPaidAlt_Amt | FLOAT | Pay Period Fixed Paid Amount Target - Alternate |  |  |
| M_Hca_TgtFixedPaidDef_Hrs | FLOAT | Pay Period Fixed Paid Hours Target - Default |  |  |
| M_Hca_TgtFixedPaid_Hrs | FLOAT | Pay Period Fixed Paid Hours Target - Alternate |  |  |
| M_Hca_TgtFixedProd_Amt | FLOAT | Pay Period Fixed Prod Amount Target - Alternate |  |  |
| M_Hca_TgtFixedProdDef_Hrs | FLOAT | Pay Period Fixed Prod Hours Target - Default |  |  |
| M_Hca_TgtFixedProdAlt_Hrs | FLOAT | Pay Period Fixed Prod Hours Target - Alternate |  |  |
| M_Hca_TgtVariablePaidDef_Amt | FLOAT | Pay Period Variable Paid Amount Target - Default |  |  |
| M_Hca_TgtVariablePaidAlt_Amt | FLOAT | Pay Period Variable Paid Amount Target - Alternate |  |  |
| M_Hca_TgtVariablePaidDef_Hrs | FLOAT | Pay Period Variable Paid Hours Target - Default |  |  |
| M_Hca_TgtVariablePaidAlt_Hrs | FLOAT | Pay Period Variable Paid Hours Target - Alternate |  |  |
| M_Hca_TgtVariableProdDef_Amt | FLOAT | Pay Period Variable Prod Amount Target - Default |  |  |
| M_Hca_TgtVariableProdAlt_Amt | FLOAT | Pay Period Variable Prod Amount Target - Default |  |  |
| M_Hca_TgtVariableProdDef_Hrs | FLOAT | Pay Period Variable Prod Hours Target - Default |  |  |
| M_Hca_TgtVariableProdAlt_Hrs | FLOAT | Pay Period Variable Prod Hours Target - Alternate |  |  |
| M_Hcakpi_VariableProdHrsPerVolWeighted_Pct | FLOAT | Pay Period Variable Productive Hours Targets/Unit Of Service |  |  |
| M_Hcakpi_PaidAmtTgtPerVolWeightedDef_Pct | FLOAT | Pay Period Paid Amount Target/Unit Of Service - Default |  |  |
| M_Hcakpi_PaidAmtTgtPerVolWeightedAlt_Pct | FLOAT | Pay Period Paid Amount Target/Unit Of Service - Alternate |  |  |
| M_Hcakpi_PaidTgtDef_Amt | FLOAT | Pay Period Paid Amount Target - Default |  |  |
| M_Hcakpi_PaidTgtAlt_Amt | FLOAT | Pay Period Paid Amount Target - Alternate |  |  |
| M_Hcakpi_PaidVar_Amt | FLOAT | Pay Period Paid Amount Variance |  |  |
| M_Hcakpi_PaidGrandTot_Amt | FLOAT | Pay Period Paid Grand Total Amount |  |  |
| M_Hcakpi_PaidGrandTotFte_Amt | FLOAT | Pay Period Paid FTEs Total |  |  |
| M_Hcakpi_PaidGrandTot_Hrs | FLOAT | Pay Period Paid Grand Total Hours |  |  |
| M_Hcakpi_PaidFte_Hrs | FLOAT | Pay Period Paid FTEs |  |  |
| M_Hcakpi_PaidHrsTgtPerVolWeightedDef_Pct | FLOAT | Pay Period Paid Hours Target/Unit Of Service - Default |  |  |
| M_Hcakpi_PaidHrsTgtPerVolWeightedAlt_Pct | FLOAT | Pay Period Paid Hours Target/Unit Of Service - Alternate |  |  |
| M_Hcakpi_PaidTgtDef_Hrs | FLOAT | Pay Period Paid Hours Target - Default |  |  |
| M_Hcakpi_PaidTgtAlt_Hrs | FLOAT | Pay Period Paid Hours Target - Alternate |  |  |
| M_Hcakpi_PaidVar_Hrs | FLOAT | Pay Period Paid Hours Variance |  |  |
| M_Hcakpi_PaidRegFtxot_Amt | FLOAT | Pay Period Regular Paid Full Time Amount |  |  |
| M_Hcakpi_PaidRegFtxotFte_Amt | FLOAT | Pay Period Regular Paid Full Time FTEs |  |  |
| M_Hcakpi_PaidRegFtxot_Hrs | FLOAT | Pay Period Regular Paid Full Time Hours |  |  |
| M_Hcakpi_PaidRegPtxot_Amt | FLOAT | Pay Period Regular Paid Part Time Amount |  |  |
| M_Hcakpi_PaidRegTotxot_Amt | FLOAT | Pay Period Regular Paid Total Amount |  |  |
| M_Hcakpi_PaidRegTotxotFte_Amt | FLOAT | Pay Period Regular Paid Total FTEs |  |  |
| M_Hcakpi_PaidRegPtxotFte_Amt | FLOAT | Pay Period Regular Paid Part Time FTEs |  |  |
| M_Hcakpi_PaidRegPtxot_Hrs | FLOAT | Pay Period Regular Paid Part Time Hours |  |  |
| M_Hcakpi_PaidRegTotxot_Hrs | FLOAT | Pay Period Regular Paid Total Hours |  |  |
| M_Hcakpi_PaidSupAgncyFte_Amt | FLOAT | Pay Period Supplemental Paid Agency FTEs |  |  |
| M_Hcakpi_PaidSupExtraptFte_Amt | FLOAT | Pay Period Supplemental Paid Extra Part Time FTEs |  |  |
| M_Hcakpi_PaidSupFltinxot_Amt | FLOAT | Pay Period Supplemental Paid Float In Amount |  |  |
| M_Hcakpi_PaidFltinxotFte_Amt | FLOAT | Pay Period Supplemental Paid Float In FTEs |  |  |
| M_Hcakpi_PaidSupFltinxot_Hrs | FLOAT | Pay Period Supplemental Paid Float In Hours |  |  |
| M_Hcakpi_PaidSupFltoutFte_Amt | FLOAT | Pay Period Supplemental Paid Float Out FTEs |  |  |
| M_Hcakpi_PaidSupIntagncyxot_Amt | FLOAT | Pay Period Supplemental Paid Internal Agency Amount |  |  |
| M_Hcakpi_PaidSupIntagncyxotFte_Amt | FLOAT | Pay Period Supplemental Paid Internal Agency FTEs |  |  |
| M_Hcakpi_PaidSupIntagncyxotFte_Hrs | FLOAT | Pay Period Supplemental Paid Internal Agency Hours |  |  |
| M_Hcakpi_PaidSupOtxagncy_Amt | FLOAT | Pay Period Supplemental Paid Overtime Amount |  |  |
| M_Hcakpi_PaidSupOtxagncyFte_Amt | FLOAT | Pay Period Supplemental Paid Overtime FTEs |  |  |
| M_Hcakpi_PaidSupOtxagncy_Hrs | FLOAT | Pay Period Supplemental Paid Overtime Hours |  |  |
| M_Hcakpi_PaidSupPdiemxot_Amt | FLOAT | Pay Period Supplemental Paid Per Diem Amount |  |  |
| M_Hcakpi_PaidSupPdiemxotFte_Amt | FLOAT | Pay Period Supplemental Paid Per Diem FTEs |  |  |
| M_Hcakpi_PaidSupPdiemxot_Hrs | FLOAT | Pay Period Supplemental Paid Per Diem Hours |  |  |
| M_Hcakpi_PaidSupPoolxot_Amt | FLOAT | Pay Period Supplemental Paid Pool Amount |  |  |
| M_Hcakpi_PaidSupTot_Hrs | FLOAT | Pay Period Supplemental Paid Total Hours |  |  |
| M_Hcakpi_ProdAmtIdx_Pct | FLOAT | Pay Period Productivity Amount Index |  |  |
| M_Hcakpi_ProdAmtTgtPerVolWeightedDef_Pct | FLOAT | Pay Period Productive Amount Target/Unit Of Service |  |  |
| M_Hcakpi_ProdAmtTgtPerVolWeightedAlt_Pct | FLOAT | Pay Period Productive Amount Target/Unit Of Service |  |  |
| M_Hcakpi_ProdTgtDef_Amt | FLOAT | Pay Period Productive Amount Target - Default |  |  |
| M_Hcakpi_ProdTgtAlt_Amt | FLOAT | Pay Period Productive Amount Target - Alternate |  |  |
| M_Hcakpi_ProdVar_Amt | FLOAT | Pay Period Productive Amount Variance |  |  |
| M_Hcakpi_PaidSupPoolxotFte_Amt | FLOAT | Pay Period Supplemental Paid Pool FTEs |  |  |
| M_Hcakpi_PaidSupTot_Amt | FLOAT | Pay Period Supplemental Paid Total Amount |  |  |
| M_Hcakpi_PaidSupTotFte_Amt | FLOAT | Pay Period Supplemental Paid Total FTEs |  |  |
| M_Hcakpi_PaidSupPoolxot_Hrs | FLOAT | Pay Period Supplemental Paid Pool Hours |  |  |
| M_Hcakpi_ProdHrsFte_Amt | FLOAT | Pay Period Productive Hours FTEs |  |  |
| M_Hcakpi_ProdHrsIdx_Pct | FLOAT | Pay Period Productivity Index |  |  |
| M_Hcakpi_ProdHrsPerVolWeighted_Pct | FLOAT | Pay Period Productive Hours/Unit Of Service |  |  |
| M_Hcakpi_ProdHrsTgtPerVolWeightedDef_Pct | FLOAT | Pay Period Productive Hours Target/Unit Of Service |  |  |
| M_Hcakpi_ProdHrsTgtPerVolWeightedAlt_Pct | FLOAT | Pay Period Productive Hours Target/Unit Of Service |  |  |
| M_Hcakpi_ProdTgtDef_Hrs | FLOAT | Pay Period Productive Hours Target - Default |  |  |
| M_Hcakpi_ProdTgtAlt_Hrs | FLOAT | Pay Period Productive Hours Target - Alternate |  |  |
| M_Hcakpi_ProdVarCost_Hrs | FLOAT | Estimated Cost |  |  |
| M_Hcakpi_ProdVar_Hrs | FLOAT | Pay Period Productive Hours Variance |  |  |
| M_Hcakpi_ProdAmtPerVolWeighted_Pct | FLOAT | Pay Period Productive Cost/Unit Of Service |  |  |
| M_Hcakpi_ProdHrsVarPerVolWeightedDef_Pct | FLOAT | Pay Period Productive Hours Variance/Unit Of Service |  |  |
| Hca_RawPayrollJob | STRING | Payroll Paid Job |  |  |
| M_Hca_RawPayrollPaid_Hrs | FLOAT | Payroll Hours |  |  |
| M_Hca_RawPayrollPaid_Amt | FLOAT | Payroll Amount |  |  |
| Hca_RawEmploymentStatus | STRING | Payroll Employment Status |  |  |
| Hca_RawPaycodeName | STRING | Payroll Paycode Name |  |  |
| M_Hca_RawStandard_Hrs | FLOAT | Payroll Standard Hours |  |  |
| M_Hca_Np_Amt | FLOAT | Pay Period Non Productive Amount |  |  |
| M_Hca_Np_Hrs | FLOAT | Pay Period Non Productive Hours |  |  |
| M_Hca_NpOthAgncy_Amt | FLOAT | Pay Period Non Productive Other Agency Amount |  |  |
| M_Hca_NpOthAgncy_Hrs | FLOAT | Pay Period Non Productive Other Agency Hours |  |  |
| M_Hca_NpOthFltin_Amt | FLOAT | Pay Period Non Productive Other Float In Amount |  |  |
| M_Hca_NpOthFltin_Hrs | FLOAT | Pay Period Non Productive Other Float In Hours |  |  |
| M_Hca_NpOthFltout_Amt | FLOAT | Pay Period Non Productive Other Float Out Amount |  |  |
| M_Hca_NpOthFltout_Hrs | FLOAT | Pay Period Non Productive Other Float Out Hours |  |  |
| M_Hca_NpOthFt_Amt | FLOAT | Pay Period Non Productive Other Full Time Amount |  |  |
| M_Hca_NpFt_Hrs | FLOAT | Pay Period Non Productive Other Full Time Hours |  |  |
| M_Hca_NpOthPdiem_Amt | FLOAT | Pay Period Non Productive Other Pdiem Amount |  |  |
| M_Hca_NpOthPdiem_Hrs | FLOAT | Pay Period Non Productive Other Pdiem Hours |  |  |
| M_Hca_NpOthPool_Amt | FLOAT | Pay Period Non Productive Other Pool Amount |  |  |
| M_Hca_NpOthPool_Hrs | FLOAT | Pay Period Non Productive Other Pool Hours |  |  |
| M_Hca_NpOthPt_Amt | FLOAT | Pay Period Non Productive Other Part Time Amount |  |  |
| M_Hca_NpOthPt_Hrs | FLOAT | Pay Period Non Productive Other Part Time Hours |  |  |
| M_Hca_NpRnpAgncy_Amt | FLOAT | Pay Period Non Productive Agency Amount |  |  |
| M_Hca_NpRnpAgncy_Hrs | FLOAT | Pay Period Non Productive Agency Hours |  |  |
| M_Hca_NpRnpFltin_Amt | FLOAT | Pay Period Non Productive Float In Amount |  |  |
| M_Hca_NpRnpFltin_Hrs | FLOAT | Pay Period Non Productive Float In Hours |  |  |
| M_Hca_NpRnpFltout_Amt | FLOAT | Pay Period Non Productive Float Out Amount |  |  |
| M_Hca_NpRnpFltout_Hrs | FLOAT | Pay Period Non Productive Float Out Hours |  |  |
| M_Hca_NpRnpFt_Amt | FLOAT | Pay Period Non Productive Full Time Amount |  |  |
| M_Hca_NpRnpFt_Hrs | FLOAT | Pay Period Non Productive Full Time Hours |  |  |
| M_Hca_NpRnpIntagncy_Amt | FLOAT | Pay Period Non Productive Internal Agency Amount |  |  |
| M_Hca_NpRnpIntagncy_Hrs | FLOAT | Pay Period Non Productive Internal Agency Hours |  |  |
| M_Hca_NpRnpPdiem_Amt | FLOAT | Pay Period Non Productive Pdiem Amount |  |  |
| M_Hca_NpRnpPdiem_Hrs | FLOAT | Pay Period Non Productive Pdiem Hours |  |  |
| M_Hca_NpRnpPool_Amt | FLOAT | Pay Period Non Productive Pool Amount |  |  |
| M_Hca_NpRnpPool_Hrs | FLOAT | Pay Period Non Productive Pool Hours |  |  |
| M_Hca_NpRnpPt_Amt | FLOAT | Pay Period Non Productive Part Time Amount |  |  |
| M_Hca_NpRnpPt_Hrs | FLOAT | Pay Period Non Productive Part Time Hours |  |  |
| M_Hca_NpRnp1Agncy_Amt | FLOAT | Pay Period Non Productive1 Agency Amount |  |  |
| M_Hca_NpRnp1Agncy_Hrs | FLOAT | Pay Period Non Productive1 Agency Hours |  |  |
| M_Hca_NpRnp1Fltin_Amt | FLOAT | Pay Period Non Productive1 Float In Amount |  |  |
| M_Hca_NpRnp1Fltin_Hrs | FLOAT | Pay Period Non Productive1 Float In Hours |  |  |
| M_Hca_NpRnp1Fltout_Amt | FLOAT | Pay Period Non Productive1 Float Out Amount |  |  |
| M_Hca_NpRnp1Fltout_Hrs | FLOAT | Pay Period Non Productive1 Float Out Hours |  |  |
| M_Hca_NpRnp1Ft_Amt | FLOAT | Pay Period Non Productive1 Full Time Amount |  |  |
| M_Hca_NpRnp1Ft_Hrs | FLOAT | Pay Period Non Productive1 Full Time Hours |  |  |
| M_Hca_NpRnp1Intagncy_Amt | FLOAT | Pay Period Non Productive1 Internal Agency Amount |  |  |
| M_Hca_NpRnp1Intagncy_Hrs | FLOAT | Pay Period Non Productive1 Internal Agency Hours |  |  |
| M_Hca_NpRnp1Pdiem_Amt | FLOAT | Pay Period Non Productive1 Pool Amount |  |  |
| M_Hca_NpRnp1Pdiem_Hrs | FLOAT | Pay Period Non Productive1 Pool Hours |  |  |
| M_Hca_NpRnp1Pool_Amt | FLOAT | Pay Period Non Productive1 Part Time Amount |  |  |
| M_Hca_NpRnp1Pool_Hrs | FLOAT | Pay Period Non Productive1 Part Time Hours |  |  |
| M_Hca_NpRnp1Pt_Amt | FLOAT | Pay Period Non Productive1 Pdiem Amount |  |  |
| M_Hca_NpRnp1Pt_Hrs | FLOAT | Pay Period Non Productive1 Pdiem Hours |  |  |
| M_Hca_NpRnp2Agncy_Amt | FLOAT | Pay Period Non Productive2 Agency Amount |  |  |
| M_Hca_NpRnp2Agncy_Hrs | FLOAT | Pay Period Non Productive2 Agency Hours |  |  |
| M_Hca_NpRnp2Fltin_Amt | FLOAT | Pay Period Non Productive2 Float In Amount |  |  |
| M_Hca_NpRnp2Fltin_Hrs | FLOAT | Pay Period Non Productive2 Float In Hours |  |  |
| M_Hca_NpRnp2Fltout_Amt | FLOAT | Pay Period Non Productive2 Float Out Amount |  |  |
| M_Hca_NpRnp2Fltout_Hrs | FLOAT | Pay Period Non Productive2 Float Out Hours |  |  |
| M_Hca_NpRnp2Ft_Amt | FLOAT | Pay Period Non Productive2 Full Time Amount |  |  |
| M_Hca_NpRnp2Ft_Hrs | FLOAT | Pay Period Non Productive2 Full Time Hours |  |  |
| M_Hca_NpRnp2Intagncy_Amt | FLOAT | Pay Period Non Productive2 Internal Agency Amount |  |  |
| M_Hca_NpRnp2Intagncy_Hrs | FLOAT | Pay Period Non Productive2 Internal Agency Hours |  |  |
| M_Hca_NpRnp2Pool_Amt | FLOAT | Pay Period Non Productive2 Pdiem Amount |  |  |
| M_Hca_NpRnp2Pool_Hrs | FLOAT | Pay Period Non Productive2 Pdiem Hours |  |  |
| M_Hca_NpRnp2Pt_Amt | FLOAT | Pay Period Non Productive2 Pool Amount |  |  |
| M_Hca_NpRnp2Pt_Hrs | FLOAT | Pay Period Non Productive2 Pool Hours |  |  |
| M_Hca_Ot_Hrs | FLOAT | Pay Period Overtime Hours |  |  |
| M_Hca_Ot_Amt | FLOAT | Pay Period Overtime Amount |  |  |
| M_Hca_PaidAgncy_Amt | FLOAT | Pay Period Paid Agency Amount |  |  |
| M_Hca_NpRnp2Pdiem_Amt | FLOAT | Pay Period Non Productive2 Part Time Amount |  |  |
| M_Hca_NpRnp2Pdiem_Hrs | FLOAT | Pay Period Non Productive2 Part Time Hours |  |  |
| M_Hca_PaidAgncy_Hrs | FLOAT | Pay Period Paid Agency Hours |  |  |
| M_Hca_Paid_Amt | FLOAT | Pay Period Paid Amount |  |  |
| M_Hca_Paid_Hrs | FLOAT | Pay Period Paid Hours |  |  |
| M_Hca_PaidFltin_Amt | FLOAT | Pay Period Paid Float In Amount |  |  |
| M_Hca_PaidFltin_Hrs | FLOAT | Pay Period Paid Float In Hours |  |  |
| M_Hca_PaidFltout_Amt | FLOAT | Pay Period Paid Float Out Amount |  |  |
| M_Hca_PaidFltout_Hrs | FLOAT | Pay Period Paid Float Out Hours |  |  |
| M_Hca_PaidFt_Amt | FLOAT | Pay Period Paid Full Time Amount |  |  |
| M_Hca_PaidFt_Hrs | FLOAT | Pay Period Paid Full Time Hours |  |  |
| M_Hca_PaidIntagncy_Amt | FLOAT | Pay Period Paid Internal Agency Amount |  |  |
| M_Hca_PaidIntagncy_Hrs | FLOAT | Pay Period Paid Internal Agency Hours |  |  |
| M_Hca_PaidPdiem_Amt | FLOAT | Pay Period Paid Per Diem Amount |  |  |
| M_Hca_PaidPdiem_Hrs | FLOAT | Pay Period Paid Per Diem Hours |  |  |
| M_Hca_PaidPool_Amt | FLOAT | Pay Period Paid Pool Amount |  |  |
| M_Hca_PaidPool_Hrs | FLOAT | Pay Period Paid Pool Hours |  |  |
| M_Hca_PaidPt_Amt | FLOAT | Pay Period Paid Part Time Amount |  |  |
| M_Hca_PaidPt_Hrs | FLOAT | Pay Period Paid Part Time Hours |  |  |
| M_Hca_ProdAgncy_Amt | FLOAT | Pay Period Productive Agency Amount |  |  |
| M_Hca_ProdAgncy_Hrs | FLOAT | Pay Period Productive Agency Hours |  |  |
| M_Hca_Prod_Amt | FLOAT | Pay Period Productive Amount |  |  |
| M_Hca_Prod_Hrs | FLOAT | Pay Period Productive Hours |  |  |
| M_Hca_PaidExtraptPt_Amt | FLOAT | Pay Period Paid Extra Part Time Amount |  |  |
| M_Hca_PaidExtraptPt_Hrs | FLOAT | Pay Period Paid Extra Part Time Hours |  |  |
| M_Hca_ProdIntagncy_Amt | FLOAT | Pay Period Productive Internal Agency Amount |  |  |
| M_Hca_ProdIntagncy_Hrs | FLOAT | Pay Period Productive Internal Agency Hours |  |  |
| M_Hca_ProdOtAgncy_Amt | FLOAT | Pay Period  Productive Overtime Agency Amount |  |  |
| M_Hca_ProdOtAgncy_Hrs | FLOAT | Pay Period  Productive Overtime Agency Hours |  |  |
| M_Hca_ProdOtFltin_Amt | FLOAT | Pay Period Productive Overtime Float In Amount |  |  |
| M_Hca_ProdOtFltin_Hrs | FLOAT | Pay Period Productive Overtime Float In Hours |  |  |
| M_Hca_ProdOtFltout_Amt | FLOAT | Pay Period Productive Overtime Float Out Amount |  |  |
| M_Hca_ProdOtFltout_Hrs | FLOAT | Pay Period Productive Overtime Float Out Hours |  |  |
| M_Hca_ProdOtFt_Amt | FLOAT | Pay Period Productive Overtime Full Time Amount |  |  |
| M_Hca_ProdOtFt_Hrs | FLOAT | Pay Period Productive Overtime Full Time Hours |  |  |
| M_Hca_ProdOtIntagncy_Amt | FLOAT | Pay Period Productive Overtime Internal Agency Amount |  |  |
| M_Hca_ProdOtIntagncy_Hrs | FLOAT | Pay Period Productive Overtime Internal Agency Hours |  |  |
| M_Hca_ProdOtPdiem_Amt | FLOAT | Pay Period  Productive Overtime Pdiem Amount |  |  |
| M_Hca_ProdOtPdiem_Hrs | FLOAT | Pay Period  Productive Overtime Pdiem Hours |  |  |
| M_Hca_ProdOtPool_Amt | FLOAT | Pay Period  Productive Overtime Pool Amount |  |  |
| M_Hca_ProdOtPool_Hrs | FLOAT | Pay Period  Productive Overtime Pool Hours |  |  |
| M_Hca_ProdOtPt_Amt | FLOAT | Pay Period Productive Overtime Part Time Amount |  |  |
| M_Hca_ProdOtPt_Hrs | FLOAT | Pay Period Productive Overtime Part Time Hours |  |  |
| M_Hca_ProdOthAgncy_Amt | FLOAT | Pay Period  Productive Other Agency Amount |  |  |
| M_Hca_ProdOthAgncy_Hrs | FLOAT | Pay Period  Productive Other Agency Hours |  |  |
| M_Hca_ProdOthFltin_Amt | FLOAT | Pay Period Productive Other Float In Amount |  |  |
| M_Hca_ProdOthFltin_Hrs | FLOAT | Pay Period Productive Other Float In Hours |  |  |
| M_Hca_ProdOthFltout_Amt | FLOAT | Pay Period Productive Other Float Out Amount |  |  |
| M_Hca_ProdOthFltout_Hrs | FLOAT | Pay Period Productive Other Float Out Hours |  |  |
| M_Hca_ProdOthFt_Amt | FLOAT | Pay Period Productive Other Full Time Amount |  |  |
| M_Hca_ProdOthFt_Hrs | FLOAT | Pay Period Productive Other Full Time Hours |  |  |
| M_Hca_ProdOthIntagncy_Amt | FLOAT | Pay Period Productive Other Internal Agency Amount |  |  |
| M_Hca_ProdOthIntagncy_Hrs | FLOAT | Pay Period Productive Other Internal Agency Hours |  |  |
| M_Hca_ProdOthPdiem_Amt | FLOAT | Pay Period  Productive Other Pdiem Amount |  |  |
| M_Hca_ProdOthPdiem_Hrs | FLOAT | Pay Period  Productive Other Pdiem Hours |  |  |
| M_Hca_ProdOthPool_Amt | FLOAT | Pay Period  Productive Other Pool Amount |  |  |
| M_Hca_ProdOthPool_Hrs | FLOAT | Pay Period  Productive Other Pool Hours |  |  |
| M_Hca_ProdOthPt_Amt | FLOAT | Pay Period Productive Other Part Time Amount |  |  |
| M_Hca_ProdOthPt_Hrs | FLOAT | Pay Period Productive Other Part Time Hours |  |  |
| M_Hca_ProdRegAgncy_Amt | FLOAT | Pay Period  Productive Other Agency Amount |  |  |
| M_Hca_ProdRegAgncy_Hrs | FLOAT | Pay Period  Productive Other Agency Hours |  |  |
| M_Hca_ProdRegFltin_Amt | FLOAT | Pay Period Productive Other Float In Amount |  |  |
| M_Hca_ProdRegFltin_Hrs | FLOAT | Pay Period Productive Other Float In Hours |  |  |
| M_Hca_ProdRegFltout_Amt | FLOAT | Pay Period Productive Other Float Out Amount |  |  |
| M_Hca_ProdRegFltout_Hrs | FLOAT | Pay Period Productive Other Float Out Hours |  |  |
| M_Hca_ProdRegFt_Amt | FLOAT | Pay Period Productive Other Full Time Amount |  |  |
| M_Hca_ProdRegFt_Hrs | FLOAT | Pay Period Productive Other Full Time Hours |  |  |
| M_Hca_ProdRegIntagncy_Amt | FLOAT | Pay Period Productive Other Internal Agency Amount |  |  |
| M_Hca_ProdRegIntagncy_Hrs | FLOAT | Pay Period Productive Other Internal Agency Hours |  |  |
| M_Hca_ProdRegPdiem_Amt | FLOAT | Pay Period  Productive Other Pdiem Amount |  |  |
| M_Hca_ProdRegPdiem_Hrs | FLOAT | Pay Period  Productive Other Pdiem Hours |  |  |
| M_Hca_ProdRegPool_Amt | FLOAT | Pay Period  Productive Other Pool Amount |  |  |
| M_Hca_ProdRegPool_Hrs | FLOAT | Pay Period  Productive Other Pool Hours |  |  |
| M_Hca_ProdRegPt_Amt | FLOAT | Pay Period Productive Other Part Time Amount |  |  |
| M_Hca_ProdRegPt_Hrs | FLOAT | Pay Period Productive Other Part Time Hours |  |  |
| M_Hcakpi_CombTotpaidAgncy_Amt | FLOAT | Pay Period Combined Agency Amount Total |  |  |
| M_Hcakpi_CombTotpaidAgncy_Hrs | FLOAT | Pay Period Combined Agency Paid Hours Total |  |  |
| M_Hcakpi_CombTotpaidFltin_Amt | FLOAT | Pay Period Combined Float In Amount Total |  |  |
| M_Hcakpi_CombTotpaidFltin_Hrs | FLOAT | Pay Period Combined Float In Paid Hours Total |  |  |
| M_Hcakpi_CombTotpaidFt_Amt | FLOAT | Pay Period Combined Full Time Amount Total |  |  |
| M_Hcakpi_CombTotpaidFt_Hrs | FLOAT | Pay Period Combined Full Time Paid Hours Total |  |  |
| M_Hcakpi_CombTotpaidIntagncy_Amt | FLOAT | Pay Period Combined Internal Agency Amount Total |  |  |
| M_Hcakpi_CombTotpaidIntagncy_Hrs | FLOAT | Pay Period Combined Internal Agency Hours Total |  |  |
| M_Hcakpi_CombTotpaidPdiem_Amt | FLOAT | Pay Period Combined Per Diem Amount Total |  |  |
| M_Hcakpi_CombTotpaidPdiem_Hrs | FLOAT | Pay Period Combined Per Diem Hours Total |  |  |
| M_Hcakpi_CombTotpaidPool_Amt | FLOAT | Pay Period Combined Pool Amount Total |  |  |
| M_Hcakpi_CombTotpaidPool_Hrs | FLOAT | Pay Period Combined Pool Hours Total |  |  |
| M_Hcakpi_CombTotpaidPt_Amt | FLOAT | Pay Period Combined Part Time Amount Total |  |  |
| M_Hcakpi_CombTotpaidPt_Hrs | FLOAT | Pay Period Combined Part Time Hours Total |  |  |
| M_Hcakpi_NpTotAgncy_Amt | FLOAT | Pay Period Non Productive Agency Amount Total |  |  |
| M_Hcakpi_NpTotAgncy_Hrs | FLOAT | Pay Period Non Productive Agency Hours Total |  |  |
| M_Hcakpi_NpTotFltin_Amt | FLOAT | Pay Period Non Productive Float In Amount Total |  |  |
| M_Hcakpi_NpTotFltin_Hrs | FLOAT | Pay Period Non Productive Float In Hours Total |  |  |
| M_Hcakpi_NpTotFt_Amt | FLOAT | Pay Period Non Productive Full Time Amount Total |  |  |
| M_Hcakpi_NpTotFt_Hrs | FLOAT | Pay Period Non Productive Full Time Hours Total |  |  |
| M_Hcakpi_NpTotIntagncy_Amt | FLOAT | Pay Period Non Productive Internal Agency Amount Total |  |  |
| M_Hcakpi_NpTotIntagncy_Hrs | FLOAT | Pay Period Non Productive Internal Agency Hours Total |  |  |
| M_Hcakpi_NpTotPdiem_Amt | FLOAT | Pay Period Non Productive Per Diem Amount Total |  |  |
| M_Hcakpi_NpTotPdiem_Hrs | FLOAT | Pay Period Non Productive Per Diem Hours Total |  |  |
| M_Hcakpi_NpTotPool_Amt | FLOAT | Pay Period Non Productive Pool Amount Total |  |  |
| M_Hcakpi_NpTotPool_Hrs | FLOAT | Pay Period Non Productive Pool Hours Total |  |  |
| M_Hcakpi_NpTotPt_Amt | FLOAT | Pay Period Non Productive Part Time Amount Total |  |  |
| M_Hcakpi_NpTotPt_Hrs | FLOAT | Pay Period Non Productive Part Time Hours Total |  |  |
| M_Hcakpi_ProdTotAgncy_Amt | FLOAT | Pay Period Productive Agency Amount Total |  |  |
| M_Hcakpi_ProdTotAgncy_Hrs | FLOAT | Pay Period Productive Agency Hours Total |  |  |
| M_Hcakpi_ProdTotFltin_Amt | FLOAT | Pay Period Productive Float In Amount Total |  |  |
| M_Hcakpi_ProdTotFltin_Hrs | FLOAT | Pay Period Productive Float In Hours Total |  |  |
| M_Hcakpi_ProdTotFt_Amt | FLOAT | Pay Period Productive Full Time Amount Total |  |  |
| M_Hcakpi_ProdTotFt_Hrs | FLOAT | Pay Period Productive Full Time Amount Total |  |  |
| M_Hcakpi_ProdTotIntagncy_Amt | FLOAT | Pay Period Productive Internal Agency Amount Total |  |  |
| M_Hcakpi_ProdTotIntagncy_Hrs | FLOAT | Pay Period Productive Internal Agency Hours Total |  |  |
| M_Hcakpi_ProdTotPdiem_Amt | FLOAT | Pay Period Productive Per Diem Amount Total |  |  |
| M_Hcakpi_ProdTotPdiem_Hrs | FLOAT | Pay Period Productive Pool Amount Total |  |  |
| M_Hcakpi_ProdTotPool_Amt | FLOAT | Pay Period Productive Pool Hours Total |  |  |
| M_Hcakpi_ProdTotPool_Hrs | FLOAT | Pay Period Productive Part Time Amount Total |  |  |
| M_Hcakpi_ProdTotPt_Amt | FLOAT | Pay Period Productive Part Time Hours Total |  |  |
| M_Hcakpi_ProdTotPt_Hrs | FLOAT | Pay Period Productive Per Diem Hours Total |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| Bus_orgName | STRING | Name of the Org Node as entered in WFD (single value) |  |  |
| Bus_orgFullName | STRING | Full Name of the Org Node as entered in WFD (single value) |  |  |
| Bus_orgDescription | STRING | Description of the Org Node as entered in WFD (single value) |  |  |
| Bus_orgEffectiveDate | DATE | Effective date of the current record (Should not be used for joins) |  |  |
| Bus_orgExpirationDate | DATE | Expiration date of the current record (Should not be used for joins) |  |  |
| Bus_orgTypeId | INT64 | Org Type(ID) in the Business Structure that this node is configured. |  |  |
| Bus_orgTypeName | STRING | Org Type(Name) in the Business Structure that this node is configured. |  |  |
| Bus_orgPathTxt | STRING | Full path in the business structure down to this node. |  |  |
| Bus_orgContextName | STRING | Can only be ORG or FORECAST |  |  |
| Bus_orgLocationCategory | STRING | Category, Department, or Site,   used for Forecasting (Retail) |  |  |
| Bus_orgBreak0 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration.  This is ALWAYS the CATEGORY level of the business structure (For Volume Only) |  |  |
| Bus_orgBreak1 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration.  This is ALWAYS the JOB level of the business structure |  |  |
| Bus_orgBreak2 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak3 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak4 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak5 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak6 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak7 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak8 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak9 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak10 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak11 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak12 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak13 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak14 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak15 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak16 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak17 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak18 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak19 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak20 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak21 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak22 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak23 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak24 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak25 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak0Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration.  This is ALWAYS the CATEGORY level of the business structure (For Volume Only) |  |  |
| Bus_orgBreak1Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration.  This is ALWAYS the JOB level of the business structure |  |  |
| Bus_orgBreak2Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak3Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak4Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak5Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak6Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak7Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak8Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak9Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak10Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak11Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak12Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak13Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak14Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak15Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak16Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak17Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak18Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak19Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak20Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak21Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak22Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak23Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak24Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak25Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Person_PersonNumber | STRING | Person Number | PII |  |
| Person_FullName | STRING | Person Number | PII |  |
| Person_IsEmployeeSwt | BOOLEAN | Full Name | PII |  |
| Person_IsManagerSwt | BOOLEAN | Boolean indicator whether or not this person is a employee |  |  |
| Person_HourlyRate | FLOAT | Boolean indicator whether or not this person is a manager |  |  |
| Person_HireDate | DATE | Hourly Rate | Confidential |  |
| Person_SeniorityDate | DATE | Hire Date |  |  |
| Person_SupervisorPersonNumber | STRING | Seniority Date |  |  |
| Person_SupervisorFullName | STRING | Supervisor Person Nunber | PII |  |
| Person_EmploymentTerm | STRING | Supervisor Name | PII |  |
| Person_WorkerType | STRING | Employment Term |  |  |
| Person_ExpectedDailyHours | FLOAT | Worker Type |  |  |
| Person_PrimaryLaborCategory | STRING | Primary Labor Category |  |  |
| Person_PrimaryLaborEntryName1 | STRING | Primary Labor Entry Name 1 |  |  |
| Person_PrimaryLaborEntryName2 | STRING | Primary Labor Entry Name 2 |  |  |
| Person_PrimaryLaborEntryName3 | STRING | Primary Labor Entry Name 3 |  |  |
| Person_PrimaryLaborEntryName4 | STRING | Primary Labor Entry Name 4 |  |  |
| Person_PrimaryLaborEntryName5 | STRING | Primary Labor Entry Name 5 |  |  |
| Person_PrimaryLaborEntryName6 | STRING | Primary Labor Entry Name 6 |  |  |
| Person_primaryOrgPathTxt | STRING | Primary Org Path |  |  |
| Person_employmentStatus | STRING | Employment Status |  |  |
| Person_timeEntryType | STRING | Time entry type |  |  |
| Person_shiftCode | STRING | Shift Code |  |  |
| Person_birthDate | DATE | Birth date | Confidential |  |
| Person_fullTimeStandardHoursQuantity | FLOAT | FT Standard Hours Qty |  |  |
| Person_FullTimeEquivalencyPercent | FLOAT | FTE Percent |  |  |
| Person_ProExternalId | STRING | Primary Org Path |  |  |
| Person_contactData | STRING | Contact information | PII |  |
| Person_zipCode | STRING | Zip Code | PII |  |
| Person_state | STRING | State | PII |  |
| Person_city | STRING | City | PII |  |
| Person_country | STRING | Country | PII |  |
| BusPri_primaryOrgId | INT64 | Primary Org Id |  |  |
| BusPri_PrimaryOrgName | STRING | Primary Org Name |  |  |
| BusPri_primaryOrgFullName | STRING | Primary Org Full Name |  |  |
| BusPri_primaryOrgDescription | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak0 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak1 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak2 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak3 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak4 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak5 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak6 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak7 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak8 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak9 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak10 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak11 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak12 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak13 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak14 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak15 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak16 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak17 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak18 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak19 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak20 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Person_CustomText1 | STRING | Custom Text | PII |  |
| Person_CustomText2 | STRING | Custom Text | PII |  |
| Person_CustomText3 | STRING | Custom Text | PII |  |
| Person_CustomText4 | STRING | Custom Text | PII |  |
| Person_CustomText5 | STRING | Custom Text | PII |  |
| Person_CustomText6 | STRING | Custom Text | PII |  |
| Person_CustomText7 | STRING | Custom Text | PII |  |
| Person_CustomText8 | STRING | Custom Text | PII |  |
| Person_CustomText9 | STRING | Custom Text | PII |  |
| Person_CustomText10 | STRING | Custom Text | PII |  |
| Person_CustomText11 | STRING | Custom Text | PII |  |
| Person_CustomText12 | STRING | Custom Text | PII |  |
| Person_CustomText13 | STRING | Custom Text | PII |  |
| Person_CustomText14 | STRING | Custom Text | PII |  |
| Person_CustomText15 | STRING | Custom Text | PII |  |
| Person_CustomText16 | STRING | Custom Text | PII |  |
| Person_CustomText17 | STRING | Custom Text | PII |  |
| Person_CustomText18 | STRING | Custom Text | PII |  |
| Person_CustomText19 | STRING | Custom Text | PII |  |
| Person_CustomText20 | STRING | Custom Text | PII |  |
| Person_CustomText21 | STRING | Custom Text | PII |  |
| Person_CustomText22 | STRING | Custom Text | PII |  |
| Person_CustomText23 | STRING | Custom Text | PII |  |
| Person_CustomText24 | STRING | Custom Text | PII |  |
| Person_CustomText25 | STRING | Custom Text | PII |  |
| Person_CustomText26 | STRING | Custom Text | PII |  |
| Person_CustomText27 | STRING | Custom Text | PII |  |
| Person_CustomText28 | STRING | Custom Text | PII |  |
| Person_CustomText29 | STRING | Custom Text | PII |  |
| Person_CustomText30 | STRING | Custom Text | PII |  |
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
| PP_startDate | DATE | Pay Period start date |  |  |
| PP_endDate | DATE | Pay Period end date |  |  |
| PP_payPeriod | STRING | Pay Period name |  |  |
| PP_payPeriodOffset | INT64 | Number of pay period back or forward from current pay period |  |  |
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
