# vEssShiftSwapStatusChange

**Group:** Detail Dataset → Employee Self Service Detail Views

- Shift Swap Request Status Changes - Tracks changes in status of request
  --   i.e. Draft > Submitted, Submitted > Approved/Rejected

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vEssShiftSwapStatusChange |
| Unique Identifier | All fields |
| Source Pipeline | essShiftSwap (DR) |

## Columns

**Column count:** 13

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | The employee ID of the initiator of an shift swap request, which is an ID that uniquely identifies an employee.This is not a person number. |  |  |
| createDateTime | TIMESTAMP | The date and time of an ESS equest was created in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss) |  |  |
| startDateTime | TIMESTAMP | The start date and time of an ESS request in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). |  |  |
| essShiftSwapId | INT64 | shift swap request id |  |  |
| reqstStatusChgToStatusName | STRING | The localized name of a request status. |  |  |
| partitionDate | DATE | The date part of the for the date selected for this request |  |  |
| endDateTime | TIMESTAMP | The end date and time of an ESS request in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). |  |  |
| reqstStatusChgFromStatusId | INT64 | The ID of a request status. |  |  |
| reqstStatusChgDateTime | TIMESTAMP | The date and time of the change to a request status in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). The date and time are specified according to Greenwich Mean Time (GMT). |  |  |
| reqstStatusChgFullName | STRING | The name of the person who changed the status of a request. |  |  |
| reqstStatusChgFromStatusName | STRING | The localized name of a request status. |  |  |
| reqstStatusChgToStatusId | INT64 | The ID of a request status. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
