# vZz_tmp_schedulePostMetric

**Group:** Detail Dataset → Schedule Post Detail Views

Temporary intermediary view used in downstream materializtion

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vZz_tmp_schedulePostMetric |
| Unique Identifier |  |
| Source Pipeline |  |

## Columns

**Column count:** 14

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Schedule start week date this is defined by the schedule_week_start_day in the schedulePost pipeline settings. |  |  |
| orgId | INTEGER | The orgId for the posted job |  |  |
| postIndicatorCnt | INTEGER | Indicator if the schedule is posted value is 1 if posted and 0 if never posted |  |  |
| postRequiredCnt | INTEGER | If the the Current Date Time the pipeline is running is greater than the postDeadlineDtm the value is 1 otherwise it's 0 |  |  |
| postOnTimeCnt | INTEGER | If the job is posted prior to the postDeadlineDtm the value is 1 otherwise it's 0 |  |  |
| postEarlyHrs | FLOAT | If the job is posted prior to the postDeadlineDtm the value is postDeadLineDtm - firstPostDtm |  |  |
| postLateHrs | FLOAT | If the job is posted after the postDeadlineDtm the value is firstPostDtm - postDeadLineDtm |  |  |
| postDeadlineDiffHrs | FLOAT | The difference between the postDeadLineDtm and firstPostDtm this number will be negative if it's early and positive if its late |  |  |
| postWeekStartDiffHrs | FLOAT | The difference between the partitionDate (Scheduled Week Start Date) and firstPostDtm this number will be negative if it's early and positive if its late |  |  |
| lastPostEarlyHrs | FLOAT | If the last job posting is prior to the postDeadlineDtm the value is postDeadLineDtm - lastPostDtm |  |  |
| lastPostLateHrs | FLOAT | If the last job posting is after the postDeadlineDtm the value is lastPostDtm - postDeadLineDtm |  |  |
| lastPostDeadlineDiffHrs | FLOAT | The difference between the postDeadLineDtm and lastPostDtm this number will be negative if it's early and positive if its late |  |  |
| lastPostWeekStartDiffHrs | FLOAT | The difference between the partitionDate (Scheduled Week Start Date) and lastPostDtm this number will be negative if it's early and positive if its late |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
