# vScheduleLeaveEdit

**Group:** Detail Dataset → Schedule Detail Views

- Leave Module of WFD.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleLeaveEdit |
| Unique Identifier | leaveEditId,partitionDate,personId |
| Source Pipeline | schedule (CDC) |

## Columns

**Column count:** 52

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| leaveEditId | INT64 | The ID of this leave edit. |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| startDate | DATE | Shift Start Date |  |  |
| startTime | TIME | Shift Start Time |  |  |
| endDate | DATE | Schedule end date |  |  |
| endTime | TIME | Schdeule end time |  |  |
| durationInTime | INT64 | Schdule leave duration |  |  |
| leaveCaseCode | STRING | Leave case code |  |  |
| leaveCaseName | STRING | Leave case name |  |  |
| leaveCaseId | INT64 | Leave case ID |  |  |
| leaveCaseOfContinuousFrequency | BOOLEAN | Frequency type of a leave case for which the leave edit is created. |  |  |
| leaveCaseStatus | INT64 | The status of a leave case for which the leave edit is created. |  |  |
| trackingSegmentId | INT64 | Tracking segment id |  |  |
| trackingSegmentOverridden | BOOLEAN | A Boolean indicator of whether or not there is a tracking segment override |  |  |
| trackingSegmentSymbolicValueId | INT64 | A reference to the symbolic value used to create this tracking segment. |  |  |
| trackingSegmentDurationInTime | INT64 | The duration in seconds of this tracking segment. |  |  |
| transferUserEnteredLaborEntryName6 | STRING | Labor Category 6 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| transferUserEnteredCostCenterSwt | BOOLEAN | A Boolean indicator of whether or not a cost center is user-entered. |  |  |
| transferUserEnteredLaborEntryName1 | STRING | Labor Category 1 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| transferUserEnteredLaborEntryName2 | STRING | Labor Category 2 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| transferUserEnteredLaborEntryName3 | STRING | Labor Category 3 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| transferUserEnteredLaborEntryName4 | STRING | Labor Category 4 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| transferUserEnteredLaborEntryName5 | STRING | Labor Category 5 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| transferPrimaryOrgId | INT64 | Unique identifier of Primary Business Structure location of the employee associated with the transaction - Joins to Business Structure dimensions |  |  |
| transferCostCenterId | INT64 | Unique Identifier for a CostCenter joins to costCenter dimension |  |  |
| transferOrgId | INT64 | Business structure job transfer org ID |  |  |
| transferUserEnteredOrgJobSwt | BOOLEAN | A Boolean indicator of whether or not an org job is user-entered. |  |  |
| transferPrimaryLaborEntryName6 | STRING | Labor Category 6 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| transferprimaryCostCenterId | INT64 | A Boolean indicator of whether or not a cost center is transferred. |  |  |
| transferPrimaryLaborEntryName1 | STRING | Labor Category 1 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| transferPrimaryLaborEntryName2 | STRING | Labor Category 2 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| transferPrimaryLaborEntryName3 | STRING | Labor Category 3 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| transferPrimaryLaborEntryName4 | STRING | Labor Category 4 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| transferPrimaryLaborEntryName5 | STRING | Labor Category 5 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| transferLaborEntryName1 | STRING | Labor Category 1 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| transferLaborEntryName2 | STRING | Labor Category 2 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| transferLaborEntryName3 | STRING | Labor Category 3 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| transferLaborEntryName4 | STRING | Labor Category 4 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| transferLaborEntryName5 | STRING | Labor Category 5 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| transferLaborEntryName6 | STRING | Labor Category 6 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| paidSegmentOverriddenSwt | BOOLEAN | A Boolean indicator of whether or not there is a paid segment override |  |  |
| paidSegmentId | INT64 | The ID of the leave segment |  |  |
| paidSegmentSymbolicValueId | INT64 | A reference to the symbolic value used to create this leave edit segment. |  |  |
| trackingSegmentSymbolicValueName | STRING | Tracking segment symbolic value name |  |  |
| paidSegmentDurationInTime | INT64 | The duration in seconds of this override leave edit segment. |  |  |
| deletedSwt | BOOLEAN | The Boolean flag indicating the day lock deleted status (read-only). |  |  |
| generatedSwt | BOOLEAN | The Boolean indicating that the system generated leave edit |  |  |
| postedSwt | BOOLEAN | A Boolean indicator of whether or not the employee has been notified of the posted leave edit. |  |  |
| lockedSwt | BOOLEAN | The leave edit locked status. |  |  |
| version | INT64 | Unix timestamp that logs the date/time of change |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
