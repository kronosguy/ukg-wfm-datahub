# vTimecardHolidayCredit

**Group:** Detail Dataset → Timecard Detail Views

- Holiday Credits applied to a timecard.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vTimecardHolidayCredit |
| Unique Identifier | holidayCreditId |
| Source Pipeline | timecard (CDC) |

## Columns

**Column count:** 33

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| holidayCreditId | INT64 | Holiday Credit ID |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| durationInHours | FLOAT64 | The duration (in hours) for the Holiday Credit |  |  |
| editableSwt | BOOLEAN | A Boolean indicator of whether or not a holiday credit is editable. |  |  |
| durationInDays | FLOAT64 | The duration (in days) for the Holiday Credit |  |  |
| holidayDisplayName | STRING | Holiday Name |  |  |
| startTimeZoneId | STRING | Start time zone ID |  |  |
| startDateTime | DATETIME | The earliest start date associated with a timecard in ISO_LOCAL_DATE format (YYYY-MM-DD). |  |  |
| endTimeZoneId | STRING | End time zone ID |  |  |
| endDateTime | DATETIME | The end date and time of a date range in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). |  |  |
| scheduleAmountType | STRING | An enumeration of the schedule amount. |  |  |
| scheduleAmountTypeId | INT64 | Schedule amount type ID |  |  |
| amountType | STRING | Indicates if the pay code unit type of the amount paid was hours, money, or days |  |  |
| moneyAmount | FLOAT64 | Holiday credit money amount |  |  |
| systemGeneratedSwt | BOOLEAN | A Boolean indicator of whether or not a holiday credtit is system-generated. |  |  |
| orgId | STRING | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| costCenterId | INT64 | Unique Identifier for a CostCenter joins to costCenter dimension |  |  |
| laborEntryName1 | STRING | Labor Category 1 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc1 | STRING | Labor Category 2 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryName2 | STRING | Labor Category 3 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc2 | STRING | Labor Category 4 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryName3 | STRING | Labor Category 5 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc3 | STRING | Labor Category 6 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryName4 | STRING | Labor Category 1 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc4 | STRING | Labor Category 2 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName5 | STRING | Labor Category 3 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc5 | STRING | Labor Category 4 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName6 | STRING | Labor Category 5 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc6 | STRING | Labor Category 6 entry description associated with transaction (applies to labor category transfer) |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| costCenter | STRING | Cost Center name |  |  |
| assignmentId | INT64 |  |  |  |
