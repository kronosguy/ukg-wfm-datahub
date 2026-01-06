# vValTimecardTotal

**Group:** Detail Dataset → Data Detail Validation

Validation Timecard Total Data sourced from IA

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vValTimecardTotal |
| Unique Identifier | All fields |
| Source Pipeline | valTimecardTotal (DR) |

## Columns

**Column count:** 18

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| paycodeId | INT64 | Unique identifier of a pay code. Joins to pay code dimension |  |  |
| orgjobId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| laborcategoryId | INT64 | Labor category Id |  |  |
| hoursAmount | FLOAT | Hours amount for totalized transaction |  |  |
| wagesAmount | FLOAT | Wage amount for totalized transaction |  |  |
| daysAmount | FLOAT | Days amount for totalized transaction |  |  |
| applyDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| jobTransferSwt | INT64 | Indicates if transaction has a business structure transfer |  |  |
| costCenter | STRING | Cost Center name (applies to cost cent transfer) |  |  |
| laborEntryName1 | STRING | Labor Category 1 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName2 | STRING | Labor Category 2 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName3 | STRING | Labor Category 3 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName4 | STRING | Labor Category 4 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName5 | STRING | Labor Category 5 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName6 | STRING | Labor Category 6 entry name associated with transaction (applies to labor category transfer) |  |  |
| updateDtm | DATETIME | Represents apply date of transaction - use to join to date dimension |  |  |
