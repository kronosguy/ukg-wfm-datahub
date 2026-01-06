# vTimecardPunchComment

**Group:** Detail Dataset → Timecard Detail Views

-

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vTimecardPunchComment |
| Unique Identifier | punchId,commentId,commentNoteId,timestamp (nullable) |
| Source Pipeline | timecard (CDC) |

## Columns

**Column count:** 13

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| punchId | INT64 | Timecar Punch ID |  |  |
| partitionDate | DATE | Represents Date Part of punch datetime for the transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| commentNoteId | INT64 | The ID for the note. |  |  |
| timestamp | DATETIME | The date and time when the note was created or modified; in ISO_LOCAL_DATE format (YYYY-MM-DD). |  |  |
| notesText | STRING | The text of the note. | PII |  |
| dataSourceId | INT64 | The ID of the person who entered the note. |  |  |
| dataSourceDisplayName | STRING | The name of the person who entered the note. |  |  |
| comment | STRING | The name of the comment and attached notes. |  |  |
| commentId | INT64 | The ID for the comment and attached notes. |  |  |
| commentCategory | STRING | Comment category name |  |  |
| commentCategoryId | INT64 | Comment category ID |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
