# vPeopleTelContact

**Group:** Detail Dataset → People Detail Views

- Non-Effective Dated - Phone Numbers

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleTelContact |
| Unique Identifier | personId,contactTypeId |
| Source Pipeline | people (CDC) |
| Scrubbing | DO NOT LOAD |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| smsSwt | BOOLEAN | SMS switch |  |  |
| hasEmailNotificationDeliverySwt | BOOLEAN | has emial notification delivery switch |  |  |
| contactTypeId | INT64 | Contact type ID |  |  |
| contactType | STRING | Contact type | PII | BLANK |
| contactData | STRING | Contact date - phone number | PII | BLANK |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
