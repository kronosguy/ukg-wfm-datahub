# vEssSelfScheduleComment

**Group:** Detail Dataset → Employee Self Service Detail Views

- Self Schedule Request Comments

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vEssSelfScheduleComment |
| Unique Identifier | essSelfScheduleId,partitionDate,personId,commentNoteId,commentId |
| Source Pipeline | essSelfSchedule (DR) |

## Columns

**Column count:** 11

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| essSelScheduleId | INT64 | self schedule request id |  |  |
| partitionDate | DATE | The date part of the for the date selected for this request |  |  |
| personId | INT64 | The employee ID of the initiator of an self schedule request, which is an ID that uniquely identifies an employee.This is not a person number. |  |  |
| commentNoteId | INT64 | The ID for the comment and attached notes. |  |  |
| activeSwt | BOOLEAN | Whether the comment is active or not. |  |  |
| commentId | INT64 | The ID for the comment. |  |  |
| commentName | STRING | The name of the comment. |  |  |
| dataSourceDisplayName | STRING | The name of the person who entered the note. |  |  |
| noteText | STRING | The text of the note. | PII |  |
| noteTimeStamp | TIMESTAMP | date employee submitted the request |  |  |
| updateDtm | DATETIME | pipeline update date time |  |  |
