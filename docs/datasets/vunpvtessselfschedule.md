# vUnpvtEssSelfSchedule

**Group:** Summary Dataset → metricsIntra (vKronosIntraSummary)

- Self Schedule Request Summary

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vUnpvtEssSelfSchedule |
| Unique Identifier | partitionDate,orgId,personId |
| Source Pipeline |  |

## Columns

**Column count:** 5

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | The date part of the for the date selected for this request |  |  |
| personId | INT64 | The employee ID of the initiator of the request, which is an ID that uniquely identifies an employee. This is not a person number. |  |  |
| primaryOrgId | INT64 | Employee primary organization id |  |  |
| completedCnt | INT64 | Number of request(s) that have been completed |  |  |
| updateDtm | DATETIME | pipeline update date time |  |  |
