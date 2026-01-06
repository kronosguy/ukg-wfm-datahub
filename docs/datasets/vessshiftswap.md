# vEssShiftSwap

**Group:** Detail Dataset → Employee Self Service Detail Views

- This resource allows a manager to retrieve shift swap request

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vEssShiftSwap |
| Unique Identifier | essShiftSwapId,partitionDate,personId,currentStatusId |
| Source Pipeline | essShiftSwap (DR) |

## Columns

**Column count:** 26

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| essShiftSwapId | INT64 | shift swap request id |  |  |
| partitionDate | DATE | The date part of the for the date selected for this request |  |  |
| personId | INT64 | The employee ID of the initiator of an shift swap request, which is an ID that uniquely identifies an employee.This is not a person number. |  |  |
| personNbr | STRING | The person ID of the initiator of the request as seen in WFD | PII |  |
| createDateTime | TIMESTAMP | The date and time an ESS request was created in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss) |  |  |
| startDateTime | TIMESTAMP | The start date and time of an ESS request in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). |  |  |
| endDateTime | TIMESTAMP | The end date and time of an ESS request in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). |  |  |
| currentStatusId | INT64 | The ID of the current status. |  |  |
| currentStatusName | STRING | The localized name of a request status. |  |  |
| reqstSubTypeId | INT64 | A reference to the request subtype object associated with an availability request |  |  |
| reqstSubTypeName | STRING | name of request subtype i.e.Time Off |  |  |
| reqstSubTypeDesc | STRING | type of request i.e.self scheduling, time-off, cover |  |  |
| reqstTypeId | INT64 | The ID of a request type. |  |  |
| reqstTypeName | STRING | name of request subtype i.e.Time Off |  |  |
| reqstTypeDesc | STRING | type of request i.e.self scheduling, time-off, cover |  |  |
| shiftOfferedPersonId | INT64 | The employee ID of the initiator of an shift swap request |  |  |
| shiftOfferedFullName | STRING | The employee name of the initiator of an shift swap request | PII |  |
| shiftOfferedShiftId | INT64 | The Shift ID of the shift being offered |  |  |
| shiftOfferedShiftName | STRING | The Shift Name of the shift being offered |  |  |
| shiftOfferedShiftVersion | INT64 | The Shift Version of the shift being offered |  |  |
| shiftReqstdPersonId | INT64 | The employee ID of the recipient of an shift swap request |  |  |
| shiftReqstdFullName | STRING | The employee name of the recipient of an shift swap request | PII |  |
| shiftReqstdShiftId | INT64 | The Shift ID of the shift being requested |  |  |
| shiftReqstdShiftName | STRING | The Shift Name of the shift being requested |  |  |
| shiftReqstdShiftVersion | INT64 | The Shift Version of the shift being requested |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
