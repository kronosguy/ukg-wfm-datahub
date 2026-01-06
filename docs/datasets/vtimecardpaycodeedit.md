# vTimecardPayCodeEdit

**Group:** Detail Dataset → Timecard Detail Views

- Paycode Edits applied to a timecard.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vTimecardPayCodeEdit |
| Unique Identifier | payCodeEditId,itemId |
| Source Pipeline | timecard (CDC) |

## Columns

**Column count:** 56

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| payCodeEditId | INT64 | Paycode Edit Id |  |  |
| itemId | INT64 | The ID of the time item. |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| amountType | STRING | Indicates if the pay code unit type of the amount paid was hours, money, or days |  |  |
| durationInDays | FLOAT64 | The duration (in days) of the pay code edit |  |  |
| durationInHours | FLOAT64 | The duration (in hours) of the pay code edit |  |  |
| moneyAmount | FLOAT64 | The amount (as a decimal value representing money) of the pay code edit. |  |  |
| overrideAcrrualAmount | FLOAT64 | The amount of override accrual days. Must be a value between -1 to 1. |  |  |
| paycode | INT64 | Paycode name |  |  |
| payCodeId | INT64 | Unique identifier of a pay code. Joins to pay code dimension |  |  |
| scheduleAmountType | STRING | An enumeration of the schedule amount. |  |  |
| scheduledShiftIds | INT64 (NESTED) | A nested list of Schedule Shift IDs |  |  |
| startTimeZoneId | STRING | Start time zone ID |  |  |
| startDateTime | DATETIME | The date and time of the start of the activity in ISO_LOCAL_DATE_TIME format (yyyy-MM-dd HH:mm:ss.SSS). |  |  |
| endTimeZoneId | STRING | End time zone ID |  |  |
| endDateTime | DATETIME | The end date and time of a date range in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). |  |  |
| editByType | STRING | A reference to the type of the user who made the change. Indicates whether the change was made by the employee or by someone else. | PII |  |
| editByTypeId | INT64 | Edit by type ID |  |  |
| workRule | STRING | Work Rule Name |  |  |
| workRuleId | INT64 | Work Rule ID |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| userEnteredCostCenter | STRING | A reference to the user-entered source cost center. |  |  |
| userEnteredCostCenterId | INT64 | User entered cost center ID |  |  |
| userEnteredLaborEntryName1 | STRING | Labor Category 1 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryDesc1 | STRING | Labor Category 1 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryName2 | STRING | Labor Category 2 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryDesc2 | STRING | Labor Category 2 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryName3 | STRING | Labor Category 3 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryDesc3 | STRING | Labor Category 3 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryName4 | STRING | Labor Category 4 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryDesc4 | STRING | Labor Category 4 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryName5 | STRING | Labor Category 5 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryDesc5 | STRING | Labor Category 5 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryName6 | STRING | Labor Category 6 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryDesc6 | STRING | Labor Category 6 entry description associated with transaction (applies to labor category transfer) |  |  |
| costCenter | STRING | Cost Center name |  |  |
| costCenterId | INT64 | Unique Identifier for a CostCenter joins to costCenter dimension |  |  |
| laborEntryName1 | STRING | Labor Category 1 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc1 | STRING | Labor Category 1 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName2 | STRING | Labor Category 2 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc2 | STRING | Labor Category 2 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName3 | STRING | Labor Category 3 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc3 | STRING | Labor Category 3 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName4 | STRING | Labor Category 4 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc4 | STRING | Labor Category 4 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName5 | STRING | Labor Category 5 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc5 | STRING | Labor Category 5 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName6 | STRING | Labor Category 6 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc6 | STRING | Labor Category 6 entry description associated with transaction (applies to labor category transfer) |  |  |
| commentsAvailableSwt | BOOLEAN | A Boolean indicator of whether or not Comments are associated with a pay code edit |  |  |
| editableSwt | BOOLEAN | A Boolean indicator of whether or not the pay code edit is editable |  |  |
| systemGeneratedSwt | BOOLEAN | A Boolean indicator of whether or not a pay code edit is system-generated. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| auditDate | DATE | The date the timecard pay code edit was entered |  |  |
| assignmentId | INT64 |  |  |  |
