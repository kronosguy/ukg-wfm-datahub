# vEssAvailability

**Group:** Detail Dataset → Employee Self Service Detail Views

- This resource allows you to retrieve availability requests, which allow managers to handle requests made by employees to temporarily override the times when they are available to work. Note: This does not include Availability Pattern Requests

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vEssAvailability |
| Unique Identifier | essAvailabilityId,partitionDate,personId |
| Source Pipeline | essAvailability (DR) |

## Columns

**Column count:** 23

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| essAvailabilityId | INT64 | The ID of an availability request. |  |  |
| partitionDate | DATE | The date part of the for the date selected for this request |  |  |
| personId | INT64 | The employee ID of the initiator of an availability request, which is an ID that uniquely identifies an employee. This is not a person number. |  |  |
| personNbr | STRING | The person ID of the initiator of the request as seen in WFD | PII |  |
| createDateTime | TIMESTAMP | The date and time an availability request was created in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). |  |  |
| currentStatusId | INT64 | The ID of the current status. |  |  |
| currentStatusName | STRING | The localized name of a request status. |  |  |
| reqstAvailDurMins | INT64 | The duration of requested availability in minutes expressed as an INT64. |  |  |
| initAvailDurMins | INT64 | The duration of initial availability in minutes expressed as an INT64. |  |  |
| deltaAvailDurMins | INT64 | The availability delta in minutes expressed as an INT64. |  |  |
| reqstSubTypeId | INT64 | A reference to the request subtype object associated with an availability request |  |  |
| reqstSubTypeName | STRING | name of request subtype i.e.Time Off |  |  |
| reqstSubTypeDesc | STRING | type of request i.e.self scheduling, time-off, cover |  |  |
| reqstTypeId | INT64 | The ID of a request type. |  |  |
| reqstTypeName | STRING | name of request subtype i.e.Time Off |  |  |
| reqstTypeDesc | STRING | type of request i.e.self scheduling, time-off, cover |  |  |
| lastReqstStatusChgDateTime | TIMESTAMP | The date and time of the change to a request status in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). The date and time are specified according to Greenwich Mean Time (GMT). |  |  |
| lastReqstStatusChgFullName | STRING | The name of the person who changed the status of a request. |  |  |
| lastReqstStatusChgFromStatusId | INT64 | The ID of a request status. |  |  |
| lastReqstStatusChgFromStatusName | STRING | The localized name of a request status. |  |  |
| lastReqstStatusChgToStatusId | INT64 | The ID of a request status. |  |  |
| lastReqstStatusChgToStatusName | STRING | The localized name of a request status. |  |  |
| updateDtm | DATETIME | pipeline update date time |  |  |
