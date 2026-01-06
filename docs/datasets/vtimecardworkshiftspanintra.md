# vTimecardWorkShiftSpanIntra

**Group:** Summary Dataset → metricsIntra (vKronosIntraSummary)

-

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vTimecardWorkShiftSpanIntra |
| Unique Identifier | partitionDate,personId,workedShiftId,workedShiftSpanId,time_24H, orderNumber,startPunchId (nullable), endPunchId (nullable) |
| Source Pipeline | summaryIntra (DR), timecard (CDC) |

## Columns

**Column count:** 42

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| laborEntryName1 | STRING | Labor Category 1 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName2 | STRING | Labor Category 2 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName3 | STRING | Labor Category 3 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName4 | STRING | Labor Category 4 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName5 | STRING | Labor Category 5 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName6 | STRING | Labor Category 6 entry name associated with transaction (applies to labor category transfer) |  |  |
| primaryOrgId | INT64 | Unique identifier of Primary Business Structure location of the employee associated with the transaction - Joins to Business Structure dimensions |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| costCenter | STRING | Cost Center name |  |  |
| costCenterId | INT64 | Unique Identifier for a CostCenter joins to costCenter dimension |  |  |
| time_24H | TIME | 24H Time |  |  |
| minutes | INT64 | Total Minutes |  |  |
| hours | FLOAT64 | Total Hours |  |  |
| days | FLOAT64 | Total Days |  |  |
| headCountWholeSpan | INT64 | Whole Span Head Count (if employee works the entire segment the value will be 1 otherwise 0) |  |  |
| headCountRounded | INT64 | Rounded Head Count (if employee works 8 minutes or more the value will be 1 otherwise 0) |  |  |
| headCountAnyWorked | INT64 | Total Headcount  (if employee works any part of the segment the value will be 1 otherwise 0) |  |  |
| startPunchId | INT64 | Start Punch ID |  |  |
| endTimezone | STRING | End timezone where the worked span was entered. Normally, this is the default or home timezone for the employee, but the worked span can include a different timezone as necessary. |  |  |
| endTimezoneId | INT64 | End Punch Time Zone ID |  |  |
| startTimezone | STRING | Start timezone where the worked span was entered. Normally, this is the default or home timezone for the employee, but the worked span can include a different timezone as necessary. |  |  |
| startTimezoneId | INT64 | Start time zone ID |  |  |
| endPunchId | INT64 | End Punch Id |  |  |
| orderNumber | INT64 | Order number |  |  |
| workedShiftId | INT64 | Worked Shift ID |  |  |
| workedShiftSpanId | INT64 | Worked Shift Span ID |  |  |
| primaryWorkRule | STRING | Primary Work Rule Name |  |  |
| primaryWorkRuleId | INT64 | Primary Work Rule ID |  |  |
| workRule | STRING | Work Rule Name |  |  |
| workRuleId | INT64 | Work Rule ID |  |  |
| startDateTime | DATETIME | The start date and time of a date range in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). |  |  |
| endDateTime | DATETIME | Work Shift End Date Time |  |  |
| projectedSwt | BOOLEAN | A Boolean indicator of whether or not shift is projected |  |  |
| scheduledOrgIdSwt | BOOLEAN | A Boolean indicator of whether or not shift has scheduled org |  |  |
| transferOrgIdSwt | BOOLEAN | A Boolean indicator of whether or not shift is org job transfer |  |  |
| userEnteredOrgIdSwt | BOOLEAN | A Boolean indicator of whether or not org is user entered |  |  |
| scheduledWorkRuleSwt | BOOLEAN | A Boolean indicator of whether or not shift has scheduled workrule |  |  |
| transferWorkRuleSwt | BOOLEAN | A Boolean indicator of whether or not shift is a work rule transfer |  |  |
| userEnteredWorkRuleSwt | BOOLEAN | A Boolean indicator of whether or not Work rule is user entered |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
