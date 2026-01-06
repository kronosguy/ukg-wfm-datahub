# vCalendarDate

**Group:** Detail Dataset → Date/Time Detail Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vCalendarDate |
| Unique Identifier | DATE_DAT |
| Source Pipeline | This data is populated as silver data. Loaded via BQ Cloud Function |

## Columns

**Column count:** 35

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| DATE_DAT | DATE | Calendar Date of Year |  |  |
| DAY_NAM | STRING | Day name Sunday, Monday ... |  |  |
| DAY_OF_WK_NBR | INT64 | Calendar day of week Sunday = 1, Monday = 2 .. |  |  |
| LAST_DAY_OF_MO_SWT | BOOLEAN | Is the last day of month |  |  |
| DAY_OF_YR_NBR | INT64 | Calendar day of year Jan 1 = 1, Feb 1 = 32 ... |  |  |
| WK_OF_YR_NBR | INT64 | Calender week of year values 1 thru 52 |  |  |
| DAY_OF_MO_NBR | INT64 | Calendar day of month Jan 1 = 1, Jan 31 = 31 |  |  |
| LAST_DAY_OF_QTR_SWT | BOOLEAN | Is last day of Quarter |  |  |
| WKEND_SWT | BOOLEAN | Is weekend |  |  |
| MO_OF_YR_NBR | INT64 | Calendar month of year Jan = 1, Feb = 2 ... |  |  |
| MO_NAM | STRING | Month name January, February ... |  |  |
| QTR_OF_YR_NBR | INT64 | Calendar Quarter of Year |  |  |
| DAY_OF_QTR_NBR | INT64 | Calendar Day within the Quarter |  |  |
| YR_NBR | INT64 | Calendar Year 2021, 2022 ... |  |  |
| QTR_NAM | STRING | Calendar Quarter Name Q1, Q2 |  |  |
| YR_MO_NBR | INT64 | Caledar Year Number combined with Calendar Month Jan 2022 = 202201 |  |  |
| LAST_DAY_OF_WK_SWT | BOOLEAN | Is the last day of week |  |  |
| LAST_DAY_OF_YR_SWT | BOOLEAN | Is the last day of year |  |  |
| vTime | A time view used in materializations of 15 min views |  |  |  |
| timeMinute | INT64 | Time minute segment |  |  |
| timeQtr24H | TIME | Time Quarter 24H |  |  |
| timeQtr12H | TIME | Time Quarter 12H |  |  |
| time24H | TIME | Time 24H |  |  |
| time12H | TIME | Time 12H |  |  |
| timeHourEnd | BOOLEAN | A boolean indicator whether or not its the end of an hour |  |  |
| timeAmPm | STRING | AM/PM designator |  |  |
| timeDayTime | TIMESTAMP | Time stamp |  |  |
| timeQtrStart | BOOLEAN | A boolean indicator whether or not its the start of a quarter |  |  |
| timeHour | INT64 | Time hour segment |  |  |
| timeHalf24H | TIME | The time portion of segment in 24H |  |  |
| timeHalf12H | TIME | The time portion of segment in 12H |  |  |
| timeHourStart | BOOLEAN | A boolean indicator whether or not its the start of a hour |  |  |
| timeHalfEnd | BOOLEAN | A boolean indicator whether or not its the half of end segment |  |  |
| timeHalfStart | BOOLEAN | A boolean indicator whether or not its the half of start segment |  |  |
| timeQtrEnd | BOOLEAN | A boolean indicator whether or not its the end of a quarter |  |  |
