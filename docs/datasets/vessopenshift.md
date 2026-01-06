# vEssOpenShift

**Group:** Detail Dataset → Employee Self Service Detail Views

- This resource allows a manager to retrieve open shift requests. Employees can request to select their own schedule from the times that are available when the request period is open.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vEssOpenShift |
| Unique Identifier | essOpenShiftId,partitionDate,personId |
| Source Pipeline | essOpenShift (DR) |

## Columns

**Column count:** 16

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| essOpenShiftId | INT64 | open shift cover request id |  |  |
| partitionDate | DATE | The date part of the for the date selected for this request |  |  |
| personId | INT64 | The employee ID of the initiator of an open shift coverage request, which is an ID that uniquely identifies an employee. This is not a person number. |  |  |
| personNbr | STRING | The person ID of the initiator of the request as seen in WFD | PII |  |
| createDateTime | TIMESTAMP | The date and time of an ESS equest was created in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss) |  |  |
| startDateTime | TIMESTAMP | The start date and time of an ESS request in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). |  |  |
| endDateTime | TIMESTAMP | The end date and time of an ESS request in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). |  |  |
| reqstSubTypeId | INT64 | The ID of a request subtype. |  |  |
| reqstSubTypeName | STRING | The name of request subtype |  |  |
| reqstSubTypeDesc | STRING | type of request i.e. self scheduling, time-off, cover |  |  |
| reqstTypeId | INT64 | The ID of a request type. |  |  |
| reqstTypeName | STRING | The name of a request type i.e. Time Off |  |  |
| reqstTypeDesc | STRING | type of request i.e. self scheduling, time-off, cover |  |  |
| currentStatusId | INT64 | The ID of the current status. |  |  |
| currentStatusName | STRING | The localized name of a request status. |  |  |
| updateDtm | DATETIME | pipeline update date time |  |  |
