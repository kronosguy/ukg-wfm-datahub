# vTimecardWorkShiftSpan

**Group:** Detail Dataset → Timecard Detail Views

- worked shift "spans"  (pairs of punches as interpreted by the punch interpretation rules)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vTimecardWorkShiftSpan |
| Unique Identifier | workedShiftSpanUniqueId |
| Source Pipeline | timecard (CDC) |

## Columns

**Column count:** 47

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| workedShiftId | INT64 | Work Shift ID |  |  |
| partitionDate | DATE | Represents Date Part of startDateTime for the transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| workedShiftSpanId | INT64 | Worked Shift Span ID |  |  |
| startTimezone | STRING | Start timezone where the worked span was entered. Normally, this is the default or home timezone for the employee, but the worked span can include a different timezone as necessary. |  |  |
| startTimezoneId | INT64 | Start time zone ID |  |  |
| startDateTime | DATETIME | Work Span Start Date Time.  The start date and time of a date range in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). |  |  |
| roundedStartDateTime | DATETIME | Work Span Rounded Start Date Time.  The start date and time of a date range in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss) (Note: If an employee clocks in from one time zone and clocks out from another, the time zone associated with this value will align with the clock-in time zone. This ensures accurate calculation of the total hours worked.) |  |  |
| startPunchId | INT64 | Start punch ID |  |  |
| endTimezone | STRING | The end timezone where the worked span was entered. Normally, this is the default or home timezone for the employee, but the worked span can include a different timezone as necessary. |  |  |
| endTimezoneId | INT64 | End time zone ID |  |  |
| endDateTime | DATETIME | The end date and time of a date range in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). |  |  |
| roundedEndDateTime | DATETIME | Work Span Rounded End Date Time.  The start date and time of a date range in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). (Note: If an employee clocks in from one time zone and clocks out from another, the time zone associated with this value will align with the clock-in time zone. This ensures accurate calculation of the total hours worked.) |  |  |
| endPunchId | INT64 | End Punch ID |  |  |
| orderNumber | INT64 | An order number associated with processing work orders that can be configured in a pay rule. |  |  |
| workRule | STRING | Work Rule Name |  |  |
| workRuleId | INT64 | Work Rule ID |  |  |
| primaryWorkRule | STRING | Primary work rule name |  |  |
| primaryWorkRuleId | INT64 | Primary work rule ID |  |  |
| laborEntryName1 | STRING | Labor Category 1 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc1 | STRING | Labor Category 1 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName2 | STRING | Labor Category 2 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc2 | STRING | Labor Category 2 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName3 | STRING | Labor Category 3 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc3 | STRING | Labor Category 3 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName4 | STRING | Labor Category 4 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc4 | STRING | Labor Category 4 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName5 | STRING | Labor Category 5 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc5 | STRING | Labor Category 5 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName6 | STRING | Labor Category 6 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc6 | STRING | Labor Category 6 entry description associated with transaction (applies to labor category transfer) |  |  |
| primaryOrgId | INT64 | Unique identifier of Primary Business Structure location of the employee associated with the transaction - Joins to Business Structure dimensions |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| projectedSwt | BOOLEAN | A Boolean indicator of whether or not shift is projected |  |  |
| scheduledOrgIdSwt | BOOLEAN | A Boolean indicator of whether or not shift has scheduled org |  |  |
| transferOrgIdSwt | BOOLEAN | A Boolean indicator of whether or not shift has org transfer |  |  |
| userEnteredOrgIdSwt | BOOLEAN | A Boolean indicator of whether or not a business structure job for this shift segment was entered by the user. |  |  |
| scheduledWorkRuleSwt | BOOLEAN | A Boolean indicator of whether or not shift has scheduled workrule |  |  |
| transferWorkRuleSwt | BOOLEAN | A Boolean indicator of whether or not shift has workrule transfer |  |  |
| userEnteredWorkRuleSwt | BOOLEAN | A Boolean indicator of whether or not a work rule for this shift segment was entered by the user. |  |  |
| costCenter | STRING | Cost Center name |  |  |
| costCenterId | INT64 | Unique Identifier for a CostCenter joins to costCenter dimension |  |  |
| shiftTotal | INT64 | Total number of hours for a worked span. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| workedShiftSpanUniqueId | INT64 | Worked shift unique identifier |  |  |
| endPunchAssignmentId | INT64 | End punch assignment id |  |  |
| startPunchAssignmentId | INT64 | Start punch assignment id |  |  |
