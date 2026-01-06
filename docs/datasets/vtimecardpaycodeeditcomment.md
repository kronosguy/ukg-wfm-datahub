# vTimecardPayCodeEditComment

**Group:** Detail Dataset → Timecard Detail Views

-

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vTimecardPayCodeEditComment |
| Unique Identifier | payCodeEditId,commentId, commentNoteId, commentCategory, commentCategoryId, timestamp (nullable) |
| Source Pipeline | timecard (CDC) |

## Columns

**Column count:** 13

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| payCodeEditId | INT64 | Pay code edit ID |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | The personId for the person who entered comment |  |  |
| commentNoteId | INT64 | The ID for the note. |  |  |
| timestamp | DATETIME | The data/time the comment was created or updated |  |  |
| notesText | STRING | The text entered in the note | PII |  |
| dataSourceId | INT64 | The ID of the person who entered the note. |  |  |
| dataSourceDisplayName | STRING | The name of the person who entered the note. |  |  |
| comment | STRING | The name of the comment and attached notes. |  |  |
| commentId | INT64 | The ID for the comment and attached notes. |  |  |
| commentCategory | STRING | Comment category name |  |  |
| commentCategoryId | INT64 | Comment category ID |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
