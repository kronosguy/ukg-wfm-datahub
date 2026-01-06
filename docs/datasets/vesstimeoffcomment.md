# vEssTimeOffComment

**Group:** Detail Dataset → Employee Self Service Detail Views

- Time Off Comments

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vEssTimeOffComment |
| Unique Identifier | essTimeOffId,partitionDate,personId,commentNoteId,commentId,noteText (nullable) |
| Source Pipeline | essTimeOff (DR) |

## Columns

**Column count:** 11

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| essTimeOffId | INT64 | time off request id |  |  |
| partitionDate | DATE | The start date of the request |  |  |
| personId | INT64 | The employee ID of the initiator of  time off request, which is an ID that uniquely identifies an employee.This is not a person number. |  |  |
| commentNoteId | INT64 | The ID for the comment and attached notes. |  |  |
| activeSwt | BOOLEAN | Whether the comment is active or not. |  |  |
| commentId | INT64 | The ID for the comment. |  |  |
| commentName | STRING | The name of the comment. |  |  |
| dataSourceDisplayName | STRING | The name of the person who entered the note. |  |  |
| noteText | STRING | The text of the note. | PII |  |
| noteTimeStamp | STRING | date employee submitted the request |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
