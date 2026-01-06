# vDeviceDetails

**Group:** Detail Dataset → Device Detail Views

getDeviceDetails

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vDeviceDetails |
| Unique Identifier | id |
| Source Pipeline |  |

## Columns

**Column count:** 21

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| id | INT64 | Unique identifer Device Id |  |  |
| description | STRING | The description of the device. |  |  |
| communicationType | STRING | The communication type of the device. |  |  |
| firmware | STRING | The firmware version of the device. |  |  |
| grantor | STRING | The grantor for the device. |  |  |
| location | STRING | A descriptive string for the device location. |  |  |
| serialNumber | STRING | A descriptive string for the device location. |  |  |
| accessGranted | BOOLEAN | whether or not the device is set for access. |  |  |
| adjustForDST | BOOLEAN | whether or not Adjust for Daylight Savings Time (DST) is enabled. |  |  |
| enabled | BOOLEAN | whether or not the device is enabled. |  |  |
| deviceName | STRING | The name of the device. |  |  |
| deviceId | STRING | The alphanumeric ID of the device. |  |  |
| deviceType | STRING | The device type |  |  |
| deviceTypeId | INT64 | The ID of the device type. |  |  |
| ipAdress | STRING | The device IP Adress |  |  |
| ipAdressId | INT64 | The ID of the device IP address. |  |  |
| deviceProfileName | STRING | the device profile name. |  |  |
| deviceProfileNameId | INT64 | The ID of the device profile name. |  |  |
| deviceTimeZone | STRING | The name of the timezone. |  |  |
| deviceTimeZoneId | STRING | The alphanumeric ID of the timezone. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
