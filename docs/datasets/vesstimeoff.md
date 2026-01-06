# vEssTimeOff

**Group:** Detail Dataset → Employee Self Service Detail Views

- This resource allows a manager to retrieve time off requests submitted by an employee.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vEssTimeOff |
| Unique Identifier | essTimeOffId,partitionDate,personId |
| Source Pipeline | essTimeOff (DR) |

## Columns

**Column count:** 14

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| essTimeOffId | INT64 | time off request id |  |  |
| partitionDate | DATE | The start date of the request |  |  |
| personId | INT64 | The employee ID of the initiator of  time off request, which is an ID that uniquely identifies an employee.This is not a person number. |  |  |
| personNbr | STRING | The person ID of the initiator of the request as seen in WFD | PII |  |
| createDateTime | TIMESTAMP | The date and time an ESS request was created in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss) |  |  |
| currentStatusId | INT64 | The ID of the current status. |  |  |
| currentStatusName | STRING | The localized name of a request status. |  |  |
| reqstSubTypeId | INT64 | A reference to the request subtype object associated with an availability request |  |  |
| reqstSubTypeName | STRING | name of request subtype i.e.Time Off |  |  |
| reqstSubTypeDesc | STRING | type of request i.e.self scheduling, time-off, cover |  |  |
| reqstTypeId | INT64 | The ID of a request type. |  |  |
| reqstTypeName | STRING | name of request subtype i.e.Time Off |  |  |
| reqstTypeDesc | STRING | type of request i.e.self scheduling, time-off, cover |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
