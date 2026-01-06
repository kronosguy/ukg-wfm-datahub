# vEssAvailabilitySegment

**Group:** Detail Dataset → Employee Self Service Detail Views

- Shift segment details for the availability request

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vEssAvailabilitySegment |
| Unique Identifier | All fields |
| Source Pipeline | essAvailability (DR) |

## Columns

**Column count:** 9

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| essAvailabilityId | INT64 | The ID of an availability request. |  |  |
| partitionDate | DATE | The date part of the for the date selected for this request |  |  |
| personId | INT64 | The employee ID of the initiator of an availability request, which is an ID that uniquely identifies an employee. This is not a person number. |  |  |
| availabilityDate | DATE | The availability date for the shift segment |  |  |
| segmentAvailTypeId | INT64 | The availbility type ID for the shift segment |  |  |
| segmentAvailType | STRING | The availbility type name for the shift segment |  |  |
| segmentStartTime | TIME | Shift segment start time |  |  |
| segmentEndTime | TIME | Shift segment end time |  |  |
| updateDtm | DATETIME | pipeline update date time |  |  |
