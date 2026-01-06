# vEssTimeOffStatusChange

**Group:** Detail Dataset → Employee Self Service Detail Views

- Time Off Request Status Changes - Tracks changes in status of request 
 -- i.e. Draft > Submitted, Submitted > Approved/Rejected

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vEssTimeOffStatusChange |
| Unique Identifier | All fields |
| Source Pipeline | essTimeOff (DR) |

## Columns

**Column count:** 11

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| essTimeOffId | INT64 | time off request id |  |  |
| partitionDate | DATE | The start date of the request |  |  |
| personId | INT64 | The employee ID of the initiator of  time off request, which is an ID that uniquely identifies an employee.This is not a person number. |  |  |
| createDateTime | TIMESTAMP | The date and time an ESS request was created in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss) |  |  |
| reqstStatusChgDateTime | TIMESTAMP | The date and time of the change to a request status in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). The date and time are specified according to Greenwich Mean Time (GMT). |  |  |
| reqstStatusChgFullName | STRING | The name of the person who changed the status of a request. | PII |  |
| reqstStatusChgFromStatusId | INT64 | The ID of a request status. |  |  |
| reqstStatusChgFromStatusName | STRING | The localized name of a request status. |  |  |
| reqstStatusChgToStatusId | INT64 | The ID of a request status. |  |  |
| reqstStatusChgToStatusName | STRING | The localized name of a request status. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
