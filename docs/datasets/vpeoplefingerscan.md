# vPeopleFingerScan

**Group:** Detail Dataset → People Detail Views

- ** Do Not Use this value is not available or inaccurate ** the API doesn't return this information due to PII

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleFingerScan |
| Unique Identifier |  |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 12

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| thresholdLabel | STRING | Threshold label |  |  |
| threshold | STRING | Threshold |  |  |
| priority | STRING | Priority |  |  |
| finger | STRING | Finger | PII | BLANK |
| enrollmentLocation | STRING | Enrollment location |  |  |
| enrollmentDate | DATE | Enrollment date |  |  |
| forIdentificationSwt | BOOLEAN | For identifification switch |  |  |
| contentScore | INT64 | Content score |  |  |
| qualityScore | INT64 | Quality score |  |  |
| biopodType | STRING | Bio pod type |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
