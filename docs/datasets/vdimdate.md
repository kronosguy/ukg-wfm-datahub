# vDimDate

**Group:** Summary Dataset → Dimension Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vDimDate |
| Unique Identifier | All fields |
| Source Pipeline | summary (DR) |

## Columns

**Column count:** 78

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| Date_partitionDate | DATE | Calendar Date |  |  |
| Date_dayOfWkNbr | INT64 | Day of Week |  |  |
| Date_dayOfMoNbr | INT64 | Day of Month |  |  |
| Date_dayOfQtrNbr | INT64 | Day of Quarter |  |  |
| Date_dayOfYrNbr | INT64 | Day of Year |  |  |
| Date_wkOfYrNbr | INT64 | Week of Year |  |  |
| Date_moOfYrNbr | INT64 | Month of Year |  |  |
| Date_qtrOfYrNbr | INT64 | Quarter of Year |  |  |
| Date_yrNbr | INT64 | Year |  |  |
| Date_dayNam | STRING | Day of Week i.e. Sunday, Monday |  |  |
| Date_moNam | STRING | Month Name |  |  |
| Date_qtrNam | STRING | Quarter Name |  |  |
| Date_yrMoNbr | INT64 | Year/Month |  |  |
| Date_lastDayOFYrSwt | BOOLEAN | Boolean indicator where or not this is Last Day of Year |  |  |
| Date_lastDayOfQtrSwt | BOOLEAN | Boolean indicator where or not this is Last Day of Quarter |  |  |
| Date_lastDayOfWkSwt | BOOLEAN | Boolean indicator where or not this is Last Day of Week |  |  |
| Date_lastDayOfMoSwt | BOOLEAN | Boolean indicator where or not this is Last Day of Month |  |  |
| Date_wkEndSwt | BOOLEAN | Boolean indicator where or not this is week end |  |  |
| Date_FsclDayOfWkNbr | INT64 | Fisccal Day of Week |  |  |
| Date_FsclDayOfMoNbr | INT64 | Fiscal Day of Month |  |  |
| Date_FsclDayOfQtrNbr | INT64 | Fiscal Day of Quarter |  |  |
| Date_FsclDayOfYrNbr | INT64 | Fiscal Day of Year |  |  |
| Date_FsclWkOfYrNbr | INT64 | Fiscal Week of Year |  |  |
| Date_FsclMoOfYrNbr | INT64 | Fiscal Month of Year |  |  |
| Date_FsclQtrOfYrNbr | INT64 | Fiscal Quarter of Year |  |  |
| Date_FsclYrNbr | INT64 | Fiscal Year Number |  |  |
| Date_FsclMoNam | STRING | Fiscal Month Name |  |  |
| Date_FsclQtrNam | STRING | Fiscal Quarter Name |  |  |
| Date_FsclYrMoNbr | STRING | Fiscal Year/Month |  |  |
| Date_FsclLastDayOfWkSwt | BOOLEAN | Boolean indicator where or not this is Fiscal Last Day of Week |  |  |
| Date_FsclLastDayOfMoSwt | BOOLEAN | Boolean indicator where or not this is Fiscal Last Day of Month |  |  |
| Date_FsclLastDayOfQtrSwt | BOOLEAN | Boolean indicator where or not this is Fiscal Last Day of Quarter |  |  |
| Date_FsclLastDayOfYrSwt | BOOLEAN | Boolean indicator where or not this is Fiscal Last Day of Year |  |  |
| stp_Today | BOOLEAN | Boolean indicator where or not this is Today |  |  |
| stp_YTD | BOOLEAN | Boolean indicator where or not this is Year to Date |  |  |
| stp_Last30Days | BOOLEAN | Boolean indicator where or not this is Last 30 Days |  |  |
| stp_Last13Weeks | BOOLEAN | Boolean indicator where or not this is Last 13 weeks |  |  |
| stp_LastMonth | BOOLEAN | Boolean indicator where or not this is Last Month |  |  |
| stp_LastQuarter | BOOLEAN | Boolean indicator where or not this is Last Quarter |  |  |
| stp_CurrentQuarter | BOOLEAN | Boolean indicator where or not this is Current Quarter |  |  |
| stp_CurrentMonth | BOOLEAN | Boolean indicator where or not this is Current Month |  |  |
| stp_NextQuarter | BOOLEAN | Boolean indicator where or not this is Next Quarter |  |  |
| stp_NextMonth | BOOLEAN | Boolean indicator where or not this is Next Month |  |  |
| stp_CurrentYear | BOOLEAN | Boolean indicator where or not this is Current Year |  |  |
| stp_LastYear | BOOLEAN | Boolean indicator where or not this is Last Year |  |  |
| stp_Yesterday | BOOLEAN | Boolean indicator where or not this is Yesterday |  |  |
| stp_QTD | BOOLEAN | Boolean indicator where or not this is Quarter to Date |  |  |
| stp_MonthBeforeLast | BOOLEAN | Boolean indicator where or not this is Month before Last |  |  |
| stp_WTD | BOOLEAN | Boolean indicator where or not this is Week to Date |  |  |
| stp_CurrentWeek | BOOLEAN | Boolean indicator where or not this is Current Week |  |  |
| stp_NextWeek | BOOLEAN | Boolean indicator where or not this is Next Week |  |  |
| stp_LastWeek | BOOLEAN | Boolean indicator where or not this is Last Week |  |  |
| stp_Last6MTD | BOOLEAN | Boolean indicator where or not this is Last 6 Months to Date |  |  |
| stp_TwoWeeksOut | BOOLEAN | Boolean indicator where or not this is 2 weeks out |  |  |
| stp_Last8Weeks | BOOLEAN | Boolean indicator where or not this is Last 8 Weeks |  |  |
| stp_MTD | BOOLEAN | Boolean indicator where or not this is Month to Date |  |  |
| stp_ThreeWeeksOut | BOOLEAN | Boolean indicator where or not this is 3 weeks out |  |  |
| stp_FsclLast13Weeks | BOOLEAN | Boolean indicator where or not this is Fiscal Last 13 weeks |  |  |
| stp_FsclLastMonth | BOOLEAN | Boolean indicator where or not this is Fiscal Last Month |  |  |
| stp_FsclLastQuarter | BOOLEAN | Boolean indicator where or not this is Fiscal Last Quarter |  |  |
| stp_FsclCurrentQuarter | BOOLEAN | Boolean indicator where or not this is Fiscal Current Quarter |  |  |
| stp_FsclCurrentMonth | BOOLEAN | Boolean indicator where or not this is Fiscal Curent Month |  |  |
| stp_FsclNextQuarter | BOOLEAN | Boolean indicator where or not this is Fiscal Next Quarter |  |  |
| stp_FsclNextMonth | BOOLEAN | Boolean indicator where or not this is Fiscal Next Month |  |  |
| stp_FsclCurrentYear | BOOLEAN | Boolean indicator where or not this is Fiscal Current Year |  |  |
| stp_FsclLastYear | BOOLEAN | Boolean indicator where or not this is Fiscal Last Year |  |  |
| stp_FsclYTD | BOOLEAN | Boolean indicator where or not this is Fiscal Year to Date |  |  |
| stp_FsclQTD | BOOLEAN | Boolean indicator where or not this is Fiscal Quarter to Date |  |  |
| stp_FsclMonthBeforeLast | BOOLEAN | Boolean indicator where or not this is Fiscal Month before Last |  |  |
| stp_FsclWTD | BOOLEAN | Boolean indicator where or not this is Fiscal Week to Date |  |  |
| stp_FsclCurrentWeek | BOOLEAN | Boolean indicator where or not this is Fiscal Current Week |  |  |
| stp_FsclNextWeek | BOOLEAN | Boolean indicator where or not this is Fiscal Next Week |  |  |
| stp_FsclLastWeek | BOOLEAN | Boolean indicator where or not this is Fiscal Last Week |  |  |
| stp_FsclLast6MTD | BOOLEAN | Boolean indicator where or not this is Fiscal Last 6 Month to Date |  |  |
| stp_FsclTwoWeeksOut | BOOLEAN | Boolean indicator where or not this is Fiscal Year 2 Weeks Out |  |  |
| stp_FsclLast8Weeks | BOOLEAN | Boolean indicator where or not this is Fiscal Last 8 weeks |  |  |
| stp_FsclMTD | BOOLEAN | Boolean indicator where or not this is Fiscal Month to Date |  |  |
| stp_FsclThreeWeeksOut | BOOLEAN | Boolean indicator where or not this is Fiscal Year 3 Weeks Out |  |  |
