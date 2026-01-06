# vScheduleOpenShiftSegment

**Group:** Detail Dataset → Schedule Detail Views

- Open Shift Segments (Child of scheduleOpenShift) Represents scheduled open shift segments within a shift. Excludes break segments

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleOpenShiftSegment |
| Unique Identifier | uniqueId |
| Source Pipeline | scheduleOpenShift (CDC) |

## Columns

**Column count:** 54

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| openShiftId | INT64 | Schedule open shift ID |  |  |
| openShiftSegmentId | INT64 | Schedule open shift segment ID |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | **  Note this value will always be null because openShift is not tied to person ** |  |  |
| startDateTime | DATETIME | Shift start date time |  |  |
| endDateTime | DATETIME | Shift end date time |  |  |
| primaryWorkRule | STRING | The name from the primary work rule |  |  |
| primaryWorkRuleId | INT64 | The ID from the primary work rule |  |  |
| primaryOrgId | INT64 | Unique identifier of Primary Business Structure location of the employee associated with the transaction - Joins to Business Structure dimensions |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| workRule | STRING | Work Rule Name |  |  |
| workRuleId | INT64 | Work Rule ID |  |  |
| openShiftSegmentType | STRING | Schedule open shift segment type |  |  |
| openShiftSegmentTypeId | INT64 | Schedule open shift segment type ID |  |  |
| segmentType | STRING | The shift segment type |  |  |
| segmentTypeId | INT64 | The shift segment type ID |  |  |
| laborEntryName1 | STRING | Labor Category 1 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryName2 | STRING | Labor Category 2 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryName3 | STRING | Labor Category 3 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryName4 | STRING | Labor Category 4 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryName5 | STRING | Labor Category 5 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryName6 | STRING | Labor Category 6 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc1 | STRING | Labor Category 1 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc2 | STRING | Labor Category 2 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc3 | STRING | Labor Category 3 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc4 | STRING | Labor Category 4 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc5 | STRING | Labor Category 5 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc6 | STRING | Labor Category 6 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryName1 | STRING | Labor Category 1 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryName2 | STRING | Labor Category 2 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryName3 | STRING | Labor Category 3 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryName4 | STRING | Labor Category 4 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryName5 | STRING | Labor Category 5 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryName6 | STRING | Labor Category 6 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryDesc1 | STRING | Labor Category 1 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryDesc2 | STRING | Labor Category 2 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryDesc3 | STRING | Labor Category 3 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryDesc4 | STRING | Labor Category 4 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryDesc5 | STRING | Labor Category 5 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryDesc6 | STRING | Labor Category 6 entry description associated with transaction (applies to labor category transfer) |  |  |
| primaryCostCenter | STRING | Primary cost center for employee associated with transaction |  |  |
| primaryCostCenterId | INT64 | Primary cost center ID - joins to cost center dimension |  |  |
| costCenter | STRING | Cost Center name |  |  |
| costCenterId | INT64 | Unique Identifier for a CostCenter joins to costCenter dimension |  |  |
| transferOrgIdSwt | BOOLEAN | A Boolean indicator of whether or not the org is a transfer. |  |  |
| userEnteredCostCenterSwt | BOOLEAN | A Boolean indicator of whether or not a cost center was entered by the user for this shift segment. |  |  |
| transferLaborCategoriesSwt | BOOLEAN | A Boolean indicator of whether or not the labor category is a transfer. |  |  |
| transferWorkruleSwt | BOOLEAN | A Boolean indicator of whether or not the work rule is a transfer. |  |  |
| userEnteredWorkruleSwt | BOOLEAN | A Boolean indicator of whether or not a work rule for this shift segment was entered by the user. |  |  |
| transferCostCenterSwt | BOOLEAN | A Boolean indicator of whether or not the cost center is a transfer. |  |  |
| userEnteredOrgSwt | BOOLEAN | A Boolean indicator of whether or not a business structure job was entered by the user. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| orgIds | INT64 (NESTED) | Nested list of orgIds |  |  |
| uniqueId | STRING | Unique Identifier |  |  |
