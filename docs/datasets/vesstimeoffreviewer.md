# vEssTimeOffReviewer

**Group:** Detail Dataset → Employee Self Service Detail Views

- Time Off Reviewers

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vEssTimeOffReviewer |
| Unique Identifier | All fields |
| Source Pipeline | essTimeOff (DR) |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| essTimeOffId | INT64 | time off request id |  |  |
| partitionDate | DATE | The start date of the request |  |  |
| personId | INT64 | The employee ID of the initiator of  time off request, which is an ID that uniquely identifies an employee.This is not a person number. |  |  |
| reviewerPersonId | INT64 | The employee ID of a reviewer, which is an ID that uniquely identifies an employee. This is not a person number. |  |  |
| approvalSwt | BOOLEAN | A Boolean indicator of whether or not the reviewer approved the approval step. |  |  |
| approvalStep | INT64 | The number of the approval step. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
