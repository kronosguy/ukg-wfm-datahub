# vEssSelfScheduleRequestPeriod

**Group:** Detail Dataset → Employee Self Service Detail Views

- Self Schedule Request schedule periods

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vEssSelfScheduleRequestPeriod |
| Unique Identifier | All fields |
| Source Pipeline | essSelfSchedule (DR) |

## Columns

**Column count:** 9

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| essSelfScheduleId | INT64 | The ID of an ESS request. |  |  |
| partitionDate | DATE | The date part of the for the date selected for this request |  |  |
| personId | INT64 | The employee ID of the initiator of an ESS request, which is an ID that uniquely identifies an employee. This is not a person number. |  |  |
| reqstOpenShiftEndDate | TIMESTAMP | The schedule item ID of the open shift pertaining to the ESS request item |  |  |
| reqstOpenShiftId | INT64 | The start date time of the open shift pertaining to the ESS request item |  |  |
| reqstOpenShiftSchdItemId | INT64 | The ID of an ESS request item |  |  |
| reqstOpenShiftSchdItemVer | INT64 | The end date time of the open shift pertaining to the ESS request item |  |  |
| reqstOpenShiftStartDate | TIMESTAMP | The schedule item version of the open shift pertaining to the ESS request item |  |  |
| updateDtm | DATETIME | pipeline update date time |  |  |
