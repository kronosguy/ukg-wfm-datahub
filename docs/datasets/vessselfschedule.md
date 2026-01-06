# vEssSelfSchedule

**Group:** Detail Dataset → Employee Self Service Detail Views

- This operation returns one or more self-schedule requests by request IDs, employee IDs, or current state.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vEssSelfSchedule |
| Unique Identifier | essSelfScheduleId,partitionDate,personId |
| Source Pipeline | essSelfSchedule (DR) |

## Columns

**Column count:** 14

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| essSelfScheduleId | INT64 | self schedule request id |  |  |
| partitionDate | DATE | The date part of the for the date selected for this request |  |  |
| personId | INT64 | The employee ID of the initiator of an shift coverage request, which is an ID that uniquely identifies an employee.This is not a person number. |  |  |
| personNbr | STRING | The person ID of the initiator of the request as seen in WFD | PII |  |
| createDateTime | TIMESTAMP | The date and time an ESS request was created in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). |  |  |
| reqstSubTypeId | INT64 | The ID of a request subtype. |  |  |
| reqstSubTypeName | STRING | The name of a request subtype. |  |  |
| reqstSubTypeDesc | STRING | The description of a request subtype. |  |  |
| reqstTypeId | INT64 | The ID of a request type. |  |  |
| reqstTypeName | STRING | The name of a request type. |  |  |
| reqstTypeDesc | STRING | The description of a request type |  |  |
| currentStatusId | INT64 | The ID of the current status. |  |  |
| currentStatusName | STRING | The localized name of a request status. |  |  |
| updateDtm | DATETIME | pipeline update date time |  |  |
