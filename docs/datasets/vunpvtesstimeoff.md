# vUnpvtEssTimeOff

**Group:** Summary Dataset → metricsIntra (vKronosIntraSummary)

- Time Off Request Summary

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vUnpvtEssTimeOff |
| Unique Identifier | partitionDate,orgId,personId |
| Source Pipeline |  |

## Columns

**Column count:** 12

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | The date part of the for the date selected for this request |  |  |
| personId | INT64 | The employee ID of the initiator of the request, which is an ID that uniquely identifies an employee. This is not a person number. |  |  |
| primaryOrgId | INT64 | Employee primary organization id |  |  |
| submittedCnt | INT64 | Number of submitted request(s) where no action has been taken by a reviewer |  |  |
| pendingCnt | INT64 | Number of request(s) with a pending status this is a a request that has multiple reviewers and has been approved by one or more of the reviewers |  |  |
| cancelledCnt | INT64 | Number of request(s) that have been cancelled |  |  |
| approvedCnt | INT64 | Number of request(s) that have been approved |  |  |
| autoApprovedCnt | INT64 | Number of request(s) that have an automatic approval |  |  |
| refusedCnt | INT64 | Number of request(s) that have been refused by reviewer |  |  |
| completedCnt | INT64 | Number of request(s) that have been approved or refused by reviewer |  |  |
| processDurationHrs | FLOAT64 | Total duration of process segment |  |  |
| updateDtm | DATETIME | pipeline update date time |  |  |
