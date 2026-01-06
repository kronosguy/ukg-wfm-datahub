# vScheduleTransaction

**Group:** Detail Dataset → Schedule Detail Views

Schedule Transaction Totals

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleTransaction |
| Unique Identifier | transactionId,personId,partitionDate,payCodeId |
| Source Pipeline | scheduleTransaction (CDC) |

## Columns

**Column count:** 54

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| transactionId | INT64 | Unique ID for schedule transaction |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| timeItemId | INT64 | The ID of the time item can be joined to to the following Views.column: vTimecardWorkShift.workedShiftId |  |  |
| timeItemTypeId | INT64 | The ID of the time item type |  |  |
| timeItemType | STRING | Description of the transaction i.e. REGULAR_SHIFT, CORRECTION_EDIT, PAYCODE_EDIT etc. |  |  |
| startDateTime | DATETIME | The inclusive start date and time segment from the totalizer note: this time is rounded if employee workRule has an associated Rounding rule for punches |  |  |
| endDateTime | DATETIME | The inclusive end date and time segment from the totalizer note: this time is rounded if employee workRule has an associated Rounding rule for punches |  |  |
| payCodeId | INT64 | Unique identifier of a pay code. Joins to pay code dimension |  |  |
| amountType | STRING | The type of transaction i.e. Money, Hour, Day |  |  |
| amountCurrencyCode | STRING | Currency code for Amount |  |  |
| durationInHours | FLOAT | Hours amount for totalized transaction |  |  |
| durationInDays | FLOAT | Days amount for totalized transaction |  |  |
| moneyAmount | FLOAT | Money amount for totalized transaction |  |  |
| wagesCurrencyCode | STRING | Currency code for wages |  |  |
| wages | FLOAT | Actual calculated totals as wages |  |  |
| activityId | INT64 | Activity id (Associated with Activities Data usually MFG vertical)  ** Do Not Use this value is not available or inaccurate ** |  |  |
| activity | STRING | Activity name (Associated with Activities Data usually MFG vertical)  ** Do Not Use this value is not available or inaccurate ** |  |  |
| workRuleId | INT64 | Unique identifier of a transfer work rule. Joins to workRule dimension |  |  |
| positionId | INT64 | The position id associated with an aggregated total |  |  |
| position | STRING | The position name associated with an aggregated total |  |  |
| payPeriodWeek | INT64 | A number representing a pay period week. |  |  |
| payPeriodNumber | INT64 | A number representing a pay period. |  |  |
| jobTransferSwt | BOOLEAN | Is this a job a transfer |  |  |
| laborTransferSwt | BOOLEAN | Is this labor category / cost center transfer |  |  |
| laborEntryName1 | STRING | Labor Category 1 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName2 | STRING | Labor Category 2 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName3 | STRING | Labor Category 3 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName4 | STRING | Labor Category 4 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName5 | STRING | Labor Category 5 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName6 | STRING | Labor Category 6 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc1 | STRING | Labor Category 1 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc2 | STRING | Labor Category 2 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc3 | STRING | Labor Category 3 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc4 | STRING | Labor Category 4 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc5 | STRING | Labor Category 5 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc6 | STRING | Labor Category 6 entry description associated with transaction (applies to labor category transfer) |  |  |
| costCenterId | INT64 | Value is null API is not returning correct value,  This will be addressed in a future release |  |  |
| costCenter | STRING | Cost center name at the time of the transaction |  |  |
| originalDate | DATE | Original date of the transaction i.e. if this was an historical correction this date would not match the partitionDate |  |  |
| originalMoneyAmountCurrencyCode | STRING | Currency code for Amount. Original Amount before Correction |  |  |
| originalMoneyAmount | FLOAT | Money amount for totalized transaction. Original Amount before Correction |  |  |
| originalDurationInHours | FLOAT | Hours amount for totalized transaction Original Amount before Correction |  |  |
| originalDurationInDays | FLOAT | Days amount for totalized transaction Original Amount before Correction |  |  |
| managerApprovalNeededSwt | BOOLEAN | A Boolean indicator of whether or not there is a total that has not been approved by a manager. |  |  |
| approvableByManagerSwt | BOOLEAN | A Boolean indicator of whether or not the aggregated total is approvable by the logged-in manager. |  |  |
| workWeekApplyDateTime | DATETIME | The date and time for which the totals are applied in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). This property is returned when the forWorkWeek request payload Boolean is 'true' |  |  |
| rate | FLOAT | Wage rate amount |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| payCode | STRING | Name of the pay code transactions are charged to - joins to pay code dimension |  |  |
| combined pay codeswt | BOOLEAN | Indicates if amount is associated with a combined pay code |  |  |
| wageMultiplier | FLOAT | Indicates pay code multiplier of hours times base wage - 1 is regular, 1.5 is premium pay, etc |  |  |
| wageAddition | FLOAT | Pay code wage addition amount |  |  |
