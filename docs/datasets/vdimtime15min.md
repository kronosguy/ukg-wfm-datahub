# vDimTime15min

**Group:** Summary Dataset → Dimension Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vDimTime15min |
| Unique Identifier | time_12H,time_24H |
| Source Pipeline |  |

## Columns

**Column count:** 16

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| time_DayTime | TIMESTAMP | Day Time Stamp in UTC |  |  |
| time_Minute | INT64 | Minute Part of time |  |  |
| time_24H | TIME | 24 hour tim |  |  |
| time_12H | TIME | 12 hour time |  |  |
| time_AmPm | STRING | AM/PPM |  |  |
| time_Hour | INT64 | Hour Part of time |  |  |
| time_HourStart | BOOLEAN | Boolean inidictator whether or not this is Start of Hour |  |  |
| time_HourEnd | BOOLEAN | Boolean inidictator whether or not this is End of Hour |  |  |
| time_Half24H | TIME | Half of 24H |  |  |
| time_Half12H | TIME | Half of 12H |  |  |
| time_HalfStart | BOOLEAN | Boolean inidictator whether or not this is Half Start |  |  |
| time_HalfEnd | BOOLEAN | Boolean inidictator whether or not this is Half End |  |  |
| time_Qtr24H | TIME | Quarter of 24h |  |  |
| time_Qtr12H | TIME | Quarter of 12h |  |  |
| time_QtrStart | BOOLEAN | Boolean inidictator whether or not this is Start of Quarter |  |  |
| time_QtrEnd | BOOLEAN | Boolean inidictator whether or not this is End of Quarter |  |  |
