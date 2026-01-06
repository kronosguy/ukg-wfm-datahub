# vTimecardPunch

**Group:** Detail Dataset → Timecard Detail Views

- Raw Punches applied to a timecard.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vTimecardPunch |
| Unique Identifier | punchId |
| Source Pipeline | timecard (CDC) |

## Columns

**Column count:** 72

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| punchId | INT64 | Punch ID |  |  |
| partitionDate | DATE | Represents Date Part of punch datetime for the transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| punchDtm | DATETIME | Punch Date Time. The date and time stamp for the punch in ISO_LOCAL_DATE_TIME. |  |  |
| roundedPunchDtm | DATETIME | Rounded Punch Date Time. The date and time stamp for the punch in ISO_LOCAL_DATE_TIME. |  |  |
| timeZoneId | INT64 | Time zone ID |  |  |
| updatedOnDtm | DATETIME | The date and time this record was last updated in ISO_LOCAL_DATE_TIME format (yyyy-MM-dd HH:mm:ss.SSS). |  |  |
| originalPunchDtm | DATETIME | The date and time stamp for the original punch in ISO_LOCAL_DATE_TIME. ** Do Not Use this value is not available or inaccurate ** |  |  |
| enteredOnDtm | DATETIME | The date and time stamp for when this punch transaction was entered through the API. |  |  |
| systemGeneratedSwt | BOOLEAN | A Boolean indicator of whether or not a punch is system-generated. |  |  |
| transferString | STRING | An ordered, semi-colon separated list of Labor Category Entries and Cost Center. |  |  |
| hasCommentsSwt | BOOLEAN | A Boolean indicator that shows whether or not a Comment is associated with a punch. |  |  |
| exceptionResolvedSwt | BOOLEAN | A boolean indicator whether or not the punch exception is resolved |  |  |
| typeOverride | STRING | Provides the type override object which indicates whether this punch object is an in punch, out punch, or a break rule. Break Rule overloads the property. |  |  |
| isScheduledSwt | BOOLEAN | A Boolean indicator of whether or not the punch is generated from a scheduled worked span. |  |  |
| isPhantomSwt | BOOLEAN | A Boolean indicator of whether or not the punch is a phantom punch. |  |  |
| editableSwt | BOOLEAN | A Boolean indicator of whether or not the punch is editable |  |  |
| typeOverrideId | INT64 | Type Override ID |  |  |
| description | STRING | Description of the punch |  |  |
| associatedRuleName | STRING | The associated rule name |  |  |
| associatedRuleId | INT64 | The ID of the associated rule. |  |  |
| breakRule | STRING | A reference to the Break Rule to be applied during calculation of totals resulting from the punch. |  |  |
| breakRuleId | INT64 | Break Rule ID |  |  |
| workRule | STRING | Work Rule Name |  |  |
| workRuleId | INT64 | Work Rule ID |  |  |
| dataSource | STRING | A reference to the data source, if one exists. Normally, this indicates that the punch came from a different source, such as a clock, device, or an external data source such as an import or interface. Note: This can be name of the employee/manager who made the punch |  |  |
| dataSourceId | INT64 | Data source ID |  |  |
| deductRule | STRING | A reference to the Deduct Rule that is applied for cancel deduction. |  |  |
| deductRuleId | INT64 | Deduct rule ID |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension Note: If the punch is associated with a work transfer this value is populated and represents the org the work is transferred to |  |  |
| userEnteredCostCenter | STRING | The user-entered Cost Center (applies to labor category transfer) |  |  |
| userEnteredCostCenterId | INT64 | The user-entered Cost Center ID (applies to labor category transfer) |  |  |
| userEnteredLaborEntryName1 | STRING | Labor Category 1 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryDesc1 | STRING | Labor Category 1 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryName2 | STRING | Labor Category 2 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryDesc2 | STRING | Labor Category 2 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryName3 | STRING | Labor Category 3 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryDesc3 | STRING | Labor Category 3 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryName4 | STRING | Labor Category 4 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryDesc4 | STRING | Labor Category 4 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryName5 | STRING | Labor Category 5 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryDesc5 | STRING | Labor Category 5 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryName6 | STRING | Labor Category 6 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryDesc6 | STRING | Labor Category 6 entry description associated with transaction (applies to labor category transfer) |  |  |
| costCenter | STRING | Cost Center Name  (applies to labor category transfer) |  |  |
| costCenterId | INT64 | Unique Identifier for a CostCenter joins to costCenter dimension  (applies to labor category transfer) |  |  |
| laborEntryName1 | STRING | Labor Category 1 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc1 | STRING | Labor Category 1 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName2 | STRING | Labor Category 2 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc2 | STRING | Labor Category 2 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName3 | STRING | Labor Category 3 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc3 | STRING | Labor Category 3 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName4 | STRING | Labor Category 4 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc4 | STRING | Labor Category 4 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName5 | STRING | Labor Category 5 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc5 | STRING | Labor Category 5 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName6 | STRING | Labor Category 6 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc6 | STRING | Labor Category 6 entry description associated with transaction (applies to labor category transfer) |  |  |
| editByType | STRING | A reference to the type of the user who made the change. Indicates whether the change was made by the employee or by someone else. | PII |  |
| editByTypeId | INT64 | Edit by type ID |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| dataSourceDisplayName | STRING | Source of punch: Time Stamp, Timecard Editor, UDM |  |  |
| dataSourceFunctionalAreaName | STRING | Person ID/DisplayName | PII |  |
| geoLocationId | INT64 | Geograhic Location ID |  |  |
| geoDeviceId | INT64 | Geograhic Location Device ID |  |  |
| geoLongitude | FLOAT | The longitude location of the punch |  |  |
| geoLatitude | FLOAT | The latitude location of the punch |  |  |
| geoAccuracy | FLOAT | Accuracy is a numeric value, in meters, that indicates how confident the device is in the accuracy of the location it is reporting. |  |  |
| geoLocationType | STRING | FINE or COARSE locations. FINE location provides better and accurate locations |  |  |
| geoOutsideOfGeofenceSwt | BOOLEAN | If punch outside GeoFence the value is True |  |  |
| geoUnverifiedSwt | BOOLEAN | If the punch is not verified the value is True |  |  |
| geoUpdateDateTime | DATETIME | Date Time of Punch of Geo Punch |  |  |
