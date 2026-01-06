# vSchedulePostJobsByWeek

**Group:** Summary Dataset → metricsIntra (vKronosIntraSummary)

- This view included all jobs by scneduled week whether it was posted or never posted.  Since the API only returns posted jobs we insert never posted jobs and these records will have a postpersonId = -999

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vSchedulePostJobsByWeek |
| Unique Identifier | partionDate,orgId,postPersonId |
| Source Pipeline |  |

## Columns

**Column count:** 20

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Schedule start week date this is defined by the schedule_week_start_day in the schedulePost pipeline settings. |  |  |
| weekEndDate | DATE | Schedule week end date is 6 days after the start date |  |  |
| orgId | INT64 | The orgId for the posted job |  |  |
| firstPostDtm | TIMESTAMP | The date time for the earliest job posting for the scheduled week |  |  |
| lastPostDtm | TIMESTAMP | The date time for the last job posting for the scheduled week |  |  |
| postpersonId | INT64 | Person ID of the person who posted the job |  |  |
| postDeadLineDtm | TIMESTAMP | The defined deadline a job should be posted prior to the scheduled week start date.  This is a calculated field postDeadLineDtm = partitionDate minus postDeadLineHrs |  |  |
| postDeadlineDiffHrs | INT64 | The difference between the postDeadLineDtm and firstPostDtm this number will be negative if it's early and positive if its late |  |  |
| postIndicatorCnt | INT64 | Indicator if the schedule is posted value is 1 if posted and 0 if never posted |  |  |
| postRequiredCnt | INT64 | If the the Current Date Time the pipeline is running is greater than the postDeadlineDtm the value is 1 otherwise it's 0 |  |  |
| postOnTimeCnt | INT64 | If the job is posted prior to the postDeadlineDtm the value is 1 otherwise it's 0 |  |  |
| postEarlyHrs | INT64 | If the job is posted prior to the postDeadlineDtm the value is postDeadLineDtm - firstPostDtm |  |  |
| postLateHrs | INT64 | If the job is posted after the postDeadlineDtm the value is firstPostDtm - postDeadLineDtm |  |  |
| postDeadLineHrs | STRING | The hours defined in schedule_posting_deadline in the schedulePost pipeline settings.  This is used to calculate the postDeadlineDtm |  |  |
| postWeekStartDiffHrs | INT64 | The difference between the partitionDate (Scheduled Week Start Date) and firstPostDtm this number will be negative if it's early and positive if its late |  |  |
| lastPostEarlyHrs | INT64 | If the last job posting is prior to the postDeadlineDtm the value is postDeadLineDtm - lastPostDtm |  |  |
| lastPostLateHrs | INT64 | If the last job posting is after the postDeadlineDtm the value is lastPostDtm - postDeadLineDtm |  |  |
| lastPostDeadlineDiffHrs | INT64 | The difference between the postDeadLineDtm and lastPostDtm this number will be negative if it's early and positive if its late |  |  |
| lastPostWeekStartDiffHrs | INT64 | The difference between the partitionDate (Scheduled Week Start Date) and lastPostDtm this number will be negative if it's early and positive if its late |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
