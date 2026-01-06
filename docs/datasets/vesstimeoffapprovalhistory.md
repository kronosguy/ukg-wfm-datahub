# vEssTimeOffApprovalHistory

**Group:** Detail Dataset → Employee Self Service Detail Views

- Time Off Approval History

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vEssTimeOffApprovalHistory |
| Unique Identifier | All fields |
| Source Pipeline | essTimeOff (DR) |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| essTimeOffId | INT64 | time off request id |  |  |
| partitionDate | DATE | The start date of the request |  |  |
| personId | INT64 | The employee ID of the initiator of an shift swap request, which is an ID that uniquely identifies an employee.This is not a person number. |  |  |
| approvalStep | INT64 | The number of the approval step. |  |  |
| approvalPersonId | INT64 | Person id for employee that reviewed the request |  |  |
| approvalSwt | BOOLEAN | A Boolean indicator of whether or not the reviewer approved the approval step. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
