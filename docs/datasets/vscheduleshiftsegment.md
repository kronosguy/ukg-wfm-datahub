# vScheduleShiftSegment

**Group:** Detail Dataset → Schedule Detail Views

- Scheduled Shift Segments (Child of scheduleShift)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleShiftSegment |
| Unique Identifier | shiftId,shiftSegmentId,partitionDate,personId |
| Source Pipeline | schedule (CDC) |

## Columns

**Column count:** 53

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| shiftId | INT64 | Shift ID |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| shiftSegmentId | INT64 | Shift Segment ID |  |  |
| startDateTime | DATETIME | Shift Start Date Time |  |  |
| endDateTime | DATETIME | Schedule End Date Time |  |  |
| primaryWorkRule | STRING | Primary work rule name |  |  |
| primaryWorkRuleId | INT64 | Primary work rule id |  |  |
| primaryOrgId | INT64 | Unique identifier of Primary Business Structure location of the employee associated with the transaction - Joins to Business Structure dimensions |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| workRule | STRING | Work rule name |  |  |
| workRuleId | INT64 | Work rule ID |  |  |
| shiftSegmentType | STRING | Shift Segment Type |  |  |
| shiftSegmentTypeId | INT64 | Shift Segment Type ID |  |  |
| segmentType | STRING | Segment Type Name |  |  |
| segmentTypeId | INT64 | Segment Type ID |  |  |
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
| primaryCostCenter | STRING | Primary cost center for employee associated with transaction |  |  |
| primaryCostCenterId | INT64 | Primary cost center ID - joins to cost center dimension |  |  |
| costCenter | STRING | Cost Center name |  |  |
| costCenterId | INT64 | Unique Identifier for a CostCenter joins to costCenter dimension |  |  |
| transferOrgIdSwt | BOOLEAN | A Boolean indicator of whether or not there is a business structure job transfer |  |  |
| transferOrgString | STRING | An ordered, semi-colon separated list of Labor Category Entries and Cost Center. |  |  |
| userEnteredCostCenterSwt | BOOLEAN | A Boolean indicator of whether or not the cost center was entered by the user. |  |  |
| transferLaborCategoriesSwt | BOOLEAN | A Boolean indicator of whether or not there is a labor categry transfer |  |  |
| transferWorkruleSwt | BOOLEAN | A Boolean indicator of whether or not there is work rule transfer |  |  |
| userEnteredWorkruleSwt | BOOLEAN | A Boolean indicator of whether or not a work rule for this shift segment was entered by the user. |  |  |
| transferCostCenterSwt | BOOLEAN | A Boolean indicator of whether or not there is a transfer cost center for this shift segment. |  |  |
| userEnteredOrgSwt | BOOLEAN | A Boolean indicator of whether or not a org for this shift segment was entered by the user. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
