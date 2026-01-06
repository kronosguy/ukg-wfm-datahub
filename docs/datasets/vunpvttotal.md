# vUnpvtTotal

**Group:** Summary Dataset → metricsIntra (vKronosIntraSummary)

-

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vUnpvtTotal |
| Unique Identifier | partitionDate,orgId,personId |
| Source Pipeline |  |

## Columns

**Column count:** 151

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| costCenter | STRING | Cost Center name |  |  |
| laborEntryName1 | STRING | Labor Category 1 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName2 | STRING | Labor Category 2 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName3 | STRING | Labor Category 3 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName4 | STRING | Labor Category 4 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName5 | STRING | Labor Category 5 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName6 | STRING | Labor Category 6 entry name associated with transaction (applies to labor category transfer) |  |  |
| paycodeId | INT64 | Unique identifier of a pay code. Joins to pay code dimension |  |  |
| M_Schd_All_Hrs | FLOAT64 | Scheduled All Hours |  |  |
| M_Schd_All_Amt | FLOAT64 | Scheduled All Amount |  |  |
| M_Schd_Paid_Hrs | FLOAT64 | Scheduled Paid Hours |  |  |
| M_Schd_Paid_Amt | FLOAT64 | Scheduled Paid Amount |  |  |
| M_Schd_Prod_Hrs | FLOAT64 | Scheduled Prod Hours |  |  |
| M_Schd_Prod_Amt | FLOAT64 | Scheduled Prod Amount |  |  |
| M_Schd_Reg_Hrs | FLOAT64 | Scheduled Reg Hours |  |  |
| M_Schd_Reg_Amt | FLOAT64 | Scheduled Reg Amount |  |  |
| M_Schd_OnCall_Hrs | FLOAT64 | Scheduled OnCall Hours |  |  |
| M_Schd_OnCall_Amt | FLOAT64 | Scheduled OnCall Amount |  |  |
| M_Schd_AbsPaid_Hrs | FLOAT64 | Scheduled Absence Paid Hours |  |  |
| M_Schd_AbsUnpaid_Hrs | FLOAT64 | Scheduled Absence Unpaid Hours |  |  |
| M_Schd_AbsPaid_Amt | FLOAT64 | Scheduled Absence Paid Amount |  |  |
| M_Schd_AbsUnpaid_Amt | FLOAT64 | Scheduled Absence Unpaid Amount |  |  |
| M_Schd_AbsPlannedPaid_Hrs | FLOAT64 | Scheduled Absence PlannedPaid Hours |  |  |
| M_Schd_AbsPlannedUnpaid_Hrs | FLOAT64 | Scheduled Absence PlannedUnpaid Hours |  |  |
| M_Schd_AbsPlannedPaid_Amt | FLOAT64 | Scheduled Absence PlannedPaid Amount |  |  |
| M_Schd_AbsPlannedUnpaid_Amt | FLOAT64 | Scheduled Absence PlannedUnpaid Amount |  |  |
| M_Schd_AbsUnplannedPaid_Hrs | FLOAT64 | Scheduled Absence UnplannedPaid Hours |  |  |
| M_Schd_AbsUnplannedUnpaid_Hrs | FLOAT64 | Scheduled Absence UnplannedUnpaid Hours |  |  |
| M_Schd_AbsUnplannedPaid_Amt | FLOAT64 | Scheduled Absence UnplannedPaid Amount |  |  |
| M_Schd_AbsUnplannedUnpaid_Amt | FLOAT64 | Scheduled Absence UnplannedUnpaid Amount |  |  |
| M_Schd_AbsExtendedPaid_Hrs | FLOAT64 | Scheduled Absence ExtendedPaid Hours |  |  |
| M_Schd_AbsExtendedUnpaid_Hrs | FLOAT64 | Scheduled Absence ExtendedUnpaid Hours |  |  |
| M_Schd_AbsExtendedPaid_Amt | FLOAT64 | Scheduled Absence ExtendedPaid Amount |  |  |
| M_Schd_AbsExtendedUnpaid_Amt | FLOAT64 | Scheduled Absence ExtendedUnpaid Amount |  |  |
| M_Schd_TrnProd_Hrs | FLOAT64 | Scheduled Training Prod Hours |  |  |
| M_Schd_TrnProd_Amt | FLOAT64 | Scheduled Training Prod Amount |  |  |
| M_Schd_TrnNonprod_Hrs | FLOAT64 | Scheduled Training Nonprod Hours |  |  |
| M_Schd_TrnNonprod_Amt | FLOAT64 | Scheduled Training Nonprod Amount |  |  |
| M_Schd_Other_Hrs | FLOAT64 | Scheduled Other Hours |  |  |
| M_Schd_Other_Amt | FLOAT64 | Scheduled Other Amount |  |  |
| M_Schd_MealPenalty_Hrs | FLOAT64 | Scheduled  Meal Penalty Hours |  |  |
| M_Schd_MealPenalty_Amt | FLOAT64 | Scheduled  Meal Penalty Amount |  |  |
| M_Schd_HolidayPaid_Hrs | FLOAT64 | Scheduled HolidayPaid Hours |  |  |
| M_Schd_HolidayPaid_Amt | FLOAT64 | Scheduled HolidayPaid Amount |  |  |
| M_Schd_OT_Hrs | FLOAT64 | Scheduled OT Hours |  |  |
| M_Schd_OT_Amt | FLOAT64 | Scheduled OT Amount |  |  |
| M_Schd_CallBack_Hrs | FLOAT64 | Scheduled CallBack Hours |  |  |
| M_Schd_CallBack_Amt | FLOAT64 | Scheduled CallBack Amount |  |  |
| M_Schd_Core_Hrs | FLOAT64 | Scheduled Core Hours |  |  |
| M_Schd_Core_Amt | FLOAT64 | Scheduled Core Amount |  |  |
| M_Schd_Noncore_Hrs | FLOAT64 | Scheduled Noncore Hours |  |  |
| M_Schd_Noncore_Amt | FLOAT64 | Scheduled Noncore Amount |  |  |
| M_Act_All_Hrs | FLOAT64 | Actual All Hours |  |  |
| M_Act_All_Amt | FLOAT64 | Actual All Amount |  |  |
| M_Act_Paid_Hrs | FLOAT64 | Paid Hours |  |  |
| M_Act_Paid_Amt | FLOAT64 | Paid Amount |  |  |
| M_Act_Prod_Hrs | FLOAT64 | Prod Hours |  |  |
| M_Act_Prod_Amt | FLOAT64 | Prod Amount |  |  |
| M_Act_Reg_Hrs | FLOAT64 | Reg Hours |  |  |
| M_Act_Reg_Amt | FLOAT64 | Reg Amount |  |  |
| M_Act_OnCall_Hrs | FLOAT64 | OnCall Hours |  |  |
| M_Act_OnCall_Amt | FLOAT64 | OnCall Amount |  |  |
| M_Act_AbsPaid_Hrs | FLOAT64 | Absence Paid Hours |  |  |
| M_Act_AbsUnpaid_Hrs | FLOAT64 | Absence Unpaid Hours |  |  |
| M_Act_AbsPaid_Amt | FLOAT64 | Absence Paid Amount |  |  |
| M_Act_AbsUnpaid_Amt | FLOAT64 | Absence Unpaid Amount |  |  |
| M_Act_AbsPlannedPaid_Hrs | FLOAT64 | Absence Planned Paid Hours |  |  |
| M_Act_AbsPlannedUnpaid_Hrs | FLOAT64 | Absence Planned Unpaid Hours |  |  |
| M_Act_AbsPlannedPaid_Amt | FLOAT64 | Absence Planned Paid Amount |  |  |
| M_Act_AbsPlannedUnpaid_Amt | FLOAT64 | Absence Planned Unpaid Amount |  |  |
| M_Act_AbsUnplannedPaid_Hrs | FLOAT64 | Absence Unplanned Paid Hours |  |  |
| M_Act_AbsUnplannedUnpaid_Hrs | FLOAT64 | Absence Unplanned Unpaid Hours |  |  |
| M_Act_AbsUnplannedPaid_Amt | FLOAT64 | Absence Unplanned Paid Amount |  |  |
| M_Act_AbsUnplannedUnpaid_Amt | FLOAT64 | Absence Unplanned Unpaid Amount |  |  |
| M_Act_AbsExtendedPaid_Hrs | FLOAT64 | Extended Absence Paid Hours |  |  |
| M_Act_AbsExtendedUnpaid_Hrs | FLOAT64 | Extended Absence Unpaid Hours |  |  |
| M_Act_AbsExtendedPaid_Amt | FLOAT64 | Extended Absence Paid Amount |  |  |
| M_Act_AbsExtendedUnpaid_Amt | FLOAT64 | Extended Absence Unpaid Amount |  |  |
| M_Act_TrnProd_Hrs | FLOAT64 | Training Prod Hours |  |  |
| M_Act_TrnProd_Amt | FLOAT64 | Training Prod Amount |  |  |
| M_Act_TrnNonprod_Hrs | FLOAT64 | Training Nonprod Hours |  |  |
| M_Act_TrnNonprod_Amt | FLOAT64 | Training Nonprod Amount |  |  |
| M_Act_Other_Hrs | FLOAT64 | Other Hours |  |  |
| M_Act_Other_Amt | FLOAT64 | Other Amount |  |  |
| M_Act_MealPenalty_Hrs | FLOAT64 | Meal Penalty Hours |  |  |
| M_Act_MealPenalty_Amt | FLOAT64 | Meal Penalty Amount |  |  |
| M_Act_HolidayPaid_Hrs | FLOAT64 | Holiday Paid Hours |  |  |
| M_Act_HolidayPaid_Amt | FLOAT64 | Holiday Paid Amount |  |  |
| M_Act_OT_Hrs | FLOAT64 | OT Hours |  |  |
| M_Act_OT_Amt | FLOAT64 | OT Amount |  |  |
| M_Act_CallBack_Hrs | FLOAT64 | Callback Hours |  |  |
| M_Act_CallBack_Amt | FLOAT64 | Callback Amont |  |  |
| M_Act_Core_Hrs | FLOAT64 | Core Hours |  |  |
| M_Act_Core_Amt | FLOAT64 | Core Amount |  |  |
| M_Act_Noncore_Hrs | FLOAT64 | Noncore Hours |  |  |
| M_Act_Noncore_Amt | FLOAT64 | Noncore Amount |  |  |
| M_Proj_All_Hrs | FLOAT64 | Projected All Hours |  |  |
| M_Proj_All_Amt | FLOAT64 | Projected All Amount |  |  |
| M_Proj_Paid_Hrs | FLOAT64 | Projected Paid Hours |  |  |
| M_Proj_Paid_Amt | FLOAT64 | Projected Paid Amount |  |  |
| M_Proj_Prod_Hrs | FLOAT64 | Projected Prod Hours |  |  |
| M_Proj_Prod_Amt | FLOAT64 | Projected Prod Amount |  |  |
| M_Proj_Reg_Hrs | FLOAT64 | Projected Reg Hours |  |  |
| M_Proj_Reg_Amt | FLOAT64 | Projected Reg Amount |  |  |
| M_Proj_OnCall_Hrs | FLOAT64 | Projected OnCall Hours |  |  |
| M_Proj_OnCall_Amt | FLOAT64 | Projected OnCall Amount |  |  |
| M_Proj_AbsPaid_Hrs | FLOAT64 | Projected Absence Paid Hours |  |  |
| M_Proj_AbsUnpaid_Hrs | FLOAT64 | Projected Absence Unpaid Hours |  |  |
| M_Proj_AbsPaid_Amt | FLOAT64 | Projected Absence Paid Amount |  |  |
| M_Proj_AbsUnpaid_Amt | FLOAT64 | Projected Absence Unpaid Amount |  |  |
| M_Proj_AbsPlannedPaid_Hrs | FLOAT64 | Projected Absence PlannedPaid Hours |  |  |
| M_Proj_AbsPlannedUnpaid_Hrs | FLOAT64 | Projected Absence PlannedUnpaid Hours |  |  |
| M_Proj_AbsPlannedPaid_Amt | FLOAT64 | Projected Absence PlannedPaid Amount |  |  |
| M_Proj_AbsPlannedUnpaid_Amt | FLOAT64 | Projected Absence PlannedUnpaid Amount |  |  |
| M_Proj_AbsUnplannedPaid_Hrs | FLOAT64 | Projected Absence UnplannedPaid Hours |  |  |
| M_Proj_AbsUnplannedUnpaid_Hrs | FLOAT64 | Projected Absence UnplannedUnpaid Hours |  |  |
| M_Proj_AbsUnplannedPaid_Amt | FLOAT64 | Projected Absence UnplannedPaid Amount |  |  |
| M_Proj_AbsUnplannedUnpaid_Amt | FLOAT64 | Projected Absence UnplannedUnpaid Amount |  |  |
| M_Proj_AbsExtendedPaid_Hrs | FLOAT64 | Projected Absence ExtendedPaid Hours |  |  |
| M_Proj_AbsExtendedUnpaid_Hrs | FLOAT64 | Projected Absence ExtendedUnpaid Hours |  |  |
| M_Proj_AbsExtendedPaid_Amt | FLOAT64 | Projected Absence ExtendedPaid Amount |  |  |
| M_Proj_AbsExtendedUnpaid_Amt | FLOAT64 | Projected Absence ExtendedUnpaid Amount |  |  |
| M_Proj_TrnProd_Hrs | FLOAT64 | Projected Training Prod Hours |  |  |
| M_Proj_TrnProd_Amt | FLOAT64 | Projected Training Prod Amount |  |  |
| M_Proj_TrnNonprod_Hrs | FLOAT64 | Projected Training Nonprod Hours |  |  |
| M_Proj_TrnNonprod_Amt | FLOAT64 | Projected Training Nonprod Amount |  |  |
| M_Proj_Other_Hrs | FLOAT64 | Projected Other Hours |  |  |
| M_Proj_Other_Amt | FLOAT64 | Projected Other Amount |  |  |
| M_Proj_MealPenalty_Hrs | FLOAT64 | Projected  Meal Penalty Hours |  |  |
| M_Proj_MealPenalty_Amt | FLOAT64 | Projected  Meal Penalty Amount |  |  |
| M_Proj_HolidayPaid_Hrs | FLOAT64 | Projected HolidayPaid Hours |  |  |
| M_Proj_HolidayPaid_Amt | FLOAT64 | Projected HolidayPaid Amount |  |  |
| M_Proj_OT_Hrs | FLOAT64 | Projected OT Hours |  |  |
| M_Proj_OT_Amt | FLOAT64 | if isOTNetDownSwt then projectedWages will be deducted from Wages where Pay Category = Overtime |  |  |
| M_Proj_CallBack_Hrs | FLOAT64 | Projected CallBack Hours |  |  |
| M_Proj_CallBack_Amt | FLOAT64 | Projected CallBack Amount |  |  |
| M_Proj_Core_Hrs | FLOAT64 | Projected Core Hours |  |  |
| M_Proj_Core_Amt | FLOAT64 | Projected Core Amount |  |  |
| M_Proj_Noncore_Hrs | FLOAT64 | Projected Noncore Hours |  |  |
| M_Proj_Noncore_Amt | FLOAT64 | Projected Noncore Amount |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| currencyExchangeRates | STRING | a string value that contains the available currency and exchange rate needed for calculations |  |  |
| laborEntryDesc1 | STRING | Labor Category 1 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc2 | STRING | Labor Category 2 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc3 | STRING | Labor Category 3 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc4 | STRING | Labor Category 4 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc5 | STRING | Labor Category 5 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc6 | STRING | Labor Category 6 entry description associated with transaction (applies to labor category transfer) |  |  |
