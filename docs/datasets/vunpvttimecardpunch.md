# vUnpvtTimecardPunch

**Group:** Summary Dataset → metricsIntra (vKronosIntraSummary)

-

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vUnpvtTimecardPunch |
| Unique Identifier | partitionDate,personId,orgId |
| Source Pipeline |  |

## Columns

**Column count:** 6

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| inPunchCnt | INT64 | In Punch Count |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| outPunchCnt | INT64 | Out Punch Count |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
