# vEssShiftCover

**Group:** Detail Dataset → Employee Self Service Detail Views

- This operation returns one or more shift cover requests matching specified search criteria corresponding to a set of cover request IDs, managers, or current state

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vEssShiftCover |
| Unique Identifier | essShiftCoverId,partitionDate,personId,coverShiftEntityVer,currentStatusId |
| Source Pipeline | essShiftCover (DR) |

## Columns

**Column count:** 20

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| essShiftCoverId | INT64 | shift cover request id |  |  |
| partitionDate | DATE | The date part of the for the date selected for this request |  |  |
| personId | INT64 | The employee ID of the initiator of an shift coverage request, which is an ID that uniquely identifies an employee.This is not a person number. |  |  |
| personNbr | STRING | The person ID of the initiator of the request as seen in WFD | PII |  |
| createDateTime | TIMESTAMP | The date and time an ESS request was created in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss) |  |  |
| startDateTime | TIMESTAMP | The start date and time of an ESS request in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). |  |  |
| endDateTime | TIMESTAMP | The end date and time of an ESS request in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). |  |  |
| coverShiftEntityId | INT64 | The ID of the shift to cover. |  |  |
| coverShiftEntityVer | INT64 | The entity version of the shift to cover. |  |  |
| currentStatusId | INT64 | The ID of the current status. |  |  |
| currentStatusName | STRING | The name of a current status of a cover request |  |  |
| recipientId | INT64 | The employee ID of the recipient of a cover request, which is an ID that uniquely identifies an employee.This is not a person number. |  |  |
| recipientPersonNbr | STRING | The person ID for the recipient of a cover request | PII |  |
| reqstSubTypeId | INT64 | The ID of a request subtype. |  |  |
| reqstSubTypeName | STRING | The name of request subtype |  |  |
| reqstSubTypeDesc | STRING | The description of a request subtype. |  |  |
| reqstTypeId | INT64 | The ID of a request type. |  |  |
| reqstTypeName | STRING | The name of a request type |  |  |
| reqstTypeDesc | STRING | The description of a request type. |  |  |
| updateDtm | DATETIME | pipeline update date time |  |  |
