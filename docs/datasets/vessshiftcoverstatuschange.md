# vEssShiftCoverStatusChange

**Group:** Detail Dataset → Employee Self Service Detail Views

- Shift Cover Request Status Change - Tracks changes in status of request i.e.Draft > Submitted, Submitted > Approved/Rejected

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vEssShiftCoverStatusChange |
| Unique Identifier | All fields |
| Source Pipeline | essShiftCover (DR) |

## Columns

**Column count:** 13

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| essShiftCoverId | INT64 | shift cover request id |  |  |
| partitionDate | DATE | The date part of the for the date selected for this request |  |  |
| personId | INT64 | The employee ID of the initiator of an shift coverage request, which is an ID that uniquely identifies an employee.This is not a person number. |  |  |
| createDateTime | TIMESTAMP | The date and time an ESS request was created in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss) |  |  |
| startDateTime | TIMESTAMP | The start date and time of an ESS request in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). |  |  |
| endDateTime | TIMESTAMP | The end date and time of an ESS request in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). |  |  |
| reqstStatusChgDateTime | TIMESTAMP | The date and time of the change to a request status in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). The date and time are specified according to Greenwich Mean Time (GMT). |  |  |
| reqstStatusChgFullName | STRING | The name of the person who changed the status of a request. |  |  |
| reqstStatusChgFromStatusId | INT64 | The ID of a request status. |  |  |
| reqstStatusChgFromStatusName | STRING | The localized name of a request status. |  |  |
| reqstStatusChgToStatusId | INT64 | The ID of a request status. |  |  |
| reqstStatusChgToStatusName | STRING | The localized name of a request status. |  |  |
| updateDtm | DATETIME | pipeline update date time |  |  |
